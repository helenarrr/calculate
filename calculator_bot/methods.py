def parse(text):
    result = []
    digit = ''
    for symbol in text:         #  '1+1'
        if symbol.isdigit():
            digit += symbol     # digit = '1'
        else:
            result.append(int(digit))  # result = [1]
            digit = ''                 # digit = ''
            result.append(symbol)      # result = [1, '+', 1]
    else:
        if digit:
            result.append(int(digit))
    return result


def calculate(lst):
    result = 0.0
    for s in lst:
        if s == '*' or s == '/':
            if s == '*':
                index = lst.index(s)
                result = lst[index - 1] * lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index - 1] / lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
    for s in lst:
        if s == '+' or s == '-':
            if s == '+':
                index = lst.index(s)
                result = lst[index - 1] + lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index - 1] - lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result
