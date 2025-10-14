# 📊 SEC EDGAR Financial Analytics & Forecasting with SQL

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/) [![SQL](https://img.shields.io/badge/SQL-Structured--Query--Language-green.svg)](https://www.w3schools.com/sql/) [![Power BI](https://img.shields.io/badge/Power%20BI-Data%20Visualization-yellow.svg)](https://powerbi.microsoft.com/) [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🚀 Overview
This project develops a robust financial analytics and forecasting pipeline leveraging SEC EDGAR 10-K and 10-Q filings. It automates data extraction via the SEC EDGAR API, transforms and integrates financial data into SQL databases, conducts KPI trend analysis, and visualizes insights interactively using Power BI.

## 🔄 Data Pipeline (ETL)
- **Extract:** Automated retrieval of SEC filings for selected companies using the SEC EDGAR API.  
- **Transform:** Parsing and cleaning of financial statements; conversion into structured SQL tables for efficient querying.  
- **Load:** Integration of transformed data into SQL databases to enable advanced analytics and forecasting.  
- **Analyze & Visualize:** KPI trend analysis and forecasting with Prophet, followed by interactive dashboards in Power BI.

## 🧠 Companies
- **Apple (AAPL)** - *Completed*  
- Tesla (TSLA) - *In Progress*  
- Pfizer (PFE) - *Upcoming*  
- Walmart (WMT) - *Upcoming*  
- JPMorgan Chase (JPM) - *Upcoming*

## 🧰 Tech Stack
- Python  
- SEC EDGAR API  
- SQLAlchemy & SQL  
- Pandas  
- Prophet (for forecasting)  
- Power BI (for visualization)

## 📁 Folder Structure
```
/data               # Raw and processed financial data files  
/scripts            # Python scripts for extraction, transformation, and loading  
/sql                # SQL scripts and schema definitions  
/powerbi            # Power BI reports and dashboards  
/notebooks          # Jupyter notebooks for exploratory analysis  
/README.md          # Project documentation  
```

## 📈 Results & Next Steps
- Successfully automated the ETL pipeline and analysis for Apple Inc.  
- Building out similar pipelines for Tesla, Pfizer, Walmart, and JPMorgan Chase.  
- Enhancing forecasting models and expanding Power BI dashboards for broader financial insights.

## 👤 Author
**Santhosh Narayanan**  
Financial Data Analyst | Python & SQL Enthusiast | Data Visualization Specialist
# 📊 SEC EDGAR Financial Analytics & Forecasting with SQL  

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/) [![SQL](https://img.shields.io/badge/SQL-Structured--Query--Language-green.svg)](https://www.w3schools.com/sql/) [![Power BI](https://img.shields.io/badge/Power%20BI-Data%20Visualization-yellow.svg)](https://powerbi.microsoft.com/) [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Overview  
This project builds an **end-to-end financial analytics and forecasting pipeline** leveraging **SEC EDGAR 10-K and 10-Q filings**.  
It automates **data extraction**, **cleaning**, and **SQL integration**, performs **trend analysis and forecasting**, and visualizes insights using **Power BI**.

---

## 🔄 Data Pipeline (ETL)  
- **Extract:** Retrieve SEC filings automatically using the EDGAR API.  
- **Transform:** Parse and clean financial statements, normalize metrics, and unify schema across filings.  
- **Load:** Store structured financial data into SQL databases for scalable analytics.  
- **Analyze & Visualize:** Perform KPI trend analysis, forecasting with Prophet/ARIMA, and create dashboards in Power BI.

---

## 🧠 Companies  
- **Apple (AAPL)** — ✅ Completed  
- **Tesla (TSLA)** — 🔄 In Progress  
- **Pfizer (PFE)** — ⏳ Upcoming  
- **Walmart (WMT)** — ⏳ Upcoming  
- **JPMorgan Chase (JPM)** — ⏳ Upcoming  

---

## 🧰 Tech Stack  
- **Python 3.12+**  
- **SEC EDGAR API** (XBRL data extraction)  
- **SQLAlchemy + SQL** (ETL and schema integration)  
- **Pandas / Matplotlib / Seaborn** (EDA and data processing)  
- **Prophet / ARIMA (Forecasting)**  
- **Power BI** (Interactive visualization)

---

## 📁 Folder Structure  
```
fin_analyst_project/
├── data/
│   ├── raw/           # SEC JSON & CSV files
│   ├── processed/     # Cleaned & filled datasets
│   └── config/        # Tag lists and API parameters
├── src/
│   ├── EDA_api.ipynb              # Exploratory data analysis for raw tags
│   ├── rev_eda.ipynb              # Revenue cleaning & GAAP transition checks
│   ├── apple_csv_check.ipynb      # Final preprocessing & missing-value EDA
│   ├── revenue_Apple_build.py     # Merge financial tags into main dataset
│   └── parse_apple.py             # Parse raw SEC JSON data
├── sql/             # SQL schema and queries
├── powerbi/         # Power BI dashboards and visuals
├── notebooks/       # Exploratory Jupyter notebooks
└── README.md        # Project documentation
```

---

## 📊 Project Progress  

### ✅ 1. Data Extraction  
- Extracted ~28 financial tags via the **SEC EDGAR API** for Apple Inc.  
- Downloaded JSON files representing income statement, balance sheet, and cash flow components.

### ✅ 2. Revenue Cleanup & GAAP Transition  
- Combined multiple revenue tags:
  - `SalesRevenueNet`  
  - `Revenues`  
  - `RevenueFromContractWithCustomerExcludingAssessedTax`  
- Detected **ASC 606 transition (2018)**:
  - Pre-2018 → `SalesRevenueNet`
  - Post-2018 → `RevenueFromContractWithCustomerExcludingAssessedTax`
- Unified temporary column `Revenue_Final` (later dropped due to inconsistencies).

### ✅ 3. Merging & Normalization  
- Merged all financial tags by date (`end`).  
- Scaled values (millions) and added time-based fields (`Year`, `Month`, `Month_Name`).  
- Ensured no duplicate year-month records.

### ✅ 4. Missing-Value Analysis  
- Visualized missingness via bar and heatmaps.  
- Dropped metrics with >30% missing data.  
- Identified **clean analysis window → 2010–2025**.

### ✅ 5. Interpolation & Final Clean File  
- Interpolated numeric values (<15% missing).  
- Forward/backward filled edges.  
- Exported cleaned dataset →  
  ```
  data/processed/apple_preprocess_1.csv
  ```
  ✅ Shape: (62, 24)  
  ✅ Date Range: 2010–01–01 → 2025–05–29  

---

## 🗂️ Version History  
| Version | File | Description | Status |
|:--:|:--|:--|:--|
| v0 | `apple_clean_2010_2025.csv` | Base filtered dataset (2010–2025) | Reference |
| v1 | `apple_preprocess_1.csv` | Filled/interpolated numeric columns | ✅ Final for SQL/Power BI |

---

## 📈 Results & Next Steps  

### ✅ Current Achievements  
- Fully automated **ETL pipeline and analysis for Apple Inc.**  
- Established reusable structure for multi-company integration.  

### 🚀 Next Steps  
- Build SQL schema (`FactFinancials` + `DimDate`).  
- Load Apple data into SQL for relational querying.  
- Connect to Power BI for visualization and forecasting dashboards.  
- Extend pipeline to Tesla, Pfizer, Walmart, and JPMorgan Chase.  

### 🧩 Pending Tasks  
- Handle remaining missing columns:
  - `AssetsNoncurrent`, `LiabilitiesNoncurrent`, `DepreciationDepletionAndAmortization`,  
    `LongTermDebtNoncurrent`, `SalesRevenueNet`, `RevenueFromContractWithCustomerExcludingAssessedTax`
- Merge into unified `Revenue_Final` and validate via correlation heatmap before SQL load.

---

## 👤 Author  
**Santhosh Narayanan**  
> Financial Data Analyst | Python & SQL Enthusiast | Data Visualization Specialist  

---