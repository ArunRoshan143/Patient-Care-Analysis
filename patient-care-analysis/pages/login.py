import streamlit as st

st.set_page_config(page_title="Login" ,page_icon='https://cdn-icons-png.flaticon.com/64/2250/2250207.png')

from db_operations import add_user
from session import set_session
import time
from streamlit_lottie import st_lottie

import requests

def login_page():
    st.title("Login")
    st.markdown("""\
                <style>
                .main{
                background-image:url("./app/static/healthcare.png");
                background-size:cover   ;
                background-repeat:no-repeat;
                }
                <\style>
                """,unsafe_allow_html=True)
    with st.container( height=280):
        user_email = st.text_input("Email")
        password=st.text_input("Password",type='password')
        res=st.button("Login")
    if res:
        if user_email:
            with st.status(expanded=True,label='') as status:
                opt=add_user(user_email,password)
                if opt=='new': 
                    status.update(state='complete',label='Signing up',expanded=False)
                    st.success("Account created successfully")
                  
                    st.session_state.logged_in = True
                    st.session_state.user_email = user_email
                    
                    set_session()
                    st.switch_page('pages/loading.py')
                elif opt:
                    status.update(state='complete',label='Signing in',expanded=False)
                    st.success("Successfully signed in")
                    st.session_state.logged_in = True
                    st.session_state.user_email = user_email
                    set_session()
                    st.switch_page('pages/loading.py')
                    
                else:
                    st.error("Invalid email or password")
                
        else:

            st.error("Invalid email or password")


login_page()
