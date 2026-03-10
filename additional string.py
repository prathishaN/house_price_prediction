s = input("Enter a string: ")#prathisha
ch = input("Enter a character to count: ")#a
print("Count:", s.count(ch))#2

s="prathisha"
print(s.capitalize())#Prathisha

s = input("Enter a string: ")#prathisha,manisha
print("Title case:", s.title())#Prathisha,Manisha

num="23"
print(num.zfill(5))#00023

s = input("Enter a string: ")#prathisha
ch = input("Enter starting character: ")#p
print(s.startswith(ch))#true    Returns True if string starts with given character

s = input("Enter a string: ")#prathisha
ch = input("Enter ending character: ")#a
print(s.endswith(ch))#true

s = input("Enter a string: ")#prathisha
old = input("Enter word to replace: ")#prathi
new = input("Enter new word: ")#mani
print("Updated string:", s.replace(old, new))#manisha

s = input("Enter a string with spaces: ")
print("After strip:", s.strip())

s = input("Enter a string: ")#prathisha manisha
words = s.split()

print("List of words:", words)#['prathisha', 'manisha']
