import streamlit as st
import sqlite3 as sql
import pandas as pd
import time,os

db_name = "data/Expense"

if not os.path.exists("data"):
    os.makedirs("data")
values = ["Connecting to the table","Adding the records","Saving","Almost done","Done"]
c=1

date = st.date_input('Date :date:', pd.to_datetime('today'),key="da")

category = st.selectbox("Category :card_index_dividers:",(
    "Housing",
    "Utilities",
    "Transportation",
    "Food",
    "Healthcare",
    "Insurance",
    "Debt Payments",
    "Entertainment",
    "Personal Care",
    "Education",
    "Savings",
    "Taxes",
    "Miscellaneous"
),key="cat")

description=st.text_input('Description :flashlight:',key='desc')

amount=st.number_input('Amount :money_mouth_face:',key='am',min_value=0,step=1,max_value=2000000)

def clear():
    st.session_state.am=0
    st.session_state.desc=""

col1,col2 = st.columns(2)

with col1:
    add = st.button("Add Expense :money_with_wings:")
with col2:
    clear_button = st.button("Clear :scissors:",on_click=clear)


def insert(date,category,description,amount):
    global c
    connection = sql.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS expenses(date DATE,category TEXT,description TEXT,amount NUMBER);")
    if description!="" and amount>0:
        cursor.execute(f"INSERT INTO expenses(date,category,description,amount) VALUES('{date}','{category}','{description}','{amount}');")
        bar = st.progress(0,values[0])
        for i in range(25,101,25):
            bar.progress(i,values[c])
            time.sleep(0.5)
            c+=1
        bar.empty()
        st.balloons()
    else:
        st.error('Please provide a description and a valid amount value greater than zero.', icon="🚨")
    connection.commit()
    connection.close()

if add:
    insert(date,category,description,amount)


