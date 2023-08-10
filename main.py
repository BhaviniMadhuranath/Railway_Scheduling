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
menu = ["Main Menu", "Problem 1", "Problem 2", "Problem 3"]
option = st.sidebar.selectbox("Menu", menu)
if option == "Main Menu":
    st.markdown(
        " ## Please choose the queries for each problem statement in the menu")
if option == "Problem 1":
    st.subheader(
        "Problem 1 - Display all trains that arrive at their destination at Midnight")
    problems.p1()
    st.markdown(
        "Here, all the trains with current station matching their destination station and arrival time midnight are displayed")

if option == "Problem 2":
    st.subheader(
        "Problem 2 - Find the minimum, maximum and average halts for all trains (This is given in minutes)")
    problems.p2()
    st.markdown("Here, the halt times of departing and arriving trains are given a default value of 2 hours to prevent any skew in the data")
if option == "Problem 3":
    st.subheader(
        "Problem 3 - Display the number of trains for a given source and destination")
    problems.p3()
    st.markdown(
        "Here, the table is self joined to find the source and destination pairs where they also match sequentially")
