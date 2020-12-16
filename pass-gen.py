#!/usr/bin/env python3
import secrets
import string

def passwd_gen(passwd_len):

    allchr = string.ascii_letters + string.digits + string.punctuation

    encrp_passwd = ''.join(secrets.choice(allchr) for i in range(passwd_len))

    return encrp_passwd

def main():

    passwd_len = int(input("Input Length password: "))

    print("Password Generated: ", passwd_gen(passwd_len))

main()
