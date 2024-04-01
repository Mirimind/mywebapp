from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#First step:
st.set_page_config(page_title= 'Uncovering Data with Miri', page_icon=':tada:', layout='wide')

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()} </style>", unsafe_allow_html = True)

local_css("Style/style.css")

#---Load Assets---
lottie_renewables = load_lottieurl('https://assets7.lottiefiles.com/private_files/lf30_kcwpiswk.json')
img_zelt = Image.open('images/20220828_073028.png')

#---Header Section ---
with st.container():
    
    st.subheader('Hi, I am Miriam :wave:')
    st.title("I am a Mexican Renewable Energy Engineer & Data Analyst living in Germany")
    st.write ('I am passionate about finding trends and answers from data, and I like learning languages and dancing')
    st.write('[My Linkdin >](https://www.linkedin.com/in/miriam-godinez-879900101/)')
    st.write('[My GitHub >](https://www.linkedin.com/in/miriam-g-879900101/)')
    
# ---What I do---
with st.container():
    st.write ('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What I do')
        st.write('##')
        st.write(
            """
            I create content for people who:
                - are starting in the world of data and programming to learn with me
                - want to learn German
                - want to know how life in Germany is and how to get the best of being an expart in Germany
                - want to learn Spanish and know more about Mexican culture
    
                
                
                If this sounds interesting to you follow me on:"""
        )
        st.write ('My Instagram( https://hyperfarm.eu/)')
        st.write ('Additionally I write the highlights of the books I find most interesting for my life and you can find them here:')
    with right_column:
        st_lottie(lottie_renewables, height=300, key='renewables')
        
        
#---Projects---

with st.container():
    st.write('---')
    st.header('My Projects')
    st.write('##')
    image_column, text_column= st.columns((1,2))
    with image_column:
         st.image(img_zelt)
    with text_column:
         st.subheader('Resources to learn about python basics')
         st.write(
             '''This is a compedium of resources that have helped me so far
             '''
         )
         st.markdown('[Watch Video to learn how to do this webpage...](https://www.youtube.com/watch?v=VqgUkExPvLY)')
              
#---Contact---
with st.container():
    st.write('---')
    st.header('Get in touch with me!')
    st.write('##')
    
    # Documentation: https://formsubmit.co/ !!! Change email address
    
    contact_form = """
    <form action="https://formsubmit.co/miirimaiirim@gmail.com" 
    method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea> 
         <button type="submit">Send</button>
     </form> 
     """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()





              