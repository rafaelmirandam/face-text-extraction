
# 🧠 Face & Text Detection with AWS Rekognition + Textract

This Streamlit app allows you to upload an image and:
- Detect faces using Amazon Rekognition
- Extract text using Amazon Textract

## 📦 Features

- 🔍 Face detection with bounding boxes
- 📝 OCR with text display
- 100% Cloud-based (no local dependencies)

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up environment variables

Create a `.env` file in the root of your project with:

```
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_REGION=us-east-1
```

### 3. Launch the app
```bash
streamlit run app_aws.py
```

## 🛡️ Requirements

- An active AWS account
- Rekognition and Textract enabled in IAM permissions
- Streamlit Cloud compatible
