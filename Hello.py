from nbformat import write
from numpy import imag
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

col1, col2 = st.columns([3,1])
with st.container():
    with col1:
        with st.container():
            st.subheader("Hi,I'am Marwan Ghouma :wave:")
            st.title("Final-year computer science engineering student ")
            
    with col2:
        st.image("me.png")
        st.markdown('''[**LinkedIn**](https://www.linkedin.com/in/marwan-ghouma/) | [**Github**](https://github.com/Marwan-Ghouma) | [**CV**](https://drive.google.com/file/d/1PQDWacscXEkl5r_g-CEU3ug_hmpwm3aM/view?usp=sharing)'''  )

    st.write(
            "I'm passionate about solving problems and creating software."
            )
    st.write("During my academic career, I  gain good knowledge in different fields such as software development, Mathematics, Data Science, and Finance.")
col21,col22 = st.columns([1,2])
with st.container():
    with col21:
        st.header("Education :mortar_board:")
    with col22:
        st.write("")
        st.write("")
        st.subheader("ENSI : National School of Computer Science of Tunisia")
        with st.expander("Computer Science Engineer • class of 2020"):
             st.write("Cursus includes :")
             st.markdown('''
             * Algorithms and programming in C
             * **OOP in c++ and Java
             * Introduction to operating systems and Unix environment
             * Web and multimedia programming
             * Graph algorithms and optimization
             * software engineer fundamentals
             * Object Oriented Analysis and Design using  UML
             * Database design
             * Big Data
             * IA  and Machine learning 
             * [**Full cursus**](http://www.ensi-uma.tn/programmes-denseignement/)
              ''')

        st.subheader("IPEIS : National School of Computer Science of Tunisia")
        with st.expander("Preparatory cycle for engineering studies MP"):
            st.write("Cursus includes :")
            st.markdown('''
            * Algebra 
            * Analysis 
            * physics
            * chemistry
            * Mechanical  
            * Algorithms and Programming with Python
             ''')

col31,col32 = st.columns([1,2])
with st.container():
    with col31:
        st.header("Experience :briefcase: ")
    with col32:
        st.write("")
        st.write("")
        st.subheader("Software Engineer Intern ")
        st.write("Infraplus Tunis,Tunisia Jul 2022 - Aug 2022 · 2 mos")
        with  st.expander("Cryptocurrency analysis and prediction platform"):
            st.markdown(''' 
            * Development and implementation of a web platform that offers 
                necessary services for crypto traders, first of all the real-time display of 
                prices, market volume and trading history of each currency, guides for profitable
                investment, and a machine learning part for prediction of 
                future bitcoin prices.
            * **Tools**: Python,FastApi,React,Tensorflow,Keras .
            ''')
        st.subheader("Back End Developer")
        st.write("National school for computer science  Jan 2022 - Apr 2022 · 4 mos")
        with st.expander("Remote cheque deposit platform"):
            st.markdown('''
            * platform that facilitates the check deposit operation, while extracting check data using a
              deep learning model and sending the encrypted data to the banker.
            * **Tools**: Python,Tensorflow,Keras,Sprigboot,Flask,Angular.
            
             ''')
        
        st.subheader("Mobile Developer  Intern ")
        st.write("AggriBrand Manouba,Tunisia Jun 2021 - Jul 2021 · 2 mos ")
        with  st.expander("E-commerce mobile application"):
            st.markdown(''' 

                * E-commerce application dedicated to rural women
                    and agripreneurs to sell their products, allows them to place an order 
                    and pay for a product directly on a smartphone. Promoting competition,
                    moderation of prices and acceleration of transactions
                * **Tools**: Dart · Firebase · Flutter
            ''')

col41,col42 = st.columns([1,2])
with st.container():
    with col41:
        st.header("Skills :stars: ")
    with col42:
        st.write("")
        st.write("")
        with  st.expander("Web Development "):
            st.markdown('''
            * HTML/CSS,Javascript,TypeScript
            * Reactjs , NodeJs
            * Java , Sprigboot
            * Python , FastApi              
             ''')
        with  st.expander("Mobile Development"):
            st.markdown('''
            * Dart 
            * Flutter
            * Firebase 
            ''')

        with  st.expander("Database and BigData"):
            st.markdown(''' 
            * SQL, Pl/SQL
            * Mysql, MongoDb
            * Apache Hadoop, Spark
            ''')
        with  st.expander("Data science "):
            st.markdown('''
            * Python
            * Matplotlib, Seaborn
            * Pandas
            * scikit-learn
            * Tensorflow
            * Keras 
             ''')
        with  st.expander("Devops"):
            st.markdown(''' 
            * Git/Github
            * Linux
            * Docker
            * Kubernetes 
            ''')

