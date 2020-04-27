#!/user/bin/python

from termcolor import colored
import hashlib


print("  __  __ ____  __     ___ _     _    _  _   _ _   _    ")
print(" |  \\/  |  _ \\ \\ \\   / / | |   | |  | || | / | \\ | |   ")
print(" | |\\/| | |_) | \\ \\ / /| | |   | |  | || |_| |  \\| |    ")
print(" | |  | |  _ <   \\ V / | | |___| |__|__   _| | |\\  |  ")
print(" |_|  |_|_| \\_\\___\\_/  |_|_____|_____| |_| |_|_| \\_|  ")
print("             |_____|                                 ")
print("             MD5-Decoder by Villain                      ")
                                                 
                                                 

def md5(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist, "r")
    except:
        print("[!!] No Such File At This Path! ")
        quit()

pass_hash = input("[*] Enter MD5 Hash Value: ")
wordlist = input("[*] Enter Passlist Here: ")
md5(wordlist)

for word in pass_file:
    print(colored("[-] trying: " + word.strip("\n"), 'red'))
    enc_wrd = word.encode('utf-8')
    md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    if md5digest == pass_hash:
        print(colored("[+] password has been cracked: " + word, 'green'))
        
print("[!] Did not find the password in list! ")



Hex = input("Enter hex i will convert ascii:")

ASCII = bytearray.fromhex(Hex).decode()

print(ASCII)
exit(0)