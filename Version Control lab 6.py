if __name__ == "__main__":
    remain=True
    while remain == True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        user_choice=input("Please enter an option: ")
        #My individual code
        if user_choice == "1":
            password=(input("Please enter your password to encode: "))
            encoded_password=""
            for num in password:
                if num == "0" or num == "1"or num == "2"or num == "3"or num == "4"or num == "5"or num == "6":
                    encoded_password+=str(int(num)+3)
                elif num == "7":
                    encoded_password+="0"

                elif num == "8":
                    encoded_password+="1"

                elif num == "9":
                    encoded_password+="2"

                else:
                    pass
            print("Your password has been encoded and stored!")
            print("")


        #Partner code
        elif user_choice == "2":
            pass




        elif user_choice == "3":
            remain = False