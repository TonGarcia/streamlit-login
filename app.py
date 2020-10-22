import time
import numpy as np
import pandas as pd
import SessionState
import streamlit as st
from streamlit.server.server import Server, SessionInfo
import streamlit.components.v1 as components


def is_empty(obj):
    for key in dir(obj):
        if '_' == key[0]:
            continue
        else:
            val = getattr(obj, key)
            if len(val) == 0:
                return True
    return False


def landing_page():
    st.subheader('Landing Page')


def main():
    """Simple LogIn App"""
    st.title("Simple Login App")
    session_state = SessionState.get(insure='', email='', pwd='')
    empty_session_state = is_empty(session_state)

    if empty_session_state:
        menu = ["Home", "LogIn"]
    else:
        menu = ["Home", "DataApp"]
    choice = st.sidebar.selectbox("Páginas", menu)

    if is_empty(session_state):
        if choice == "Home":
            ####################################
            #           HOME PAGE              #
            ####################################
            landing_page()
            # /LANDING PAGE
        elif choice == "LogIn":
            ####################################
            #           LOGIN PAGE             #
            ####################################
            subheader = st.subheader('Já possui conta? Faça seu LogIn')

            insure = st.text_input("Corretora")
            email = st.text_input("Email")
            password = st.text_input("Senha", type='password')

            if st.button("LogIn"):
                if((insure == 'Blue' and email == 'blue@blueai.com' and password == '123123') or
                        (insure == "Rede D'or" and email == 'admin@rededor.com.br' and password == '123123') or
                        (insure == "Amil" and email == 'admin@amil.com.br' and password == '123123')):
                    session_state.insure = insure
                    session_state.email = email
                    session_state.pwd = password
                else:
                    st.error('LogIn e/ou Senha inválidos')

            # /LOGIN PAGE
        elif choice == "SignUp":
            ####################################
            #          REGISTER PAGE           #
            ####################################
            st.subheader('Ainda não possui conta? Registre-se aqui')
            # /SIGNUP PAGE

            # name = st.text_input("Nome")
            # insure = st.text_input("Corretora")
            # email = st.text_input("Email")
            # pwd = st.text_input("Senha", type='password')
            #
            # if st.button("Registrar-me"):
            #     # session_state.user_name
            #     session_state.user_name = name
            #     session_state.insure = insure
            #     session_state.email = email
            #     session_state.pwd = pwd
    else:
        if choice == "Home":
            ####################################
            #           HOME PAGE              #
            ####################################
            landing_page()
            # /LANDING PAGE
        elif choice == "DataApp":
            ####################################
            #           DATA PAGE              #
            ####################################
            st.subheader('DataApp')


if __name__ == '__main__':
    main()
