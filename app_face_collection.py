
import os
import streamlit as st
import boto3
from PIL import Image
import io

# Carrega credenciais da AWS (secrets ou .env)
try:
    AWS_ACCESS_KEY_ID = st.secrets["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = st.secrets["AWS_SECRET_ACCESS_KEY"]
    AWS_REGION = st.secrets["AWS_REGION"]
except Exception:
    from dotenv import load_dotenv
    load_dotenv()
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION")

# Inicializar cliente Rekognition
rekognition = boto3.client(
    "rekognition",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

st.title("🧠 Reconhecimento Facial com Coleção - AWS Rekognition")

colecao_id = "face-collection-app"

# Criar coleção se necessário
try:
    rekognition.create_collection(CollectionId=colecao_id)
    st.success(f"Coleção '{colecao_id}' criada.")
except rekognition.exceptions.ResourceAlreadyExistsException:
    st.info(f"Coleção '{colecao_id}' já existe.")

st.header("📥 Indexar rosto conhecido")
with st.form("indexar_form"):
    nome_pessoa = st.text_input("Nome da pessoa (identificador)")
    imagem_conhecida = st.file_uploader("Imagem do rosto conhecido", type=["jpg", "jpeg", "png"], key="conhecida")
    submitted = st.form_submit_button("Indexar rosto")
    if submitted and imagem_conhecida and nome_pessoa:
        image = Image.open(imagem_conhecida).convert("RGB")
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="JPEG")
        img_bytes = img_bytes.getvalue()

        response = rekognition.index_faces(
            CollectionId=colecao_id,
            Image={"Bytes": img_bytes},
            ExternalImageId=nome_pessoa,
            DetectionAttributes=["DEFAULT"]
        )

        if response["FaceRecords"]:
            st.success(f"Rosto de '{nome_pessoa}' indexado com sucesso.")
        else:
            st.error("Nenhum rosto detectado na imagem.")

st.header("🔍 Reconhecer rosto enviado")
imagem_teste = st.file_uploader("Imagem para reconhecimento", type=["jpg", "jpeg", "png"], key="teste")

if imagem_teste:
    image = Image.open(imagem_teste).convert("RGB")
    st.image(image, caption="Imagem para reconhecimento", use_container_width=True)

    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()

    response = rekognition.search_faces_by_image(
        CollectionId=colecao_id,
        Image={"Bytes": img_bytes},
        MaxFaces=1,
        FaceMatchThreshold=85
    )

    matches = response.get("FaceMatches", [])
    if matches:
        face = matches[0]["Face"]
        st.success(f"✅ Rosto reconhecido como: **{face['ExternalImageId']}** (confiança: {face['Confidence']:.2f}%)")
    else:
        st.warning("❌ Nenhum rosto correspondente encontrado.")
