import streamlit as st
import pandas as pd
import re
from streamlit_option_menu import option_menu
import requests
from bs4 import BeautifulSoup

st.set_page_config(
            page_title="GetRes Iare",
            page_icon="https://img.icons8.com/external-nawicon-mixed-nawicon/64/external-Hacker-internet-security-nawicon-mixed-nawicon.png",
            layout="centered"
)
ad_code1 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1009909662863685"
     crossorigin="anonymous"></script>
</head>
<body>
</body>
</html>

"""
st.markdown(ad_code1, unsafe_allow_html=True)

st.title("IARE Student Tools")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

custom_css = """
<style>
  .block-container{
        padding : 0px;
    }
    .st-emotion-cache-10trblm.e1nzilvr1{
        display : flex;
        justify-content : center;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

custom_js = """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1009909662863685"
     crossorigin="anonymous">
     </script>
"""
st.markdown(custom_js, unsafe_allow_html=True)

selected_opt = option_menu(
    menu_title=None,
    options=["GetRes Anonymous" , "GetRes Credentials" , "Get Attendance"],
    icons=["person-fill-lock" , "person-check-fill" , "file-bar-graph-fill"] ,
    menu_icon="cast" ,
    default_index=0 ,
    orientation="horizontal"
)

if selected_opt == "GetRes Anonymous" :
            imdata = ['sem4cse.xlsx','sem4aiml.xlsx','sem4ds.xlsx' ,'sem4cs.xlsx','sem4csit.xlsx' ,'sem4ce.xlsx',
          'sem4eee.xlsx' ,'sem4mech.xlsx' ,'sem4ece.xlsx' ,'sem4it.xlsx' ,'sem4aero.xlsx']

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


            branches = [ "Computer Science Engineering","CSE(AIML)","CSE(DS)" ,"CSE(CS)" ,"CSIT" ,
                        "Civil Engineering" ,"EEE","Mechanical Engineering" ,
                        "Electronics and Communication Engineering" , 
                        "Information Technology" , "AERO"]
            semesters = ["1st Semester", "2nd Semester", "3rd Semester", "4th Semester", "5th Semester", "6th Semester", "7th Semester", "8th Semester"]
            exam_types = ["CIE-I","CIE-II" , "Final Exam"]


            st.title("Get Results")

            selected_branch = st.selectbox("Select Branch", branches)
            selected_semester = st.selectbox("Select Semester", semesters)
            selected_exam_type = st.selectbox("Select Exam Type", exam_types)
            roll_number = st.text_input("Enter Roll Number(In Uppercase!)")

            res_d=[]

            try:
                        for y in range(len(semesters)):
                                    if selected_semester == semesters[y]:
                                                for i in range(len(data)):
                                                            for j in range(len(branches)):
                                                                        if (selected_branch == branches[j] and selected_semester == semesters[y]):
                                                                                    filtered_data = data[j][((data[j]['Branch'] == selected_branch) & (data[j]['Exam Type'] == selected_exam_type) & (data[j]['Rollno'] == roll_number.upper())) ]
                                                                                    if not filtered_data.empty:
                                                                                                res_d.append(filtered_data[[str(k) for k in headings_sheet[j]]])
                                                                                                break
    
                        if ((len(res_d)>0)):
                                    s1=str(selected_semester)
                                    s2=str(res_d[0])
                                    if re.search(s1, s2):
                                                st.write("Student Marks for Selected Branch, Semester, and Roll Number:")
                                                st.write(res_d[0])
                                    else:
                                                st.write("No data found for the selected options.")
                        else:
                                    st.write("No data found for the selected options.")
                        st.write(f"You selected: Branch - {selected_branch}, Semester - {selected_semester}, Exam Type - {selected_exam_type}")
                        st.caption('Currently works only for :blue[4th Semester] ')


            except Exception as e:
                    st.error(f"An error occurred : {str(e)}")
                    st.write("Working on Issues...")

if selected_opt == "GetRes Credentials" :
    st.title("GetRes Credentials")
    username = st.text_input("Enter Username:" )
    password = st.text_input("Enter Password:", type="password")
    if st.button("Submit"):
        try:
            if username!=None and password!=None:
                wait_message = st.empty()
                wait_message.text("Please wait...")
                session = requests.Session()
                login_url = 'https://samvidha.iare.ac.in/pages/login/checkUser.php'
                login_payload = {
                    'username': username,
                    'password': password
                }
                login_response = session.post(login_url, data=login_payload)
                target_url = 'https://samvidha.iare.ac.in/home?action=cie_marks_mba'

                page_response = session.get(target_url)
                if page_response.status_code == 200:
                    soup = BeautifulSoup(page_response.text, 'html.parser')

                    table = soup.find('table', class_='table table-bordered table-sm table-striped')

                    headers = table.find_all("th")
                    titles=[]
                    titles_t=[]
                    for i in headers:
                        title = i.text 
                        titles.append(title)
                    titles_t = titles[3:11]

                    t=len(titles_t)
                    data = table.find_all("td")
                    td_data = [tag.get_text() for tag in data]
                
                    chunks = []
                    for i in range(0, len(td_data), 8):
                        chunk = td_data[i:i + 8]
                        if chunk[0] == " Laboratory Marks (Practical) " :
                            break
                        else:
                            chunks.append(chunk)
    
                    df = pd.DataFrame(chunks, columns=titles_t)
                    wait_message.text("")
                    st.write(df , index=False)
                else:
                    st.write("Failed to access the page.")
        except Exception as e:
            st.error("Please enter correct details before submitting.")


if selected_opt == "Get Attendance" :
    st.title("Get Attendance")
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password")
    st.caption(' :blue[This feature will be available soon..] ')         


ad_code = """
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1009909662863685"
     crossorigin="anonymous"></script>
<!-- getres -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-1009909662863685"
     data-ad-slot="9448856519"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
"""
st.markdown(ad_code, unsafe_allow_html=True)
