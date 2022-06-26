from secrets import choice
import streamlit as st
def main():

    st.title('Test Vision')
    menu = ['Home', 'Login', 'SignUp']
    choice = st.sidebar.selectbox('Menu', menu)


    if choice == 'Home':
        st.subheader('Home')

    elif choice == 'Login':
        st.subheader('Login Section')
        username = st.sidebar.text_input('User Name')
        password = st.sidebar.text_input('Password', type='password')

        if password == '12345':
            if st.sidebar.checkbox('Login'):
                st.success('Logged in as {}'.format(username))
                task = st.selectbox('Task', ['Test checker', 'Statistics'])
                if task == 'Test checker':
                    st.subheader('Test checking')
                elif task == 'Statistics':
                    st.subheader('Informations')
        else:
            st.warning("Incorrect Username or Password")


    elif choice == 'SignUp':
        st.subheader('Create New Account')
        new_user = st.text_input('Username')
        new_password = st.text_input('Password', type='password')

        if st.button('SignUp'):
            st.success('You have successfully created an account')
            st.info('Go to login menu to login')

if __name__ == '__main__':
    main()