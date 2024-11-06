file=open('29.example.txt', 'w')
print('file name:', file.name)
print('file open mode:', file.mode)
print('readable:', file.readable())
print('writable', file.writable())
def get_status(f):
    if (f.closed != False):
        return 'Closed'
    else: return 'Open'
print('file status:', get_status(file))
file.close()
print('\nfile status:', get_status(file))