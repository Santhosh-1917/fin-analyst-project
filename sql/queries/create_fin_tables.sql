-- Create company dimension
CREATE TABLE IF NOT EXISTS dim_company (
    company_id SERIAL PRIMARY KEY,
    company_name TEXT NOT NULL,
    ticker TEXT UNIQUE,
    sector TEXT
);

-- Create date dimension
CREATE TABLE IF NOT EXISTS dim_date (
    date_id SERIAL PRIMARY KEY,
    date DATE UNIQUE NOT NULL,
    year INT,
    month INT,
    month_name TEXT
);

-- Create fact table
CREATE TABLE IF NOT EXISTS fact_financials (
    fact_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES dim_company(company_id),
    date_id INT REFERENCES dim_date(date_id),
    accounts_receivable NUMERIC,
    assets NUMERIC,
    assets_current NUMERIC,
    cash NUMERIC,
    gross_profit NUMERIC,
    income_before_tax NUMERIC,
    income_tax NUMERIC,
    inc_dec_receivable NUMERIC,
    inc_dec_other_receivable NUMERIC,
    inventory NUMERIC,
    liabilities NUMERIC,
    liabilities_current NUMERIC,
    net_cash_financing NUMERIC,
    net_cash_investing NUMERIC,
    net_cash_operating NUMERIC,
    net_income NUMERIC,
    operating_expenses NUMERIC,
    operating_income NUMERIC,
    rd_expense NUMERIC,
    stockholders_equity NUMERIC
);