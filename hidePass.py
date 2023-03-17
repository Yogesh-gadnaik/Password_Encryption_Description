# 1. with join and split method we can encrypt password by simple way--->

# def encrypt(key,str):
#     return key.join(str)

# def decrypt(key,str):
#     return str.split(key)

# Password=str(input("Enter your password"))
# key=input("Enter the key")

# enc=encrypt(key,Password)
# print("Encrypted password is:",enc)

# dec=decrypt(key,Password)
# original_pass=" ".join(dec)
# print("Decrypted password is:",original_pass)


# 2. With crytography module we can encrypt and decript the password for sequrity purpose--->

# from cryptography.fernet import Fernet

# def function(value):
#     key = Fernet.generate_key()             # It will genrate the random key
#     print(key)
#     f = Fernet(key)                         # Need to create the object of fernet class for encryption
#     pat=value.encode()                      # we need to Encoding the password before encryptin i.e changing strin to byte object
#     encrypted_data = f.encrypt(pat)         #It will encrypt the password based on genrated key
#     print("After encryption : ", encrypted_data)
#     decrypted_data = f.decrypt(encrypted_data)                # It will secript the password based on key
#     print(decrypted_data)
#     print("After decryption : ", decrypted_data.decode())      # It will convert the byte into string oject.

# password=str(input("Enter your passowrd"))
# function(password)


# 3.  With bcrypt module we can do encryption and decription of password---->


import bcrypt
# store your password</strong>:
password = str(input("input password: "))
# Encode the stored password</strong>:
password = password.encode('utf-8')
# Encrypt the stored pasword</strong>:
hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
print(hashed)
# Create an authenticating password input field to check if a user enters the correct password</strong>
check = str(input("check password: "))
# Encode the authenticating password as well</strong>
check = check.encode('utf-8')
print(check)
print(bcrypt.checkpw(check, hashed))
# Use conditions to compare the authenticating password with the stored one</strong>:
if bcrypt.checkpw(check, hashed):
    print("login success")
else:
    print("incorrect password")
