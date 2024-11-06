from clones_classes import*

zola=Bird('Beep, beep')
print('\nZola built-in instance attributes...')
for attrib in dir(zola):
    if attrib[0] == '_': 
        print(attrib)
print('\nClass dictionary...')
for item in Bird.__dict__:
    print(item, ':', Bird.__dict__[item])
    print('\nInstance dictionary...')
    for item in zola.__dict__:
        print(item, ':', zola.__dict__[item])