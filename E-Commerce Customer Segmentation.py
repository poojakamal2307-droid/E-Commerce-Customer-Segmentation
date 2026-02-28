# -------------------------
# Import Libraries
# -------------------------
import pandas as pd
from sqlalchemy import create_engine

# -------------------------
# Database Connection
# -------------------------
engine = create_engine(
    "mysql+pymysql://root:Root%401234@localhost/E_Commerce"
)

# -------------------------
# Load Data
# -------------------------
data = pd.read_sql("SELECT * FROM orders", engine)

print("\nDataset\n", data)

# -------------------------
# Data Preparation
# -------------------------
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
data['TotalAmount'] = data['Quantity'] * data['UnitPrice']

# -------------------------
# RFM Calculation
# -------------------------
today_date = data['InvoiceDate'].max()

RFM = data.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (today_date - x.max()).days,
    'InvoiceNo': 'count',
    'TotalAmount': 'sum'
})

RFM.columns = ['Recency','Frequency','Monetary']

print("\nRFM Table\n", RFM)

# -------------------------
# RFM Scoring
# -------------------------
RFM['R_score'] = pd.qcut(
    RFM['Recency'],
    4,
    labels=[4,3,2,1],
    duplicates='drop'
)

RFM['F_score'] = pd.qcut(
    RFM['Frequency'].rank(method='first'),
    4,
    labels=[1,2,3,4],
    duplicates='drop'
)

RFM['M_score'] = pd.qcut(
    RFM['Monetary'],
    4,
    labels=[1,2,3,4],
    duplicates='drop'
)

# -------------------------
# Combine Score
# -------------------------
RFM['RFM_Score'] = (
    RFM['R_score'].astype(str) +
    RFM['F_score'].astype(str) +
    RFM['M_score'].astype(str)
)

# -------------------------
# Customer Segmentation
# -------------------------
def segment_customer(score):
    if score[0]=='4' and score[1]=='4':
        return "Best Customers"
    elif score[1]=='4':
        return "Loyal Customers"
    elif score[0]=='4':
        return "Recent Customers"
    else:
        return "At Risk Customers"

RFM['Segment'] = RFM['RFM_Score'].apply(segment_customer)

print("\nFinal Segmentation\n", RFM)

# -------------------------
# Save Result to SQL
# -------------------------
RFM.to_sql(
    name='customer_segmentation',
    con=engine,
    if_exists='replace'
)
