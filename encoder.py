# The password encoder should take in an 8-digit password in string
# format containing only integers. After passing the password into
# the encoder, the encoder stores the encoded password to a new
# variable, with each digit being shifted up by 3 numbers.


def main():
    password = input("Enter password: ")
    for i in range(0, len(password)):
        num = int(password[i])
        num += 3
        if num >= 10:
            num -= 10
            print(f"{num}", end="")
        else:
            print(f"{num}", end="")


if __name__ == '__main__':
    main()
