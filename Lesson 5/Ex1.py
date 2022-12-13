# Написать функцию, принимающую строку-пароль. 
# Функция должна проверить подходит ли этот пароль условиям и вернуть True - если подходит; False - если не подходит. Условия:
# Должен быть не менее 6 символов;
# Должен содержать хотя бы одну цифру;
# Не должен состоять только из цифр;
# Не должен содержать слово “password” в любом регистре.

password = input("Enter you password: ")

def passwordCheck(passwrd): 

    checkLength = 0         # The flag is raised when the length is more than 5 symbols
    checkDigit = 0          # The flag is raised when there is even one digit
    checkNotAllDigit = 0    # The flag is raised when there are other symbols (not only digits)
    checkPasswd = 0         # The flag is raised when the password is not "password"

    if len(passwrd) > 5:
        checkLength = 1

    for i in range(len(passwrd)):
        if passwrd[i].isdigit():
            checkDigit = 1

    if passwrd.isnumeric() == False:
        checkNotAllDigit = 1

    if passwrd.lower() != "password":
        checkPasswd = 1

    if checkLength == 1 and checkDigit == 1 and checkNotAllDigit == 1 and checkPasswd == 1:
        return True
    else:
        return False

print(passwordCheck(password))
