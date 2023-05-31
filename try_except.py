try:
    num1 = int(input("Enter a value:"))
    num2 = int(input("Enter a value:"))
    ans = num1 / num2
    print(ans)
except ZeroDivisionError:
    print("Second value can not be Zero")
except ValueError:
    print("Not a valid input")
except: 
    print("Any Other error")
finally:
    print("Finally block")