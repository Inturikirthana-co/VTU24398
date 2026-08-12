def calculator(a, b, operation):
    operation = operation.lower().strip()

    if operation in ["add", "addition", "plus"]:
        return a + b

    elif operation in ["subtract", "subtraction", "minus"]:
        return a - b

    elif operation in ["multiply", "multiplication", "times"]:
        return a * b

    elif operation in ["divide", "division"]:
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    else:
        return f"Unsupported operation: {operation}"