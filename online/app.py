from flask import Flask, render_template, request, jsonify
from model import process_image
import matplotlib.pyplot as plt
import numpy as np
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    file = request.files['fileInput']
    K = int(request.form['compressionLevel'])
    
    original_img = plt.imread(file)
    original_img = original_img / 255.0
    
    # Process the image
    processed_image = process_image(original_img, K)
    
    # Save processed image to a temporary file
    with open('processed_image.png', 'wb') as f:
        plt.imsave(f, processed_image, format='png')
    
    # Convert processed image to base64 string
    with open('processed_image.png', 'rb') as f:
        img_str = base64.b64encode(f.read()).decode('utf-8')

    return jsonify({'result': img_str})

if __name__ == '__main__':
    app.run(debug=True)
