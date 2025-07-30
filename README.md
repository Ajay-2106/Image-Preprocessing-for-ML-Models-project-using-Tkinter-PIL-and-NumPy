# 🖼️ Image Preprocessor for Machine Learning Models

This Python script allows you to select an image using a GUI (Tkinter), convert it to grayscale, resize it to 256×256 pixels, and normalize it for machine learning use. It also saves the preprocessed image in PNG format. The output is a NumPy-ready array suitable for feeding into CNN-based models (e.g., Keras/TensorFlow).

---

## 🚀 Features
- GUI-based file selection and saving (via `tkinter`)
- Converts any image to **grayscale**
- Resizes image to **256x256** using bilinear interpolation
- Normalizes pixel values to the range **[0, 1]**
- Returns image as a NumPy array shaped as `(1, 256, 256, 1)` — ready for ML input
- Saves preprocessed image to user-defined location

---

## 🛠 Requirements
- Python 3.x
- Libraries: **pillow**, **numpy**
