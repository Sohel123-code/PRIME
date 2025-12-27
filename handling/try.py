try:
    n=int(input("enter any number : "))
    div=10/n

except ZeroDivisionError:
    print("enter valid number, zero is not allowed")

except ValueError:
    print("enter a valid integer")

else:
    print(f"answer is {div}")

finally :
    print("this program is executed")

