import hashlib
import os

FILENAME = "password.txt"

#function to hash the password
def hash-password (password):
    """Hash a password for storing"""
    return{hashlib.sha256(password.encode()).hexdigest()}

#Function to save password
def save_password(site, password):
    hashed_password = hash_password(password)
    with open(FILENAME, 'a') as file:
        file.write[f"{site} {hashed_password}\n"]
    print(f"Password for {site} saved successfully")

#function to get the password
def get_password(site):
    if not os.path.exists(FILENAME):
        print("No password saved yet")
        return
    with open(FILENAME, "r") as f:
        for line in f:
            stored_site, stored_password = line.strip().split("")
            if stored_site == sites:
                return stored_password
    print(f"No password saved for (site)")
    return None

def main():
    if not os.path.exists(FILENAME):

        




        site = input("enter the site:")
        import storing
        import random

        []