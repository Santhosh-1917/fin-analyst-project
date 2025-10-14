-- create_dim_date.sql
-- Create and populate date dimension for Power BI / analytics

CREATE TABLE IF NOT EXISTS dim_date (
    date_id SERIAL PRIMARY KEY,
    full_date DATE NOT NULL,
    year INT,
    quarter INT,
    month INT,
    month_name TEXT,
    day INT
);

-- Populate dim_date table (2006–2026 range)
INSERT INTO dim_date (full_date, year, quarter, month, month_name, day)
SELECT d::DATE,
       EXTRACT(YEAR FROM d),
       EXTRACT(QUARTER FROM d),
       EXTRACT(MONTH FROM d),
       TO_CHAR(d, 'Month'),
       EXTRACT(DAY FROM d)
FROM GENERATE_SERIES('2006-01-01'::DATE, '2026-12-31'::DATE, '1 day'::INTERVAL) d;