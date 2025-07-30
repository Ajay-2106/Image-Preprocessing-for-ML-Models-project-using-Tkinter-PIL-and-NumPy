from PIL import Image
import numpy as np
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def preprocess_image_for_model(image_path, save_path=None):
    
    img = Image.open(image_path).convert("L")
    img_resized = img.resize((256, 256), Image.BILINEAR)
    if save_path:
        img_resized.save(save_path, format='PNG')
        img_array = np.array(img_resized).astype(np.float32)
        img_array /= 255.0
        img_ready = img_array.reshape(1, 256, 256, 1)
    return img_ready

if __name__ == "__main__":
    Tk().withdraw()
    image_path = askopenfilename(
        title="Select Image for Preprocessing",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff")]
    )
    print("Uploaded image is pre-processed")

    if not image_path:
        print("No image selected. Exiting.")
        exit()

    save_path = asksaveasfilename(
        title="Save Pre-processed Image",
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png")]
    )
    if not save_path:
        print("No image saved. Exiting.")
        exit()
    print("Pre-processed image saved")

processed = preprocess_image_for_model(image_path, save_path)