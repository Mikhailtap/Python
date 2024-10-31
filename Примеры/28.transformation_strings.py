import unicodedata
s='РЖД'
print('\nRed string:', s)
print('Type:', type(s), '\tlenght:', len(s))
s=s.encode('utf-8')
print('\nEncoded string:', s)
print('Type:', type(s), '\tlenght:', len(s))
s=s.decode('utf-8')
print('\nDecoded string:', s)
print('Type:', type(s), '\tlenght:', len(s))
for i in range(len(s)):
    print(s[i], unicodedata.name(s[i]), sep=' : ')
s=b'Gr\xc3\xb6n'
print('\nGreen string:', s.decode('utf-8'))
#s='Gr\N{LATIN SMALL LETTER 0 WITH DIAERESIS}n'
#print('Green string:', s)
#кароче, весело. Будет нужно - гугли че такое закомменчено