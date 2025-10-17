def unit_conversion():
    while True:
        print("\n unit conversion unit")
        print("1. kms to miles")
        print("2. miles to kms")
        print("3. fehrits to celcius")
        print("4. celcius to fehrits")
        print("5. pounds to kg")
        print("6. kg to pounds")
        print("7. exit")

        choice = input(" select any number between (1-7):)")

        if choice == '1':
            km = input("enter distance in kms:")
            miles = km * 0.62
            print("miles")
        
        elif choice == '2':
            miles = input("enter distance in miles: ")
            km = miles * 1.60
            print("km")

        elif choice == '3':
            fehrits = input(" enter teperature in fehrits:")
            celcius = (fehrits-32)*0.56
            print("celcius")

        elif choice == '4':
            celcius = input("enter temperature in  celcius:")
            fehrits = (celcius*9/5)+32
            print("fehrits")

        elif choice == '5':
            pounds = input("enter weight in pounds:")
            kg = pounds*0.45
            print("kg")

        elif choice == '6':
            kg = input("enter weight in kg:")
            pounds = kg*2.20
            print("pounds")

        elif choice == '7':
            print("exiting calcuylator SEE YOU")

        else :
            print("enter any number between 1 and 7")

