from clones_classes import*
print('\nClasses instances of:\n', Bird.__doc__)
polly=Bird('Squawk, squawk!') #это chat
print('\nNumber of  birds:', polly.count)
print('Polly says:', polly.talk())
harry=Bird('Tweet, tweet!')
print('\nNumber of  birds:', harry.count)
print('Harry says:', harry.talk())