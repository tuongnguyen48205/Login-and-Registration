# Key encryption system
# Created by Tuong Bao Nguyen

# Import the neccesary libraries
from cryptography.fernet import Fernet

def generate_key():
    '''
    This function generates a key for encryption
    '''
    # Generate the key and string the key in a file
    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    return

def encrypt(csv_name):
    '''
    This function encrypts a given csv file
    '''
    # Open the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)

    # Open the file that needs to be encrypted
    with open(csv_name, 'rb') as file:
        original = file.read()

    # Encrypt the file
    encrypted = fernet.encrypt(original)

    # Open the file and writing the encrypted data
    with open(csv_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    return

def decrypt(csv_name):
    '''
    This function decrypts a given csv file
    '''
    # Open the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)

    # Open the encrypted file
    with open(csv_name, 'rb') as enc_file:
        encrypted = enc_file.read()
    
    # Decrypt the file
    decrypted = fernet.decrypt(encrypted)

    # Open the file and write the decrypted data
    with open(csv_name, 'wb') as dec_file:
        dec_file.write(decrypted)
    
    return

