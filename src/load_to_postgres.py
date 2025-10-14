import pandas as pd
from sqlalchemy import create_engine, text

# ================================
# 🔧 Database Configuration
# ================================
DB_NAME = "fin_analytics"
DB_USER = "santhosh"      # change if you use a different username
DB_PASS = ""              # add password if your local DB uses one
DB_HOST = "localhost"
DB_PORT = "5432"

# ================================
# 📁 Load the Preprocessed CSV
# ================================
file_path = "/Users/santhosh/Desktop/fin analyst project/data/processed/apple_preprocess_1.csv"

print("🔹 Loading dataset...")
df = pd.read_csv(file_path)

print(f"✅ Loaded CSV — {df.shape[0]} rows, {df.shape[1]} columns")

# ================================
# 🧩 Basic Data Preparation
# ================================

# Rename columns to match your SQL schema
rename_map = {
    "AccountsReceivableNetCurrent": "accounts_receivable",
    "Assets": "assets",
    "AssetsCurrent": "assets_current",
    "CashAndCashEquivalentsAtCarryingValue": "cash",
    "GrossProfit": "gross_profit",
    "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest": "income_before_tax",
    "IncomeTaxExpenseBenefit": "income_tax",
    "IncreaseDecreaseInAccountsReceivable": "inc_dec_receivable",
    "IncreaseDecreaseInOtherReceivables": "inc_dec_other_receivable",
    "InventoryNet": "inventory",
    "Liabilities": "liabilities",
    "LiabilitiesCurrent": "liabilities_current",
    "NetCashProvidedByUsedInFinancingActivities": "net_cash_financing",
    "NetCashProvidedByUsedInInvestingActivities": "net_cash_investing",
    "NetCashProvidedByUsedInOperatingActivities": "net_cash_operating",
    "NetIncomeLoss": "net_income",
    "OperatingExpenses": "operating_expenses",
    "OperatingIncomeLoss": "operating_income",
    "ResearchAndDevelopmentExpense": "rd_expense",
    "StockholdersEquity": "stockholders_equity"
}

df.rename(columns=rename_map, inplace=True)

# Add company_id (Apple = 1)
df["company_id"] = 1

# Convert date columns
df["end"] = pd.to_datetime(df["end"])
df["year"] = pd.to_datetime(df["end"]).dt.year
df["month"] = pd.to_datetime(df["end"]).dt.month

# Drop extra columns not in SQL schema
columns_to_keep = list(rename_map.values()) + ["company_id"]
df_final = df[columns_to_keep]

# ================================
# 🧠 Load into PostgreSQL
# ================================
conn_str = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(conn_str)

try:
    with engine.begin() as conn:
        df_final.to_sql("fact_financials", conn, if_exists="append", index=False)
    print("✅ Data successfully loaded into fact_financials!")
except Exception as e:
    print("❌ Error during load:", e)

# ================================
# 🔍 Verification Query (Optional)
# ================================
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM fact_financials"))
        count = result.scalar()
        print(f"📊 Total records now in fact_financials: {count}")
except Exception as e:
    print("⚠️ Could not verify record count:", e)