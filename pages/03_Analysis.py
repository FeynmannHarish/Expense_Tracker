import streamlit as st
import pandas as pd
import os
import sqlite3 as sql
from wordcloud import WordCloud
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

db_name = "data/Expense"

if not os.path.exists("data"):
    os.makedirs("data")
def execution():
    connection = sql.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM expenses;")
    records = cursor.fetchall()

    dataframe = pd.DataFrame(records,columns=["date","category","description","amount"])

    max_amount = dataframe[dataframe["amount"]==dataframe["amount"].max()]
    min_amount = dataframe[dataframe["amount"]==dataframe["amount"].min()]


    st.subheader("You are spending the most here :cry:")
    st.dataframe(max_amount.reset_index(drop=True))
    st.subheader("You are spending the least here :blush:")
    st.dataframe(min_amount.reset_index(drop=True))

    mode_category = dataframe["category"].mode()
    st.subheader("The categories for which you are spending the most :cry:")

    st.dataframe(mode_category.reset_index(drop=True))

    st.subheader("The categories for which you are spending the least :blush:")
    st.dataframe(dataframe[dataframe['category'].value_counts().idxmin()==dataframe['category']]["category"].reset_index(drop=True))

    description_data = ' '.join(list(dataframe["description"].values))

    # Function to generate and display word cloud
    def generate_wordcloud(text):
        wordcloud = WordCloud(width=400, height=400, background_color='white',).generate(text)
        plt.figure(figsize=(5, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot()

    st.subheader("Description cloud :cloud:")
    generate_wordcloud(description_data)

try:
    execution()
except:
    st.header("Please add some expenses to analyse.")
