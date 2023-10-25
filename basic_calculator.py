num = float(input("Enter the starting number: "))
done = False


while(not done):
    funct = input("Enter math function ('+', '-', '/', '*'): ")
    num2 = float(input(f"Enter number2 to {funct}: "))
    if funct=='+':
        num+=num2
    elif funct=='-':
        num-=num2
    elif funct=='/':
        num/=num2
    elif funct=='*':
        num*=num2
    else:
        print("You entered an invalid function! Try again")
        continue
    print(f"The number is now {str(num)}")
    done = input("To continue with another mathematical function, type 'continue', to end, type anything else: ") != 'continue'
print(f"The final number is {num} ")