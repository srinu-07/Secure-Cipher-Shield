Secure Cipher Shield

Secure Cipher Shield is a web application built with Flask that allows users to securely hide and reveal encrypted messages within images using Steganography and cryptography. The application uses the Fernet symmetric encryption from the cryptography library to encrypt messages, and Stepic to encode them into images.

Features

Encrypt Messages: Users can input a secret message and encrypt it using a cryptographic key.
Hide Messages in Images: The encrypted message is embedded in a chosen image using steganography.
Reveal Hidden Messages: Users can upload an image with an encrypted message and a key to extract and decrypt the hidden message.

Key Generation: A key can be generated securely using the Fernet encryption algorithm for message encryption and decryption.

Technologies Used

Flask: Web framework for Python.

Pillow (PIL): Python Imaging Library used to manipulate images.

Stepic: Library for steganography used to encode/decode messages in images.

Cryptography (Fernet): Provides symmetric encryption for securing the messages.

HTML/CSS/JavaScript: Frontend technologies for creating the user interface.

Prerequisites

Before running this application, ensure you have the following installed:

Python 3.x
Flask
Pillow (pip install pillow)
Stepic (pip install stepic)
Cryptography (pip install cryptography)



Usage

1. Hide a Message:

Upload an image.
Enter the message to hide.
Provide the encryption key (you can generate one if needed).
Download the encoded image with the hidden message.

2. Reveal a Message:

Upload the image with the hidden message.
Enter the key used to encrypt the message.
The hidden message will be revealed.

3. Generate a Key:
Click on the "Generate Key" button to create a new secure key for encryption.

Notes:

The application ensures that multiple users can encode different images without conflicts by generating unique filenames for every encoded image.
For added security, ensure the encryption key is stored securely and is not shared publicly.
The application is meant for educational purposes and should not be used for securing sensitive data in a production environment.

Future Enhancements

Implement error handling and validation for uploaded files.
Add support for other image formats besides PNG.
Improve the user interface with additional feedback and status messages.
