astring = "Hello world!"
astring = 'hello world!'

print("a single quote is here ' '")
print(len(astring))
print(astring +" .capitalize() => "+astring.capitalize())
print(astring + " .index('wor') => %d " % astring.index('wor'))
print(astring + " .count('l') => %d " % astring.count('l'))

astring = 'abcdefghijklmnop'
print(astring + " [1:7] => %s " % astring[1:7])
print(astring + " [1:8:2] => %s " % astring[1:8:2])
print(astring + " [::-1] => %s " % astring[::-1])

astring = 'AbcdefghijklmnoP'
print("%s upper %s" % (astring, astring.upper()))
print("%s lower %s" %  (astring, astring.lower()))

print("%s start with %s %s" % (astring, 'Abc', astring.startswith('Abc')))
print("%s end with %s %s" %  (astring, 'dsd', astring.endswith('dsd')))

astring = "Hello World"
print("%s split to %s" % (astring, astring.split(" ")))