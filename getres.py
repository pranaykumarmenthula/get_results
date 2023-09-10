import streamlit as st
import pandas as pd


imdata = ['sem4aiml.xlsx','sem4ce.xlsx','sem4cse.xlsx','sem4ds.xlsx' ,
          'sem4ece.xlsx' ,'sem4eee.xlsx' ,'sem4it.xlsx' ,'sem4mech.xlsx']

idata=[]
ihs=[]

for i in range(len(imdata)):
    def load_data():
        df = pd.read_excel( imdata[i] , engine='openpyxl')
        return df

    data = load_data()
    hs = data.columns
    idata.append(data)
    ihs.append(hs)




data=[x for x in idata]
headings_sheet=[x for x in ihs]


branches = [ "CSE(AIML)",
            "Civil Engineering" ,"Computer Science Engineering",
            "CSE(DS)" ,"Electronics and Communication Engineering" , 
            "EEE","Information Technology" , "Mechanical Engineering"]
semesters = ["1st Semester", "2nd Semester", "3rd Semester", "4th Semester", "5th Semester", "6th Semester", "7th Semester", "8th Semester"]
exam_types = ["CIE-I","CIE-II" , "Final Exam"]


st.title("Get Results")

selected_branch = st.selectbox("Select Branch", branches)

selected_semester = st.selectbox("Select Semester", semesters)

selected_exam_type = st.selectbox("Select Exam Type", exam_types)


roll_number = st.text_input("Enter Roll Number(In Uppercase!)")

res_d=[]



for i in range(len(data)):
    for y in range(len(semesters)):
        if selected_semester == semesters[y]:
            for j in range(len(branches)):
                if selected_branch == branches[j] :

                    filtered_data = data[j][((data[j]['Branch'] == selected_branch) & (data[j]['Exam Type'] == selected_exam_type) & (data[j]['Rollno'] == roll_number)) ]
 
                    if not filtered_data.empty:
                        res_d.append(filtered_data[[str(k) for k in headings_sheet[j]]])
                        break
    


if (len(res_d)>0):
    st.write("Student Marks for Selected Branch, Semester, and Roll Number:")
    st.write(res_d[0])
else:
    st.write("No data found for the selected options.")

        
        


st.write(f"You selected: Branch - {selected_branch}, Semester - {selected_semester}, Exam Type - {selected_exam_type}")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
