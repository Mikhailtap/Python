from re import*
pattern=\
compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
def get_address():
    address=input('Enter your mail address: ')
    is_valid=pattern.match(address)
    if is_valid: #проверяет на корректность введенные данные (валидность)
        print('Valid address:', is_valid.group())
    else:
        print('Invalid address! Please retry...\n')
get_address()