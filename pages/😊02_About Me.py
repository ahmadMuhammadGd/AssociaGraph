import streamlit as st

st.set_page_config(
    layout='centered',
    initial_sidebar_state='expanded',
    page_title='😊02_About Me',
    page_icon='📊'
)


st.markdown(
"""
 <style>
        body {
            font-family: 'Arial', sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }

        .content-container {
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .image-container {
            margin-right: 20px; /* Adjust the margin as needed */
        }

        img {
            max-width: 100%;
            height: auto;
        }

        .text-container {
            max-width: 400px; /* Adjust the max-width as needed */
        }
    </style>

    <div class="content-container">
        <div class="image-container">
            <img src="./about_me_imgs/me.jpg" alt="ME">
        </div>
        <div class="text-container">
            <p>HELLO 👋<br>
                I’m Ahmad Muhammad<br>
                Data Analyst and Python Developer<br>
                <a href="https://www.linkedin.com/in/your-linkedin-profile/" target="_blank">🔗LINKEDIN</a><br>
                AHMADMUHAMMADGD@GMAIL.COM
            </p>
        </div>
    </div>

""", unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)
col2.title("Hi there! 👋")
col2.image("./about_me_imgs/me.jpg", width=350)
st.title("I'm Ahmad Muhammad, a passionate data analysis and python developer based in Egypt.")


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