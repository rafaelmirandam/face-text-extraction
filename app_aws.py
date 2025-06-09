
import os
import streamlit as st
import boto3
from PIL import Image, ImageDraw
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

rekognition = boto3.client(
    "rekognition",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

textract = boto3.client(
    "textract",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

st.title("🧠 AWS Rekognition + Textract")

uploaded_file = st.file_uploader("📤 Envie uma imagem", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="📷 Imagem Original", use_container_width=True)

    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()

    st.subheader("🧑‍🦱 Rostos detectados:")
    response_faces = rekognition.detect_faces(Image={"Bytes": img_bytes}, Attributes=["ALL"])
    draw = ImageDraw.Draw(image)

    for i, detail in enumerate(response_faces["FaceDetails"]):
        box = detail["BoundingBox"]
        w, h = image.size
        left = int(box["Left"] * w)
        top = int(box["Top"] * h)
        right = int(left + box["Width"] * w)
        bottom = int(top + box["Height"] * h)
        draw.rectangle([left, top, right, bottom], outline="red", width=2)
        st.image(image.crop((left, top, right, bottom)), caption=f"Face {i+1}", width=150)

    st.subheader("🖼️ Imagem com caixas:")
    st.image(image, use_container_width=True)

    st.subheader("📝 Texto extraído da imagem:")
    response_text = textract.detect_document_text(Document={"Bytes": img_bytes})
    full_text = " ".join([block["Text"] for block in response_text["Blocks"] if block["BlockType"] == "LINE"])
    st.text(full_text)
