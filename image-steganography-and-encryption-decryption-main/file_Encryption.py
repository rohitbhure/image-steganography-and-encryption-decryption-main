



############################################## PACKAGES & MODULES ###########################################


from cryptography.fernet import Fernet
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from functools import partial

############################################## GLOBAL VARIABLES #############################################

global filename
button_height = 2
button_width = 25


############################################# BROWSE FILES ##################################################


def browseFiles():
    browseFiles.filename = filedialog.askopenfilename(initialdir="/", title="Select a File",)
    file_explorer.configure(text="File Opened: " + browseFiles.filename)

    passwd_label.pack()
    password_entry.pack()
    temp_label.pack()
    button_encrypt.pack()
    button_decrypt.pack()
    
############################################# ENCRYPTION ######################################################


def encrypt_file(pass_word):
    secret_key = pass_word.get()
    if secret_key == "":
        messagebox.showerror("Alert", "Please enter secret key")
    else:     
        secret_key = ''.join(p for p in secret_key if p.isalnum())
        key = secret_key + ("s" * (43 - len(secret_key)) + "=")

        fernet = Fernet(key)

        with open(browseFiles.filename, 'rb') as file:  original = file.read()
        encrypted = fernet.encrypt(original)

        with open(browseFiles.filename, 'wb') as encrypted_file:    encrypted_file.write(encrypted)

        status_label.configure(text="Encrypted")
        status_label.pack()

############################################## DECRYPTION ####################################################


def decrypt_file(pass_word):
    secret_key = pass_word.get()
    if secret_key == "":
        messagebox.showerror("Alert", "Please enter secret key")
    elif secret_key != pass_word:
        messagebox.showerror("Alert", "Please enter Correct secret key")

    else:    
        secret_key = ''.join(p for p in secret_key if p.isalnum())
        key = secret_key + ("s" * (43 - len(secret_key)) + "=")

        fernet = Fernet(key)
        

        with open(browseFiles.filename, 'rb') as encrypt_file:  encrypted = encrypt_file.read()
        decrypted = fernet.decrypt(encrypted)

        with open(browseFiles.filename, 'wb') as decrypt_file:  decrypt_file.write(decrypted)

        status_label.configure(text="Decrypted")
        status_label.pack()


################################################################  USER INTERFACE ############################################################################

################################################################     Tkinter     ############################################################################

root = Tk()

root.title('File Encryptor and Decryptor')
root.geometry("1460x740")
root.config(background="black")

main_title = Label(root, text = "File Encrypter and Decrypter", width=100, height=2, fg="white", bg="black", font=("",30))
password = StringVar()


encrypt_fun = partial(encrypt_file,password)
decrypt_fun = partial(decrypt_file,password)

credit = Label(root, text="Developed By CSE Department Group-19, Major Project-I", bg="black", height=2, fg="white", font=("",15))
file_explorer = Label(root, text="File Name: ", width=100, height=2, fg="white", bg="black",font=("",20))
passwd_label = Label(root, text="Enter the Secret key: ", width=100, height=2, fg="white", bg="black",font =("",20)) 
temp_label = Label(root, text="",height=3,bg="black")

button_explore = Button(root, text="Browse File", command=browseFiles, width=button_width, height=button_height, font =("",15))

password_entry = Entry(root, textvariable=password,show="*")                     


button_encrypt = Button(root, text="Encrypt", command=encrypt_fun, width=button_width, height=button_height, font =("",15))
button_decrypt = Button(root, text="Decrypt", command=decrypt_fun, width=button_width, height=button_height, font =("",15))


status_label = Label(root, text="", width=100, height=4, fg="white", bg="black",font =("",17))

credit.pack()
main_title.pack()
file_explorer.pack()
button_explore.pack()
root.mainloop()


################################################################     END     ############################################################################
