import streamlit as st
import sqlite3 as sql
import pandas as pd
import os
db_name = "data/Expense"

if not os.path.exists("data"):
    os.makedir("data")

def Clear():
    st.session_state.nam=""
    st.session_state.fed=""
connection = sql.connect(db_name)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user_feedback(name TEXT,feedback TEXT,rating NUMBER);")
connection.commit()

name = st.text_input("Enter your name",key="nam")
feedback = st.text_input("Please provide your feedback",key="fed")
rating = st.slider("Please provide a rating on a scale of 1 - 5",min_value=1,max_value=5,step=1)

emoji_holder=st.empty()
if rating==1:
    emoji_holder.header(":weary:"+" We will definitely improve")
if rating==2:
    emoji_holder.header(":disappointed_relieved:"+" We will definitely improve your experience")
if rating==3:
    emoji_holder.header(":persevere:"+" Thanks !!")
if rating==4:
    emoji_holder.header(":smiley_cat:"+" Oh you are loving it!!!")
if rating==5:
    emoji_holder.header(":heart_eyes_cat:"+" Thank you so much for your love")

col1,col2 = st.columns(2)
with col1:
    submit = st.button("Submit :smile:")
with col2:
    clear = st.button("Clear :scissors:",on_click=Clear)

if submit:
    cursor.execute(f"INSERT INTO user_feedback(name,feedback,rating) VALUES('{name}','{feedback}',{rating});")
    connection.commit()
    connection.close()
    st.success("Thank you for your valuable feedback.")

st.subheader("Past feedbacks")

connection = sql.connect(db_name)
cursor = connection.cursor()
cursor.execute("SELECT * FROM user_feedback;")
records = cursor.fetchall()

dataframe = pd.DataFrame(records,columns=["Name","Feedback","Rating"]).reset_index(drop=True)
st.dataframe(dataframe)
