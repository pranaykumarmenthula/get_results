import streamlit as st
import pandas as pd
import re
from streamlit_option_menu import option_menu
import requests
from bs4 import BeautifulSoup
import json
import plotly.express as px
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import GeckoDriverManager
import time


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
            exam_types = ["CIE-I","CIE-II"]


            st.title("Get Results")
            st.subheader("CIE Marks")

            selected_branch = st.selectbox("Select Branch", branches)
            selected_semester = st.selectbox("Select Semester", semesters)
            selected_exam_type = st.selectbox("Select Exam Type", exam_types)
            roll_number = st.text_input("Enter Roll Number")

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
            st.subheader("CGPA")
            try:
                        branches = [ "Computer Science Engineering","CSE(AIML)","CSE(DS)" ,"CS" ,"CSIT" ,
                "Civil Engineering" ,"EEE","Mechanical Engineering" ,
                "Electronics and Communication Engineering" , 
                "Information Technology" , "AERO" , "MBA"]
                        batch = ["2023" , "2022" , "2021" , "2020" , "2019" , "2018" , "2017" , "2016"] 

                        selected_batch = st.selectbox("Select Batch", batch)
                        selected_branch = st.selectbox("Select Branch", branches)
                        search_key = st.text_input("Enter Name")

                        if selected_branch == "Civil Engineering":
                                    dept_num = 1
                                    dept_name = "Civil Engineering"
                        if selected_branch == "EEE":
                                    dept_num = 2
                                    dept_name = "EEE"
                        if selected_branch == "Mechanical Engineering":
                                    dept_num = 3
                                    dept_name = "Mechanical Engineering"
                        if selected_branch == "Electronics and Communication Engineering":
                                    dept_num = 4
                                    dept_name = "Electronics and Communication Engineering"
                        if selected_branch == "Computer Science Engineering":
                                    dept_num = 5
                                    dept_name = "Computer Science Engineering"
                        if selected_branch == "Information Technology":
                                    dept_num = 6
                                    dept_name = "Information Technology"
                        if selected_branch == "AERO":
                                    dept_num = 7
                                    dept_name ="AERO"
                        if selected_branch == "MBA":
                                    dept_num = 9
                                    dept_name ="MBA"
                        if selected_branch == "CSE(AIML)":
                                    dept_num = 34
                                    dept_name ="CSE(AIML)"
                        if selected_branch == "CSE(DS)":
                                    dept_num = 35
                                    dept_name ="CSE(DS)"
                        if selected_branch == "CS":
                                    dept_num = 36
                                    dept_name ="CS"
                        if selected_branch == "CSIT":
                                    dept_num = 37
                                    dept_name ="CSIT"

                        url = "https://samvidha.iare.ac.in/pages/admin/reports/ajax/cal_cgpa.php"

                        payload = "batch="+str(selected_batch)+"&dept="+str(dept_num)+"&sem=4&action=get_cgp"
                        headers = {
                                    "authority": "samvidha.iare.ac.in",
                                    "accept": "application/json, text/javascript, */*; q=0.01",
                                    "accept-language": "en-US,en;q=0.7",
                                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                                    "cookie": "PHPSESSID=r1v167a3p2af2nengeu5j3s0dc",
                                    "origin": "https://samvidha.iare.ac.in",
                                    "referer": "https://samvidha.iare.ac.in/home?action=cgp_sem_HOD",
                                    "sec-ch-ua": "^\^Chromium^^;v=^\^118^^, ^\^Brave^^;v=^\^118^^, ^\^Not=A?Brand^^;v=^\^99^^",
                                    "sec-ch-ua-mobile": "?0",
                                    "sec-ch-ua-platform": "^\^Windows^^",
                                    "sec-fetch-dest": "empty",
                                    "sec-fetch-mode": "cors",
                                    "sec-fetch-site": "same-origin",
                                    "sec-gpc": "1",
                                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
                                    "x-requested-with": "XMLHttpRequest"
                        }

                        response = requests.request("POST", url, data=payload, headers=headers)


                        data_dict = json.loads(response.text)
                        df = pd.DataFrame(data_dict['data'])
                        new_cols = ['S.NO.' , 'Roll No.' , 'Name' , 'Department' , 'I sem' , 'II sem' ,'III sem' , 'IV sem' , 'V sem' , 'VI sem' , 'VII sem' , 'VIII sem' , 'CGPA']
                        df.columns = new_cols
                        df['Department'] = str(dept_name)
                        result = df[df['Name'].str.contains(search_key.upper()) | df['Roll No.'].str.contains(search_key.upper())]
                        plot_df = result
                        if search_key:
                                    st.write(result)
                                    if st.button("Plot"):
                                                l= result.iloc[0].to_list()
                                                l_f = l[4:12]
                                                lf=[]
                                                for i in range(len(l_f)):
                                                            if l_f[i] is not None:
                                                                        lf.append(l_f[i])
                                                l_int = [float(element) for element in lf]
                                                l_len=[]
                                                for i in range(len(l_int)):
                                                            l_len.append(i+1)
                                                data = pd.DataFrame({'SGPA': l_int, 'Semester': l_len})
                                                fig = px.bar(data, x='Semester', y='SGPA', text='SGPA', title='SGPA Bar Chart')
                                                fig.update_traces(texttemplate='%{text}', textposition='outside')
                                                st.plotly_chart(fig)
                                                st.write("CGPA is : :blue[{}]".format(l[12]))
            except Exception as e:
                        st.error(f"An error occurred")
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
                    for i in range(0, len(td_data), t):
                        chunk = td_data[i:i + t]
                        if chunk[0] == " Laboratory Marks (Practical) " :
                            break
                        else:
                            chunks.append(chunk)
    
                    df = pd.DataFrame(chunks, columns=titles_t)
                    wait_message.text("")
                    st.write("Current Semester CIE Marks")
                    st.write(df , index=False)
                else:
                    st.write("Failed to access the page.")
        except Exception as e:
            st.error("Please enter correct details before submitting.")
        


if selected_opt == "Get Attendance" :
            st.title("Get Attendance")
            rollno = st.text_input("Enter Roll Number")
            if st.button("Submit"):
                        try:
                                    wait_message = st.empty()
                                    wait_message.text("Please wait...")
                                    chrome_options = Options()
                                    chrome_options.add_argument("--headless=new")
                                    chrome_options.add_argument('--disable-gpu')
                                    chrome_options.add_argument("--no-sandbox")
                                    chrome_options.add_argument("--disable-dev-shm-usage")
                                    service = Service(GeckoDriverManager().install())
                                    driver = webdriver.Chrome(options=chrome_options , service=service)
                                    driver.get('https://samvidha.iare.ac.in/home')
                                    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'txt_uname')))
                                    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'txt_pwd')))
                                    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Sign In")]')))
                                    username_input.send_keys('aimlhod')
                                    password_input.send_keys('aiml@95')
                                    login_button.click()
                                    time.sleep(4)
                                    driver.get('https://samvidha.iare.ac.in/home?action=stud_att_hod')
                                    search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'rollno')))
                                    search_bar.send_keys(rollno)
                                    response = search_bar.send_keys(Keys.RETURN)
                                    time.sleep(4)
                                    page_source = driver.page_source
                                    soup = BeautifulSoup(page_source, 'html.parser')
                                    table = soup.find('table', class_='table table-striped table-bordered table-hover table-head-fixed responsive ')

                                    thead = soup.find('thead')
                                    headings = [th.text for th in thead.find_all('th')]

                                    tbod = soup.find_all('tbody')
                                    tbody=tbod[2]
                                    table_data = []
                                    rows=tbody.find_all('tr')
                                    for row in rows:
                                                row_data = [td.text for td in row.find_all('td')]
                                                table_data.append(row_data)
 
                                    df = pd.DataFrame(table_data, columns=headings)
            

                                    lst_cond = [x for x in df['Conducted']]
                                    for i in range(len(lst_cond)):
                                                if lst_cond[i]=="":
                                                            lst_cond[i]='0'
                                                else:
                                                            pass
                                    lst_att = [x for x in df['Attended']]
                                    for i in range(len(lst_cond)):
                                                if lst_att[i]=="":
                                                            lst_att[i]='0'
                                                else:
                                                            pass
            
                                    lst_final = []
                                    att_numbers = [int(num) for num in lst_att]
                                    cond_numbers = [int(num) for num in lst_cond]
                                    for i in range(len(lst_att)):
                                                x = cond_numbers[i]
                                                y= att_numbers[i]
                                                if y<(x*0.75):
                                                            z=(x-y)*4
                                                            fin = z - x
                                                            lst_final.append(fin)
                                                else:
                                                            lst_final.append(0)
            
                                    lst_sub = [x for x in df['Course Name']]
                                    try:
                                                for i in range(len(lst_final)):
                                                            if lst_final[i] != 0:
                                                                        st.write(lst_sub[i] ,": :red[{} Classes]".format(int(lst_final[i])) )
                                                            else:
                                                                        pass
                                                wait_message.text("")
                                                st.write(df)
                                    except Exception as e:
                                                st.success(":green[Satisfactory]")
            

                        except Exception as e:
                                    st.error(e)    


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
