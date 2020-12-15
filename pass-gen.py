import secrets
import string

def passwd_gen(passwd_len):

    characters = string.ascii_letters + string.digits

    secure_passwd = ''.join(secrets.choice(characters) for i in range(passwd_len))

    return secure_passwd

def main():

    user_passwd_len = int(input("Input number of digits for password: "))

    print("Password Generated: ", password_gen(user_passwd_len))

main()
