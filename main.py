# The objective of this lab is to understand the purpose and usefulness of
# version control. You will work in a group of two. You will write a
# simplified password encoder/decoder program and practice the
# functions of version control systems to develop familiarity with them.


def encode():
    password = input("Please enter your password to encode: ")
    result = ""
    for i in range(0, len(password)):
        num = int(password[i])
        num += 3
        if num >= 10:
            num -= 10
            result = result + str(num)
        else:
            result = result + str(num)
    return result


def decode(password):
    result = ""
    for i in str(password):
        result += str(int(i)+17)[-1]
    return result


def main():
    encoded = ""
    decoded = ""
    while True:
        print(f"\nMenu \n-------------")
        print(f"1. Encode \n2. Decode \n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            encoded = encode()
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")
        elif option == 3:
            quit()
        else:
            print("Error, try again")


if __name__ == '__main__':
    main()
