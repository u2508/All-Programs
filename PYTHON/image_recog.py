import dlib
import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

def check_facial_similarity(input_image_path, default_image_path):
    # Load the default image
    default_image = dlib.load_rgb_image(default_image_path)
    
    # Load the input image
    input_image = dlib.load_rgb_image(input_image_path)
    
    # Create a face detector
    detector = dlib.get_frontal_face_detector()
    
    # Detect faces in the default image
    default_faces = detector(default_image)
    
    # Detect faces in the input image
    input_faces = detector(input_image)
    
    # Create a face recognition model
    shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    face_recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
    
    # Compute face descriptors for the default image
    default_descriptors = []
    for face in default_faces:
        shape = shape_predictor(default_image, face)
        descriptor = face_recognizer.compute_face_descriptor(default_image, shape)
        default_descriptors.append(descriptor)
    
    # Compute face descriptors for the input image
    input_descriptors = []
    for face in input_faces:
        shape = shape_predictor(input_image, face)
        descriptor = face_recognizer.compute_face_descriptor(input_image, shape)
        input_descriptors.append(descriptor)
    
    # Compare face descriptors and check for similarity
    similarity = False
    for input_descriptor in input_descriptors:
        for default_descriptor in default_descriptors:
            distance = dlib.distance(input_descriptor, default_descriptor)
            if distance < 0.75:  # Adjust the threshold as needed
                similarity = True
                break
    
    return similarity

# Usage example
input_image_path = file_path
default_image_path = "C:\\Users\\utkar\\Downloads\\WhatsApp Image 2023-05-26 at 1.28.17 AM (2).jpeg"
result = check_facial_similarity(input_image_path, default_image_path)

# Print the result
if result:
    print("The input image is similar to the default image.")
else:
    print("The input image is not similar to the default image.")
