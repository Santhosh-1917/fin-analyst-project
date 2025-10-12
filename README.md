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