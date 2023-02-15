# Encryption and Decryption using AES in Python
This is a Python program that demonstrates encryption and decryption using Advanced Encryption Standard (AES) with Cipher-Block Chaining (CBC) mode of operation. It uses the PyCryptodome package for AES encryption and decryption.

The program reads a text file that contains student numbers and encrypts them. It then writes the encrypted student numbers to a new file. The program can also decrypt the encrypted student numbers and write them to a separate file.

The program uses a password-based key derivation function to derive an AES encryption key from a user-provided password. It generates a random initialization vector (IV) for each student number and uses the derived key and the IV to encrypt and decrypt the student numbers.

The program also uses the pickle module to store the IVs and the derived key for decryption after the program is terminated.

# Prerequisites
The following packages are required to run the program:

PyCryptodome
pbkdf2
# Usage
Run the encryption.py file in a Python environment.

When prompted, enter either e for encryption or d for decryption. If you choose to encrypt, you will be prompted to enter the file path for the text file containing student numbers. If you do not specify a file path, the program will use the default file student_numbers.txt.

The program will generate a new file named encrypted.txt that contains the encrypted student numbers.

If you choose to decrypt, the program will use the encrypted.txt file to decrypt the student numbers and write them to a new file named decrypted.txt.

When the program finishes, it will ask whether to decrypt or exit. If you choose to exit, the program will terminate. If you choose to decrypt, the program will read the IVs and the derived key from the pickle files and use them to decrypt the student numbers.

Note: The program writes the encrypted and decrypted student numbers to new files, but it does not delete the files after use. You should delete these files manually after use.
