import re
def normalize_phone(phone_number):
    pattern = r'[^\d+]'
    repl = ""
    result = re.sub(pattern, repl, phone_number)
    if result[0:3] == '380':
        result = ''.join(['+',result])
    elif result[0]=='0':
           result = ''.join(['+38', result])
    return (result)
phone_number ='(095)123-4567\\n'
print(normalize_phone(phone_number))
        




