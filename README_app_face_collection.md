
# 🧠 Face Recognition using AWS Rekognition Collections

This Streamlit app allows you to:
- Index known faces into a Rekognition collection
- Upload a new image and identify if the face matches someone already indexed

## 📦 Features

- 🧑‍💼 Face indexing with person ID (name)
- 🔍 Face recognition from new image
- Uses AWS Rekognition collections
- No local face processing required

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
streamlit run app_face_collection.py
```

## 🛡️ Requirements

- AWS account with Rekognition enabled
- Permissions for:
  - rekognition:CreateCollection
  - rekognition:IndexFaces
  - rekognition:SearchFacesByImage
