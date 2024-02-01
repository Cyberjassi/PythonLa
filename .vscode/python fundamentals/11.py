# prime or not


S = True

number = int(input("Enter a no. for check prime or not:"))
while S:
        for i in range(2,number):
            if number%i == 0:
                print(f"Not a Prime no.")
                break
            else:
                print(f"Prime no.")
                break
        again = input("Again want to check(yes/no)")
        if(again == 'yes'):
             number = int(input("Enter a no. for check prime or not:"))
        else:
           S = False

