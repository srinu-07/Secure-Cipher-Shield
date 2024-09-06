import os
from flask import Flask, render_template, request, send_file
from PIL import Image
import stepic
from cryptography.fernet import Fernet

app = Flask(__name__)

# Ensure the downloads directory exists
if not os.path.exists('downloads'):
    os.makedirs('downloads')

def generate_unique_filename(directory, base_name, extension):
    counter = 1
    new_filename = f"{base_name}{extension}"
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base_name}({counter}){extension}"
        counter += 1
    return new_filename

def encrypt_fernet(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_fernet(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message)
    return decrypted_message.decode()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_key')
def generate_key():
    key = Fernet.generate_key().decode('utf-8')
    return key

@app.route('/hide', methods=['POST'])
def hide():
    image_file = request.files['image']
    message = request.form['message']
    key = request.form['key']
    if not (image_file and message and key):
        return 'Missing required parameters', 400
    
    # Encrypt the message
    encrypted_message = encrypt_fernet(message, key)

    # Open the image and encode the message
    image = Image.open(image_file.stream)
    encoded_image = stepic.encode(image, encrypted_message)

    # Generate a unique filename
    base_name, extension = os.path.splitext('encoded_image.png')
    unique_filename = generate_unique_filename('downloads', base_name, extension)
    output_path = os.path.join('downloads', unique_filename)

    # Save the encoded image
    encoded_image.save(output_path)

    return send_file(output_path, mimetype='image/png', as_attachment=True)

@app.route('/reveal', methods=['POST'])
def reveal():
    image_file = request.files['image']
    key = request.form['key']
    if not (image_file and key):
        return 'Missing required parameters', 400
    
    # Open the image and decode the message
    image = Image.open(image_file.stream)
    encrypted_message = stepic.decode(image)

    # Decrypt the message
    message = decrypt_fernet(encrypted_message, key)

    return message

if __name__ == "__main__":
    app.run(debug=True)
