import streamlit as st
import pandas as pd
import sqlite3 as sql
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

db_path = "data/Expense"

def execution():

    date_from = st.date_input("From Date :date:")
    date_to = st.date_input("To Date :date:")

    st.write("Amount :money_with_wings:")
    amount_min = st.slider("Minimum value",min_value=0,max_value=20000,value=0,step=10)
    amount_max = st.slider("Maximum value",min_value=0,max_value=20000,value=20000,step=10)
    category = st.multiselect("Categories :card_index_dividers:",["Housing","Utilities","Transportation","Food","Healthcare","Insurance","Debt Payments","Entertainment","Personal Care","Education","Savings","Taxes","Miscellaneous"],placeholder="You can choose multiple option(s)")

    connection = sql.connect(db_path)
    cursor = connection.cursor()

    if category!=[]:
        if len(category)==1:
            category=tuple(category)
            category=str(category).replace(',','')
        else:
            category=tuple(category)
        print(f"SELECT * FROM expenses WHERE date>='{date_from}' AND date<='{date_to}' AND amount>={amount_min} AND amount<={amount_max} AND category IN {category};")
        cursor.execute(f"SELECT * FROM expenses WHERE date>='{date_from}' AND date<='{date_to}' AND amount>={amount_min} AND amount<={amount_max} AND category IN {category};")
    else:
        cursor.execute(f"SELECT * FROM expenses WHERE date>='{date_from}' AND date<='{date_to}' AND amount>={amount_min} AND amount<={amount_max};")

    records=cursor.fetchall()

    dataframe = pd.DataFrame(records,columns=["Date","Category","Description","Amount"])

    st.title("Expenses :receipt:")
    st.dataframe(dataframe[["Category","Description","Amount"]])

    st.title("Amount :money_with_wings:")
    st.line_chart(dataframe["Amount"])

    st.title("Categories :card_index_dividers:")

    category_dataframe = dataframe.groupby('Category')['Amount'].sum()
    plt.pie(category_dataframe, labels=category_dataframe.index, autopct='%.2f',textprops={'fontsize': 8.5})
    st.pyplot()

try:
    execution()
except:
    st.header("Please add some expenses to view.")
