import logging
logging.basicConfig(filename="app.log")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("division failed")                  # version 1
        logging.exception("division failed")      # version 2
print(divide(10,0))