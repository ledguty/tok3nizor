import streamlit as st
import PyPDF2
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def leer_archivo(archivo):
    if archivo.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(archivo)
        texto = ""
        for pagina in pdf_reader.pages:
            texto += pagina.extract_text()
    else:
        texto = archivo.getvalue().decode("utf-8")
    return texto

def tokenizar(texto):
    return word_tokenize(texto)

st.title("Lector de Tokens")

archivo_subido = st.file_uploader("Sube un archivo PDF o TXT", type=["pdf", "txt"])

if archivo_subido is not None:
    texto = leer_archivo(archivo_subido)
    tokens = tokenizar(texto)
    
    st.write(f"Número total de tokens: {len(tokens)}")
    st.write("Primeros 100 tokens:")
    st.write(tokens[:100])
