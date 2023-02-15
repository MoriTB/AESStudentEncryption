import binascii
import os
import pbkdf2
import pyaes
import secrets
import pickle


# encryption and key is used to be shown in hexifiy format.
def key(password):
    # Derive a 256-bit AES encryption key from the password
    # need to change the location of the password
    # it should not be hard driven....
    passwordSalt = os.urandom(16)
    keygenerated = pbkdf2.PBKDF2(password, passwordSalt).read(32)
    keygeneratedHexified = binascii.hexlify(keygenerated)
    print('AES encryption key:', keygeneratedHexified)
    return keygeneratedHexified


def aesEncryption(student_number, sharekey,
                  initialVector):  # generating initial vector outside helps with simpler execution in decrypting.
    aes = pyaes.AESModeOfOperationCTR(sharekey, pyaes.Counter(initialVector))
    ciphertext = aes.encrypt(student_number)
    # print('Encrypted:', binascii.hexlify(ciphertext))
    ciphertextHexified = binascii.hexlify(ciphertext)
    return ciphertextHexified  # we use the hexlify version to submit into our file.


def decryption(ciphertext, iv, usedkey):
    aes = pyaes.AESModeOfOperationCTR(usedkey, pyaes.Counter(iv))
    decrypted = aes.decrypt(ciphertext)
    # print('Decrypted:', decrypted)
    return decrypted


if __name__ == '__main__':
    # encrypting the text file with getting address or using default.
    # decrypting the text file with getting address or using default. ( if a new file is given we should know iv so default it is)
    ivCount = []
    model = input("what do you want(e/d)?\n")
    secondModel = ''
    file1 = open("/Users/apple/PycharmProjects/securitySecondPhase/pass_key.txt", "r")
    stringpass = file1.read()
    keyGenerated = key(stringpass)
    keyGenerated = binascii.unhexlify(
        keyGenerated)  # unhexlify the process because the output is displaying number in hex.
    while True:
        if model == 'e':  # encryption method set.
            file_student = ''  # making manual test file.
            address_student = input(
                "please input the address of student file. (you can use 'default' command for our student file.)\n")
            if address_student == "default":
                file_student = open("/Users/apple/PycharmProjects/securitySecondPhase/student_numbers", "r")
            else:
                file_student = open(address_student, "r")
            file_encryption = open("/Users/apple/PycharmProjects/securitySecondPhase/encrypted.txt", "wb")
            file1 = open("/Users/apple/PycharmProjects/securitySecondPhase/pass_key.txt", "r")
            for student_numbers in file_student:
                student_numbers = student_numbers.replace('\n', '')
                iv = secrets.randbits(256)
                encryptedStudentNumber = aesEncryption(student_numbers, keyGenerated, iv)  # this is hexlified version
                ivCount.append(iv)
                file_encryption.write(encryptedStudentNumber)
                # find a way to dont use \n for specification .
                bytes = b'\n'
                file_encryption.write(bytes)
            file_encryption.close()
            print("the encryption was successful.")
            with open('pickled_list.pickle', 'wb') as remembering:  # saving iv for decryption after the program is done.
                pickle.dump(ivCount, remembering)
            with open('pickled_list1.pickle', 'wb') as key_remember:  # saving keygenerated for decryption after the program is done.
                pickle.dump(keyGenerated, key_remember)
            secondModel = input(
                "do you want to decrypt the encryption?(y/n)?\n")  # usually we want to do that to show everything works pretty fine.
        if model == 'd' or secondModel == 'y':
            file_decryption = open("/Users/apple/PycharmProjects/securitySecondPhase/decrypted.txt", "wb")
            counter = 0
            with open('pickled_list.pickle', 'rb') as remembered: # to load the previous iv used for encryption.
                iv_list_registered = pickle.load(remembered)
            with open('pickled_list1.pickle', 'rb') as key_remembering:  # to load the previous iv used for encryption.
                keyGenerated = pickle.load(key_remembering)
            with open("/Users/apple/PycharmProjects/securitySecondPhase/encrypted.txt", "rb") as encrypted:
                for encryption in encrypted:
                    # print("******************* decryption *********************")
                    encryption = encryption.replace(b'\n',
                                                    b'')  # we used this to cover the \n problem for showing properly in encryption.
                    encryption = binascii.unhexlify(
                        encryption)  # unhexlify it because the format saved is registered in hex format.
                    plaintext = decryption(encryption, iv_list_registered[counter], keyGenerated)
                    file_decryption.write(plaintext)
                    bytes = b'\n'
                    file_decryption.write(bytes)
                    counter = counter + 1
            file_decryption.close()
            print("the decryption was successful.")
            break
        if model == 'exit' or secondModel == 'n':
            if secondModel == 'n':
                file_decryption = open("/Users/apple/PycharmProjects/securitySecondPhase/decrypted.txt", "wb")
                file_decryption.close()
            break
        else:
            print("please try again. you can quit by 'exit' command. ")
            model = input()
