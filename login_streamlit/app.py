from secrets import choice
import streamlit as st
def main():

    st.title('Test Vision')
    menu = ['Home', 'Login', 'SignUp']
    choice = st.sidebar.selectbox('Menu')


    if choice == 'Home':
        st.subheader('Home')

    elif choice == 'Login':
        st.subheader('Login Section')

    elif choice == 'SignUp':
        st.subheader('Create New Account')
if __name__ == '__main__':
    main()