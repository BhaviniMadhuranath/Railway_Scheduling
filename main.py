import streamlit as st
import mysql.connector
import problems
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alohomora"
)
cur = mydb.cursor()
cur.execute("USE RAILWAY")

st.title("RAILWAY SYSTEM")
st.markdown(" ##Please choose the queries for each problem statement in the menu")
menu = ["Problem 1", "Problem 2", "Problem 3"]
option = st.sidebar.selectbox("Menu", menu)
if option == "Problem 1":
    st.subheader(
        "Problem 1 - Display all trains that arrive at their destination at Midnight")
    problems.p1()
    st.markdown("put 00 explanation here")

if option == "Problem 2":
    st.subheader(
        "Problem 2 - Find the minimum, maximum and average halts for all trains")
    problems.p1()
    st.markdown("put dept/arr handling explanation here")
if option == "Problem 3":
    st.subheader(
        "Problem 3 - Display the number of trains for a given source and destination")
    problems.p1()
    st.markdown("put logic explanation here")
