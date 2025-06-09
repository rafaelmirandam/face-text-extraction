
# 🧠 Face & Text Extraction with OpenAI Vision API

This project demonstrates the use of OpenAI's GPT-4 Vision model to detect and crop faces and extract text from images. It includes a Jupyter Notebook for the analysis and a Streamlit app for interactive testing.

## 📦 Features

- ✅ **Face Detection**: Automatically locates and crops faces from input images.
- ✅ **Text Extraction**: Recognizes and extracts textual content embedded in the image.
- ✅ **Cloud-based Inference**: Utilizes OpenAI GPT-4 Vision API for all processing.
- ✅ **Streamlit App**: Interactive app for uploading images and viewing results.

## 🧪 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/rafaelmirandam/face-text-extraction.git
cd face-text-extraction
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment
Create a `.env` file and insert your OpenAI API key:
```
OPENAI_API_KEY=sk-xxxxxx
```

### 4. Run the Notebook
Open and run the Jupyter notebook:
```
jupyter notebook face_text_extraction.ipynb
```

### 5. Launch the Streamlit App
```bash
streamlit run app.py
```

## 🌐 Streamlit Cloud
You can deploy this app to [Streamlit Cloud](https://streamlit.io/cloud) by:
- Uploading the files to a public GitHub repo
- Adding your API key to the Streamlit Secrets
- Pointing to `app.py` as the main file

## 📁 Project Structure

```
.
├── face_text_extraction.ipynb   # Notebook with OpenAI API calls
├── app.py                       # Streamlit app
├── .env                         # OpenAI API Key (not shared)
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🧠 Model
- **Model**: `gpt-4-vision-preview`
- **Provider**: OpenAI Cloud API
