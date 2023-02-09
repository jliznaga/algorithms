def is_balanced_expression(expression):
    open_symbols = ["[", "{", "("]
    close_symbols = ["]", "}", ")"]
    stack = []
    for item in expression:
        if item in open_symbols:
            stack.append(item)
        elif item in close_symbols:
            pos = close_symbols.index(item)
            if len(stack) > 0 or open_symbols[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return False
    return True
