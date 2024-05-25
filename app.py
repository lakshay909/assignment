from flask import Flask, request, jsonify, send_from_directory, render_template_string
from werkzeug.utils import secure_filename
import os
import boto3
import csv
from PIL import Image, ImageDraw, ImageFont
import io
import cv2
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    with open('static/index.html', 'r') as file:
        return render_template_string(file.read())

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def detect_text(img_path):
    # with open(rekognition_path, 'r') as file:
    #     next(file)
    #     reader = csv.reader(file)
    #     for line in reader:
    access_key_id = 'AKIAW3MEFEVHLVVM7Z5F'
    secret_access_key = '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'

    client = boto3.client('rekognition', region_name='us-west-2',
                          aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    with open(img_path, 'rb') as image_file:
        source_bytes = image_file.read()

    detect_text_response = client.detect_text(Image={'Bytes': source_bytes})

    detected_texts = [text['DetectedText'] for text in detect_text_response['TextDetections']]
    return detected_texts

def detect_labels(img_path):
    # with open(rekognition_path, 'r') as file:
    #     next(file)
    #     reader = csv.reader(file)
    #     for line in reader:
    access_key_id = 'AKIAW3MEFEVHLVVM7Z5F'
    secret_access_key = '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'

    client = boto3.client('rekognition', region_name='us-west-2',
                          aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    with open(img_path, 'rb') as image_file:
        source_bytes = image_file.read()

    detect_objects = client.detect_labels(Image={'Bytes': source_bytes})

    image = Image.open(io.BytesIO(source_bytes))
    draw = ImageDraw.Draw(image)

    for label in detect_objects['Labels']:
        for instance in label['Instances']:
            if 'BoundingBox' in instance:
                box = instance["BoundingBox"]
                image_width, image_height = image.size
                left = image_width * box['Left']
                top = image_height * box['Top']
                width = image_width * box['Width']
                height = image_height * box['Height']

                points = [
                    (left, top),
                    (left + width, top),
                    (left + width, top + height),
                    (left, top + height),
                    (left, top)
                ]

                draw.line(points, width=2, fill="#FF0000")

                font = ImageFont.truetype("arial.ttf", 15)
                draw.text((left, top - 10), label["Name"], font=font, fill='#FF0000')

    processed_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_image.jpg')
    image.save(processed_image_path)
    return processed_image_path

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    # rekognition_path = '/Users/lakshaynarula/Desktop/Codes/Text and Visual analysis/vision-rekongnition_accessKeys.csv'
    
    detected_texts = detect_text(file_path)
    processed_image_path = detect_labels(file_path)

    # Serve the processed image by returning its URL
    image_url = f'/uploads/{os.path.basename(processed_image_path)}'
    
    return jsonify({
        'text': '\n'.join(detected_texts),
        'image_url': image_url
    })

if __name__ == "__main__":
    app.run(debug=True)
