import streamlit as st
import base64  # Add this import statement

st.set_page_config(
    layout='centered',
    initial_sidebar_state='expanded',
    page_title='😊02_About Me',
    page_icon='📊'
)

st.write(f"""# __Hello 👋 I'm__ </br>Ahamd Muhammad 𓂀</br>""", unsafe_allow_html=True)


st.write(f"""## Who am I?
**Data analyst and python developer** based in **Egypt 𓂀**.""", unsafe_allow_html=True)
st.write(
    """ 
        ## Background 🎓
        I have a background in EEC enginering and have been volunteered in business based activities for two years. My expertise includes fundraising, coding, and machine learning.
        
        ## Interests 🌟
        I am passionate about Python, Statistics, design and cutting edge AI technologies, and I enjoy composing metal music in my free time 🤘.
    """
)


st.write("""        ## What I Do 💼
        Currently, I am building data analysis templates and apps like AssociaGraph. I'm dedicated to make data analysis acccessable for all people, aiming to help all small, medium businesses to grow.
        
        ## Connect with Me 📫
        Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/ahmadmuhammadgd/), or drop me an [Email](ahmadmuhammadgd@gmail.com). I'm always open to collaboration and interesting conversations.
        
        Thanks for stopping by! 🚀""")