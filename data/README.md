# Data Description

## Raw Data (`data/raw/`)

This directory contains the source datasets for the NGO Grant Prediction project.

### 1. NGO Registry Dump (`ngo_dump_*.zip`)
- **Source:** [OpenNGO](https://openngo.ru/)
- **Content:** Full registry of Russian NGOs in JSON format, compressed into multiple ZIP archives.
- **Usage:** Used to extract base features (region, age, OKVED, founders, reports).

### 2. Financial Statements (`buh_data.csv`)
- **Source:** Rosstat / Federal Tax Service (via aggregator)
- **Content:** Financial indicators for 2019-2021 (Income, Expenses, Assets, Profit).
- **Usage:** Used to assess financial capacity (`income_2021`, `assets_2021`).

### 3. Social Media Verification (`2022_lab_vk_pages_website_ogrn.csv`)
- **Source:** Laboratory of Civil Society Research (Internal/Parsed)
- **Content:** List of verified VKontakte pages and websites for NGOs as of 2022.
- **Usage:** Used to validate digital presence (`has_vk_2022`, `has_website_2022`).

### 4. Foundation Codes (`foundations_codes.csv`)
- **Source:** Manual mapping
- **Content:** Codes to identify specific types of foundations.

## Processed Data (`data/processed/`)
- This folder is used to store intermediate files (e.g., cleaned Parquet files).
- Currently empty (data is processed in-memory).
