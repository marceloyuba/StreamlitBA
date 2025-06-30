

import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="Accidentes - Strategic Data Transform", page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")
with st.container():
    
    st.markdown('<style>h4{color: white;}</style>', unsafe_allow_html=True)    
    st.markdown('<style>h3 {color: white;}</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}</style>', unsafe_allow_html=True)
    st.markdown('<style>write {color: white;}</style>', unsafe_allow_html=True)

column_widths = [1, 1, 2]
with st.container():
    
    col1, col2, col3 = st.columns(column_widths)   
    with col1:
        st.image("scr/Logo_Buenos_Aires.png", width=550, use_container_width=True, output_format='auto')
        
    with col2:
        st.title("")
          
    with col3: 
        st.image("scr/SDTLogoC.png", width=1200, use_container_width=True, output_format='auto')

st.title("") 
st.title("") 

column_widths = [2, 1]
with st.container():
    col1, col2 = st.columns(column_widths)
    
    with col1:
        st.header("Informe estadistico de accidentes viales en la Ciudad de Buenos Aires")        
        st.markdown("""
                #### El Observatorio de Movilidad y Seguridad Vial (OMSV), centro de estudios que se encuentra bajo la órbita de la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires, nos solicita la elaboración de un proyecto de análisis de datos, con el fin de generar información que le permita a las autoridades locales tomar medidas para disminuir la cantidad de víctimas fatales de los siniestros viales. Para ello, nos disponibiliza un dataset sobre homicidios en siniestros viales acaecidos en la Ciudad de Buenos Aires durante el periodo 2016-2021. 
                """) 
        
    
    with col2:
        imagen = "scr/BA.png"  
        st.image(imagen, width=500, use_container_width=True, output_format='auto')
    

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)  

def main():    

    st.title("Dashboard de analisis de accidentes viales")
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
       <iframe title="DatasetMockup" width="1300" height="860" src="https://app.powerbi.com/view?r=eyJrIjoiM2NjNDA0YmItMmRhZC00ZDhlLWFmOWYtZTZiMWMxYWY3ODAzIiwidCI6ImUyYjc5Nzc5LTBhODgtNDMzMS05YjQyLTM4NGNkNzFjODVkNyIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>
       </div>
        """,
        unsafe_allow_html=True
    )      
    
if __name__ == "__main__":
    main()

st.title("")

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    
with st.container():
    
    st.header("Contactanos!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/strategicdatatransform@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nombre" required>
        <input type="email" name="email" placeholder="E-mail" required>
        <textarea name="message" placeholder="Tu consulta" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/marceloyuba/StreamlitBA/blob/main/scr/fondoba.png?raw=true");
background-position: top left;
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
