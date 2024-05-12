

import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="Accidentes - Strategic Data Transform", page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")
with st.container():
    
    st.markdown('<style>h4{color: white;}, font=</style>', unsafe_allow_html=True)    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>write {color: white;}, font=</style>', unsafe_allow_html=True)
st.write("""
<style>
    .fixed-container {
        position: relative;
        bottom: 30px;
        padding: 10px;
        left: 10%;
        background-image:img src="https://github.com/marceloyuba/StreamlitSDT/blob/main/scr/SDTLogoC.png?raw=true" ;
        background-color: rgba(0, 0, 0, 0);
        color: #ffffff;
        
        width: 1280px;
        height: auto;
        z-index: 9999;
        
    }
    .fixed-container img {
        width: 1100px; /* Ancho de la imagen */
        height: auto; /* Autoajuste de la altura según el ancho */
        margin: 0 auto; /* Centro horizontalmente */
        display: block; /* Convertir la imagen en un bloque para aplicar márgenes automáticos */
    }
    .BA img {
        width: 550px; /* Ancho de la imagen */
        height: auto; /* Autoajuste de la altura según el ancho */
        margin: 0 auto; /* Centro horizontalmente */
        display: block; /* Convertir la imagen en un bloque para aplicar márgenes automáticos */
    }
    .fixed-container a {
        font-size: 20px;
        margin-top: 10px; /* Espacio después de la imagen */
        text-decoration: none; /* Quitar el subrayado */
        color: #ffffff; /* Cambiar el color del texto del enlace */
        
    }
</style>
""", unsafe_allow_html=True)
column_widths = [1, 1, 2]
with st.container():
    st.title("")
    col1, col2, col3 = st.columns(column_widths)   
    with col1:
        st.image("scr/Logo_Buenos_Aires.png",width=550, use_column_width=True, output_format='auto')
        
    with col2:
        st.text("")
          
    with col3: 
        st.image("scr/SDTLogoC.png",width=1200, use_column_width=True, output_format='auto')

st.title("") 

            
st.write("""
<style>
    .botones a {
        font-size: 30px;
        margin-top: 10px; /* Espacio después de la imagen */
        text-decoration: none; /* Quitar el subrayado */
        color: #ffffff; /* Cambiar el color del texto del enlace */
        
    }
</style>
""", unsafe_allow_html=True)  

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
        st.image(imagen, width=500, use_column_width=True, output_format='auto')
    

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

st.title("Nuestro equipo de trabajo")

with st.container():
     
    col1, col2 = st.columns(column_widths)
    
    
    with col1:
        st.header("Elizabeth Fraire")
        st.markdown(""" 
                #### Departamento: Data Science, Engineering, Analist
                #### Background: Ciencias Biológicas
                #### Linkedin: [Acceder a su perfil](https://www.linkedin.com/in/veronica-elizabeth-torres-fraire-a830bb234/)
                #### Github: [Acceder a su perfil](https://github.com/Bethcosima)
                """) 
    
    with col2:
        imagen = "scr/Eli.jpg"  
        st.image(imagen, width=250, use_column_width=False, output_format='auto')    

st.title("")

with st.container():
     
    col1, col2 = st.columns(column_widths)
    
    
    with col1:
        st.header("Marcelo Yuba")
        st.markdown(""" 
                #### Departamento: Data Analist, Graphic Design
                #### Background: Diseño multimedial, Publicidad grafica, E-Commerce
                #### Linkedin: [Acceder a su perfil](www.linkedin.com/in/marcelo-yuba)
                #### Github: [Acceder a su perfil](https://github.com/marceloyuba)
                """) 
    with col2:
        imagen = "scr/fotoLI.jpg"  
        st.image(imagen, width=250, use_column_width=False, output_format='auto')   





page_bg_img = f"""
<style>

[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://github.com/marceloyuba/StreamlitSDT/blob/main/scr/fondoi.png?raw=true");
background-position: top left;
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)