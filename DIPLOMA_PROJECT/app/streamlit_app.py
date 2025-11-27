import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import numpy as np

# === CONFIGURATION ===
st.set_page_config(
    page_title="NGO Grant Scoring",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === PATHS ===
# Определяем пути относительно файла приложения
APP_DIR = Path(__file__).parent
PROJECT_ROOT = APP_DIR.parent
MODEL_PATH = PROJECT_ROOT / 'reports' / 'best_model.pkl'

# === STYLING ===
st.markdown("""
    <style>
    .main {
        background-color: #0f0c29;
        color: white;
    }
    .stButton>button {
        width: 100%;
        background-color: #00f2ff;
        color: #0f0c29;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #b026ff;
        color: white;
    }
    h1, h2, h3 {
        color: #00f2ff;
    }
    .metric-card {
        background-color: #1a1a2e;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00f2ff;
    }
    </style>
    """, unsafe_allow_html=True)

# === LOAD MODEL ===
@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        st.error(f"❌ Модель не найдена по пути: {MODEL_PATH}")
        return None
    return joblib.load(MODEL_PATH)

model = load_model()

# === SIDEBAR: INPUTS ===
st.sidebar.header("📝 Параметры НКО")

def user_input_features():
    # Группа 1: Основные данные
    st.sidebar.subheader("1. Основные данные")
    region_name = st.sidebar.selectbox("Регион", ['Москва', 'Санкт-Петербург', 'Московская область', 'Другой'])
    age_years = st.sidebar.slider("Возраст организации (лет)", 0.0, 30.0, 5.0)
    okved_category = st.sidebar.selectbox("Категория ОКВЭД", ['85 (Образование)', '88 (Соц. услуги)', '94 (Членские орг.)', 'Другой'])
    
    # Группа 2: Финансы
    st.sidebar.subheader("2. Финансы (2021)")
    income_2021 = st.sidebar.number_input("Доходы (RUB)", min_value=0, value=1000000)
    assets_2021 = st.sidebar.number_input("Активы (RUB)", min_value=0, value=500000)
    has_fin_report = 1 if income_2021 > 0 else 0
    
    # Группа 3: Цифровой след
    st.sidebar.subheader("3. Цифровой след")
    has_vk_2022 = st.sidebar.checkbox("Есть верифицированный VK (2022)?", value=True)
    has_website = st.sidebar.checkbox("Есть веб-сайт?", value=True)
    
    # Сборка DataFrame (должен совпадать с признаками модели)
    # Упрощенная версия для демо (в реальности нужно больше полей)
    data = {
        'region_name': region_name,
        'age_years': age_years,
        'okved_category': okved_category.split(' ')[0],
        'income_2021': income_2021,
        'assets_2021': assets_2021,
        'has_fin_report': has_fin_report,
        'has_vk_2022': int(has_vk_2022),
        'has_website': int(has_website),
        # Заглушки для остальных полей, которые ожидает модель
        'opf_name': 'Unknown',
        'opf_type': 'Unknown',
        'add_okved_count': 0,
        'has_social_add_okved': 0,
        'social_media_count': 1 if has_vk_2022 else 0,
        'has_vk': int(has_vk_2022),
        'has_ok': 0,
        'has_youtube': 0,
        'leaders_count': 1,
        'reports_count': 1,
        'last_report_year': 2021,
        'founders_type': 'Unknown',
        'has_regional_support': 0,
        'minjust_status': 'Действует',
        'expenses_2021': income_2021 * 0.9, # Предполагаем
        'profit_2021': income_2021 * 0.1,
        'has_website_2022': int(has_website)
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# === MAIN PANEL ===
st.title("🎓 NGO Grant Scoring System")
st.markdown("### Система оценки вероятности получения госфинансирования")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### 📊 Введенные данные")
    st.dataframe(input_df[['region_name', 'age_years', 'income_2021', 'has_vk_2022']])

    if st.button("🚀 Рассчитать вероятность"):
        if model:
            # Предсказание
            try:
                # В реальном проекте здесь нужен полноценный препроцессинг (как в ноутбуке)
                # Для демо предполагаем, что модель (Pipeline) сама обработает сырые данные
                # или используем упрощенную логику.
                # ВАЖНО: CatBoost умеет работать с категориями, если они указаны.
                # Если модель - Pipeline с OneHotEncoder, она справится.
                
                prediction_proba = model.predict_proba(input_df)[0][1]
                
                st.markdown("---")
                st.markdown("### Результат скоринга")
                
                # Визуализация результата
                col_res1, col_res2 = st.columns(2)
                
                with col_res1:
                    st.metric(label="Вероятность успеха", value=f"{prediction_proba:.1%}")
                
                with col_res2:
                    if prediction_proba > 0.7:
                        st.success("✅ **Высокий шанс** (Зеленый коридор)")
                        st.markdown("Рекомендация: **Поддерживать**")
                    elif prediction_proba < 0.3:
                        st.error("⛔ **Низкий шанс** (Красный коридор)")
                        st.markdown("Рекомендация: **Отказать / Обучение**")
                    else:
                        st.warning("⚠️ **Средний шанс** (Серая зона)")
                        st.markdown("Рекомендация: **Ручная проверка**")
                        
                # Прогресс бар
                st.progress(prediction_proba)
                
            except Exception as e:
                st.error(f"Ошибка при расчете: {e}")
                st.info("💡 Убедитесь, что входные данные соответствуют формату обучения модели.")

with col2:
    st.markdown("#### ℹ️ О модели")
    st.info("""
    **Модель:** CatBoost Classifier
    **Метрика ROC-AUC:** > 0.80
    
    **Топ факторов:**
    1. 💰 Доходы (Income)
    2. 📱 Соцсети (VK 2022)
    3. 📅 Возраст (Age)
    """)
    
    st.markdown("---")
    st.caption("Developed by Kokorin V.A. | SkillFactory")

