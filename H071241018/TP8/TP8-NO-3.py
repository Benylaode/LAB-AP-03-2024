import re

def handleInput(inputaAlif, tipe):
    while True:
        try:
            inputField = tipe(input(inputaAlif))
            return inputField
        except:
            print("Input tidak sesuai")

usernamePattern = r'^(?=.*[A-Za-z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]{5,20}$'
emailPattern = r'^[a-z]+([0-9]{2,})?@[example]+\.(com|co.id)$'
passwordPattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*()_+])[A-Za-z0-9@#$%^&*()_+]{8,}$'

def tampilkanError(field):
    print()
    print(f"{field} yang kamu input tidak valdi. Registrasi gagal!")

def main():
    username = handleInput("Masukkan username: ", str)

    if not re.match(usernamePattern, username):
        tampilkanError("Username")
        return
    else:
        email = handleInput("Masukkan email: ", str)
    
    if not re.match(emailPattern, email):
        tampilkanError("Email")
        return
    else:
        password = handleInput("Masukkan password: ", str)

    if not re.match(passwordPattern, password):
        tampilkanError("Password")
        return
    else:
        print()
        print(f"Registrasi berhasil! Selamat datang, {username}")

main()