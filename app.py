
import streamlit as st
import openai
import base64
from PIL import Image, ImageDraw
import io
import os
import re
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 Face Recognition + Text Extraction (OpenAI Vision)")

uploaded_file = st.file_uploader("📤 Envie uma imagem (JPEG/PNG)", type=["jpg", "jpeg", "png"])

def extract_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def extract_coordinates(text):
    pattern = r"\[\s*(\d+),\s*(\d+),\s*(\d+),\s*(\d+)\s*\]"
    return [list(map(int, match)) for match in re.findall(pattern, text)]

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="📷 Imagem Original", use_column_width=True)

    base64_img = extract_base64(image)

    prompt = (
        "Detecte todos os rostos nesta imagem e retorne as coordenadas no formato: "
        "[left, top, right, bottom] para cada rosto. Depois, extraia e liste todos os textos encontrados na imagem."
    )

    with st.spinner("🔍 Analisando com GPT-4 Vision..."):
        response = openai.ChatCompletion.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_img}"}}
                    ]
                }
            ],
            max_tokens=1200
        )

    content = response["choices"][0]["message"]["content"]
    st.subheader("📝 Resultado bruto da API")
    st.text(content)

    coords = extract_coordinates(content)
    st.subheader(f"🧑‍🦱 Rostos Detectados: {len(coords)}")

    draw = ImageDraw.Draw(image)
    for i, (l, t, r, b) in enumerate(coords):
        face_img = image.crop((l, t, r, b))
        st.image(face_img, caption=f"Face {i+1}", width=150)
        draw.rectangle([l, t, r, b], outline="red", width=2)

    st.subheader("🖼️ Imagem com caixas desenhadas:")
    st.image(image, use_column_width=True)
