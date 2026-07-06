import streamlit as st
import pandas as pd

# Title
st.title("Student Management System")

# Student Data
data = {
    "Student ID": [1, 2, 3, 4, 5],
    "Name": ["Arun", "Meena", "Kavin", "Nisha", "Vijay"],
    "Department": ["CSE", "ECE", "IT", "EEE", "CSE"],
    "Marks": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)

# Display Data
st.subheader("Student Records")
st.dataframe(df)

# Search Student
st.subheader("Search Student")

student_id = st.number_input(
    "Enter Student ID",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Search"):
    result = df[df["Student ID"] == student_id]

    if not result.empty:
        st.success("Student Found")
        st.dataframe(result)
    else:
        st.error("Student Not Found")

# Statistics
st.subheader("Marks Analysis")

st.write("Average Marks:", round(df["Marks"].mean(), 2))
st.write("Highest Marks:", df["Marks"].max())
st.write("Lowest Marks:", df["Marks"].min())

# Chart
st.subheader("Student Marks Chart")
chart_data = df.set_index("Name")["Marks"]
st.bar_chart(chart_data)

# Department Filter
st.subheader("Department Filter")

dept = st.selectbox(
    "Select Department",
    df["Department"].unique()
)

filtered = df[df["Department"] == dept]
st.dataframe(filtered)