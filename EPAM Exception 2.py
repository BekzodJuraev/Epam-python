


def divide(str_with_ints):

    try:
        x = str_with_ints.split()
        a = int(x[0])
        b = int(x[1])
        return a / b
    except ZeroDivisionError:
        return "Error code: division by zero"
    except ValueError as e:
        return f"Error code: {e}"




print(divide('5  5'))
