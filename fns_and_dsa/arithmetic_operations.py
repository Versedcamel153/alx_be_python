def perform_operation(num1, num2, operation):
    
    if operation=='add':
        result = num1 + num2
    elif operation=='subtract':
        result = num1 - num2
    elif operation =='multiply':
        result = num1 * num2
    elif operation =='divide':
        try:
            result = num1 / num2
            if num2 == 0:
                print("Error! cannot divide by zero")
        except ZeroDivisionError:
            result = float('inf')
        
    
    return result


