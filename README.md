# 📊 SEC EDGAR Financial Analytics & Forecasting with SQL

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/) [![SQL](https://img.shields.io/badge/SQL-Structured--Query--Language-green.svg)](https://www.w3schools.com/sql/) [![Power BI](https://img.shields.io/badge/Power%20BI-Data%20Visualization-yellow.svg)](https://powerbi.microsoft.com/) [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Overview
This project builds an **end-to-end financial analytics and forecasting pipeline** leveraging **SEC EDGAR 10-K and 10-Q filings**.  
It automates **data extraction**, **cleaning**, **SQL integration**, and **Power BI visualization**, providing a real-world demonstration of full-stack financial analytics — from raw data to insights.

---

## 🔄 ETL Workflow
1. **Extract:** SEC EDGAR API → 10-K & 10-Q filings (JSON).  
2. **Transform:** Clean, merge, and normalize financial tags using Python (Pandas).  
3. **Load:** Store structured data into PostgreSQL star schema.  
4. **Visualize:** Build Power BI dashboards with financial KPIs & forecasting.

---

## 🧰 Tech Stack
- **Languages:** Python, SQL  
- **Libraries:** Pandas, Matplotlib, Seaborn, Prophet, ARIMA  
- **Database:** PostgreSQL 14  
- **Visualization:** Power BI (Windows VM), Tableau  
- **API Source:** SEC EDGAR (XBRL data)

---

## 🧠 Companies Covered
| Company | Status |
|:--|:--:|
| Apple (AAPL) | ✅ Completed |
| Tesla (TSLA) | 🔄 In Progress |
| Pfizer (PFE) | ⏳ Upcoming |
| Walmart (WMT) | ⏳ Upcoming |
| JPMorgan Chase (JPM) | ⏳ Upcoming |

---

## 🧱 SQL Database Schema
Three core tables form the **star schema**:
- **dim_company** → company metadata (id, name, sector)  
- **dim_date** → fiscal calendar (date_id, year, quarter, month)  
- **fact_financials** → financial measures (revenue, net_income, assets, liabilities)

```sql
CREATE TABLE dim_company (
  company_id SERIAL PRIMARY KEY,
  company_name TEXT,
  sector TEXT
);

CREATE TABLE dim_date (
  date_id SERIAL PRIMARY KEY,
  full_date DATE,
  fiscal_year INT,
  fiscal_quarter INT,
  month_name TEXT
);

CREATE TABLE fact_financials (
  fact_id SERIAL PRIMARY KEY,
  company_id INT REFERENCES dim_company(company_id),
  date_id INT REFERENCES dim_date(date_id),
  revenue_final NUMERIC,
  net_income NUMERIC,
  assets NUMERIC,
  liabilities NUMERIC
);
```

---

## 🧠 SQL Roadmap
| Stage | Focus | Skills Demonstrated |
|:--|:--|:--|
| **Modeling & Setup** | Build star schema with PK/FK | Database design |
| **ETL & Data Loading** | Load CSV via COPY | ETL automation |
| **Data Quality** | Validate nulls & duplicates | QA, validation |
| **Analytical Queries** | Create KPIs & ratios | Aggregation, joins |
| **Advanced SQL** | Window functions & CTEs | YOY/QoQ trend analysis |
| **Optimization** | Indexes & VIEWs | Performance tuning |
| **Automation** | Stored procedures, pgAgent | Scheduling |
| **Integration** | Connect PostgreSQL → Power BI | BI workflow |

---

## 📊 Power BI Dashboard
Visuals include:
- **Revenue & Net Income Trends (2010–2025)**
- **Profit Margin & YOY Growth KPIs**
- **Assets vs Liabilities Analysis**
- **R&D & Operating Expense Trends**
- **Company-level slicers and date filters**

> Tableau is also used for comparative dashboards and public visualization of forecast results, enabling interactive sharing and broader accessibility of key financial insights.

---

## 📈 Forecasting Extension
This extension implements predictive modeling using **Prophet** and **ARIMA** within Python notebooks to forecast key financial metrics such as revenue and net income. The forecasting workflow includes data preparation, model training, evaluation, and visualization of forecast results. Forecast outputs are integrated back into PostgreSQL to enable seamless Power BI visualization alongside historical data.

Key implementation details:
- Python notebooks for time series modeling and diagnostics.
- Use of Pandas for data manipulation and Matplotlib/Seaborn for plotting forecast trends.
- Integration scripts to load forecast results into a dedicated PostgreSQL table.
- Power BI connects to both historical and forecasted data for hybrid views.

Modeling steps:
- Data preparation: Clean and format historical financial data for modeling.
- Training: Fit Prophet and ARIMA models on historical time series.
- Evaluation: Assess model accuracy using metrics such as RMSE and MAPE.
- Visualization: Plot forecasted trends with confidence intervals.

Example SQL snippet to integrate forecast results:

```sql
CREATE TABLE fact_forecast (
  forecast_id SERIAL PRIMARY KEY,
  company_id INT REFERENCES dim_company(company_id),
  date_id INT REFERENCES dim_date(date_id),
  forecast_metric TEXT,
  forecast_value NUMERIC,
  confidence_lower NUMERIC,
  confidence_upper NUMERIC
);

INSERT INTO fact_forecast (company_id, date_id, forecast_metric, forecast_value, confidence_lower, confidence_upper)
VALUES
  (1, 20260101, 'revenue_final', 1500000000, 1400000000, 1600000000),
  (1, 20260101, 'net_income', 120000000, 110000000, 130000000);
```

---

## 🗓️ Project Timeline
| Phase | Status | Key Deliverables |
|:--|:--|:--|:--|
| **Phase 1 – Data Extraction & Cleaning** | ✅ Done | API integration, missing-value interpolation |
| **Phase 2 – SQL Modeling & Integration** | ✅ Done | Star schema + loaded Apple dataset |
| **Phase 3 – Power BI Integration** | ✅ Done | Interactive visuals + KPI model |
| **Phase 4 – Advanced SQL & Forecasting** | 🔄 Ongoing | CTEs, window functions, Prophet/ARIMA |
| **Phase 5 – Automation & Scaling** | 🔜 Planned | Multi-company ETL + stored procedures |

---

## 🧾 Example Query
```sql
SELECT 
  c.company_name,
  d.fiscal_year,
  ROUND(SUM(f.net_income)/NULLIF(SUM(f.revenue_final),0)*100, 2) AS profit_margin,
  SUM(f.revenue_final) AS total_revenue
FROM fact_financials f
JOIN dim_company c ON f.company_id = c.company_id
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY c.company_name, d.fiscal_year
ORDER BY c.company_name, d.fiscal_year;
```

---

## 🎯 Outcomes
- Full ETL + analytics pipeline built for **Apple Inc.** (2010–2025).  
- SQL-based KPIs integrated seamlessly into **Power BI**.  
- Ready for multi-company scaling and predictive analytics.  

---

## 👤 Author
**Santhosh Narayanan**  
> Financial Data Analyst | Python & SQL Enthusiast | Power BI Developer  