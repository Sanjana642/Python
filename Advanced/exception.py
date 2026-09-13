# exception = An event that interrupts the flow of the program 
# (ZeroDivisionError, TypeError, ValueError)
# 1.try 2.except 3.finally

# 1 / 0 - ZeroDivisionError: division by zero

# try:
    # try some code
# except Exception:
    # handle an exception
# finally:
    # do some cleanup
try:
    number = int(input("Enter a number: "))
    print(1 / number)   # for 0 zerodivisionerror 
except ZeroDivisionError:
    print("You can't divide by 0")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")