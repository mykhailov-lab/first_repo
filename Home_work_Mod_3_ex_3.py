def normalize_phone(phone_number):
    import re
    r = phone_number.split('\n')
    new_number = []
    for i in r:
        pattern = r'[()\s\-"\']'
        repl = ""
        result = re.sub(pattern, repl, i)
        if result[0:3] == '380':
            result = ''.join(['+',result])
        elif result[0]=='0':
           result = ''.join(['+38', result])
        new_number.append(result)
    return (new_number)
phone_number = """    +38(050)123-32-34"
"     0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11   """
print(normalize_phone(phone_number))
        




