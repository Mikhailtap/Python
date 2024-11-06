from clones_classes import*

chick=Bird('Cheep, cheep')
chick.age='1 week'
print('\nChick says:', chick.talk())
print('Chick age:', chick.age)
chick.age='2 weeks'
print('Chick now:', chick.age)
setattr(chick, 'age', '3 weeks')
print('\nChick attributes...')
for attrib in dir(chick):
    #print(attrib, ':', getattr(chick, attrib))
    if attrib[0] != '_': #имена атрибутов, предоставляемые интерпретатором
        #содержат символ "_", как частные
        print(attrib, ':', getattr(chick, attrib))
delattr(chick, 'age')
print('\nChick age attribute?', hasattr(chick, 'age'))