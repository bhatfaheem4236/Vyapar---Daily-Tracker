import streamlit as st
import csv 
import os
import pandas as pd

st.set_page_config(page_title ="Vyapar Daily Tracker", layout ='centered')
st.title("Vyapar Daily Tracker")

SALES_FILE = "sales.csv"
EXPENSES_FILE = "expenses.csv"

def setup_files():
    if not os.path.exists(SALES_FILE):
        with open (SALES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Item", "Quantity", "Price", "Total Revenue", "Total profit"])
            
    if not os.path.exists(EXPENSES_FILE):
        with open (EXPENSES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amout", "Note"])
            
st.sidebar.title("Menu")
page = st.sidebar.radio("Select Option", 
                        ["Add Sale", "Add Expenses", "Daily Summary", "Show Graph"]
)
            
if page == "Add Sale":
    st.header("➕ Add Sale")
    
    date = st.date_input("Date")
    item = st.text_input("Item Name")
    quantity = st.number_input("Quantity", min_value=1, step=1)
    cost_price = st.number_input("Cost Price per Item(₹)", min_value=0.0, step=0.5)
    selling_price = st.number_input("Selling Price per Item(₹)", min_value=0.0, step=0.5)
    
    if st.button("Save Sale"):
        total_revenue = quantity * selling_price
        total_cost = quantity * cost_price
        total_Profit = total_revenue - total_cost
    
        with open (SALES_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date, item, quantity, selling_price, cost_price, total_revenue, total_Profit])
            
        st.success(f"✅ Sale Saved! Revenue: ₹{total_revenue:.2f}")
        
        col1, col2,col3 = st.columns(3)
        col1.metric("Revenue", f"₹{total_revenue:.2f}")
        col2.metric("Cost", f"₹{total_cost:.2f}")
        col3.metric("Profit", f"₹{total_Profit:.2f}")
        
elif page == "Add Expenses":
    st.header("Add Expenses")
        
    date = st.date_input("Date")
    category = st.selectbox("Category",[
        "Rent", "Electricity", "Transport", 
        "Raw Material", "Salary", "Other"])
    amount = st.number_input("Amount(₹)", min_value=0.0, step =10.0)
    note = st.text_input("Note(Optional)")
        
    if st.button("Save Expenses"):
        with open (EXPENSES_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date, category, amount, note])
                
            st.success(f"✅ Expense Saved ! ₹{amount:.2f} added under {category}")
            
elif page == "Daily Summary":
    st.header("Daily Summary")
    
    selected_date = st.date_input("Select Date")
    
    if os.path.exists(SALES_FILE):
        sales_df = pd.read_csv(SALES_FILE, names=["Date", "Items", "Quantity", "Selling Price", "Cost Price", "Revenue", "Profit"])
        sales_df = sales_df[sales_df["Date"]== str(selected_date)]
    else:
        sales_df = pd.DataFrame()
    if os.path.exists(EXPENSES_FILE):
        exp_df = pd.read_csv(EXPENSES_FILE, names=["Date", "Category", "Amount", "Note"])
        exp_df = exp_df[exp_df["Date"]== str(selected_date)]
    else:
        exp_df = pd.DataFrame()
        
    total_revenue = sales_df["Revenue"].astype(float).sum()if not sales_df.empty else 0
    total_profit = sales_df["Profit"].astype(float).sum()if not sales_df.empty else 0
    total_expense = exp_df["Amount"].astype(float).sum()if not exp_df.empty else 0
    net = total_profit - total_expense
    
    col1, col2, col3 ,col4 = st.columns(4)
    col1.metric("Revenue", f"₹{total_revenue:.2f}")
    col2.metric("Profit", f"₹{total_profit:.2f}")
    col3.metric("Expense", f"₹{total_expense:.2f}")
    col4.metric("Net", f"{net:.2f}")
        
    st.subheader("Sales")
    st.dataframe(sales_df if not sales_df.empty else pd.DataFrame({"Message": ["No Sales on this date"]}))
    
    st.subheader("Expenses")
    st.dataframe(exp_df if not exp_df.empty else pd.DataFrame({"Message": ["No Expense on this date"]}) )    
        
elif page == "Show Graph":
    st.header("Show Graph")
    
    if os.path.exists(SALES_FILE):
        sales_df = pd.read_csv(SALES_FILE, names=["Date", "Items", "Quantity", "Selling Price", "Cost Price", "Revenue", "Profit"])
        sales_df["Revenue"] = sales_df["Revenue"].astype(float)
        sales_df["Profit"] = sales_df["Profit"].astype(float)
    else:
        sales_df = pd.DataFrame()
    
    if os.path.exists(EXPENSES_FILE):
        exp_df = pd.read_csv(EXPENSES_FILE, names=["Date", "Category", "Amount", "Note"])
        exp_df["Amount"] = exp_df["Amount"].astype(float)
        
    else:
        exp_df = pd.DataFrame()
        
    if not sales_df.empty:
        st.subheader("Daily Revenue")
        revenue_chart = sales_df.groupby("Date")["Revenue"].sum()
        st.bar_chart(revenue_chart)
        
        st.subheader("Daily Profit")
        profit_chart = sales_df.groupby("Date")["Profit"].sum()
        st.line_chart(profit_chart)      
    
    if not exp_df.empty:
        st.subheader("Daily Expenses by Category")
        exp_chart = exp_df.groupby("Category")["Amount"].sum()
        st.bar_chart(exp_chart)
        
    if sales_df.empty and exp_df.empty:
        st.info("No data available to show graphs. Please add sales or expenses first.")
        

    
