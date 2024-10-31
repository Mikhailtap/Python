s = input ().split ()
s1 = ''
for i in range (len (s)):
    s[i] = s[i][::-1]
    s1 += s[i]
    s1+=' '
print (s1[:-1])