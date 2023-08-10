import streamlit as st
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alohomora",
    database="railway"
)
cur = mydb.cursor()


def get_stations():
    cur.execute(
        "Select StationName from station"
    )
    data = cur.fetchall()
    return data


def p1():
    cur.execute(
        "SELECT midnight.tno,train.tname,midnight.stationcode,station.stationname from midnight INNER JOIN train ON midnight.tno=train.tno INNER JOIN station on midnight.Stationcode=station.Stationcode")
    data = cur.fetchall()
    df = pd.DataFrame(data, columns=["Train number",
                      "Train Name", "Station Code", "Station Name"])
    st.dataframe(df)


def p2():
    cur.execute("SELECT min(Halt),max(Halt),avg(Halt) from halts")
    data = cur.fetchone()
    df = pd.DataFrame([data], columns=["Minimum", "Maximum", "Average"])
    st.dataframe(df)


def p3():
    menu = [i[0] for i in get_stations()]
    option1 = st.selectbox("From", menu)
    option2 = st.selectbox("To", menu)
    cur.execute(
        "SELECT count(*) from stops s1,stops s2,station s3,station s4 WHERE s1.tno=s2.tno and s1.stationcode=s3.stationcode and s3.stationname=\"" +
        option1+"\"and s2.stationcode=s4.stationcode and s4.stationname=\"" +
        option2+"\"and s1.SEQ<s2.SEQ"
    )
    data = cur.fetchone()
    # data = cur.fetchall()
    #df = pd.DataFrame(data)
    # st.dataframe(df)
    string = "there are "+str(data[0])+" routes for your journey"
    st.markdown(string)
