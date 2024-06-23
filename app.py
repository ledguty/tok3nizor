import streamlit as st
import PyPDF2
import spacy

# Cargar el modelo de español de spaCy
@st.cache_resource
def load_model():
    return spacy.load("es_core_news_sm")

nlp = load_model()

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
    doc = nlp(texto)
    return [token.text for token in doc]

st.title("Analizador de Tokens")

archivo_subido = st.file_uploader("Sube un archivo PDF o TXT", type=["pdf", "txt"])

if archivo_subido is not None:
    texto = leer_archivo(archivo_subido)
    tokens = tokenizar(texto)
    
    st.write(f"Número total de tokens: {len(tokens)}")
    
    # Mostrar los primeros 100 tokens
    st.write("Primeros 100 tokens:")
    st.write(tokens[:100])
    
    # Análisis detallado de los primeros 20 tokens
    st.write("Análisis detallado de los primeros 20 tokens:")
    doc = nlp(texto[:1000])  # Analizamos solo los primeros 1000 caracteres para velocidad
    for token in list(doc)[:20]:
        st.write(f"Texto: {token.text}, Lema: {token.lemma_}, Tipo: {token.pos_}, Etiqueta detallada: {token.tag_}")

    # Frecuencia de tokens
    from collections import Counter
    frecuencia = Counter(tokens)
    st.write("Tokens más frecuentes:")
    st.write(frecuencia.most_common(10))
