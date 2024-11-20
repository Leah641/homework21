# homework21

# start
print("I can solve ax^2+bx+c=0 for you!")

while True:
    try:
        #ask for correct coefficient
        a = float(input("Please give me the 'a' coefficient: "))
        b = float(input("Please give me the 'b' coefficient: "))
        c = float(input("Please give me the 'c' coefficient: "))
        delta = b**2 - 4*a*c  #check the roots are real

        if a == 0:  # a cannot be 0
            print("Sorry, but 'a' cannot be zero")

        elif delta < 0: # if delta < 0, there is no real root
            print("Sorry, but that quadratic does not have real roots.")

        elif delta == 0:  # so there will be two cases of answer
            print("Thank you, that is a valid input :) OKAY I'LL SOLVE IT NOW.")
            print("ROOT:", -b / 2*a)
            break

        else:
            print("ROOT 1:", (-b + delta**(1/2) / (2*a)))
            print("ROOT 2:", (-b - delta**(1/2) / (2*a)))
            break

    except:  #if it is not a number
        print("That is not a real number!")

quit()
