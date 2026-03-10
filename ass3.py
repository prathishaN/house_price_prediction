#int to other data types
a=10
print(a, type(a))
b=float(a)
print(b, type(b))
c=complex(a)
print(c, type(c))
d=bool(a)
print(d, type(d))
e=str(a)
print(e, type(e))
l=list(a)
print(l, type(l))#list type error
s=set(a)
print(s, type(s))#set type error
t=tuple(a)
print(t, type(t))#tuple type error
d=dict(a)
print(d, type(d))#dict type error

#float to other data type

a=10.4
print(a, type(a))
b=int(a)
print(b,type(b))
c=complex(a)
print(c, type(c))
d=bool(a)
print(d, type(d))
s=str(a)
print(s, type(s))
l=list(a)           #list type error
print(l, type(l))
s=set(a)            #set type error
print(s, type(s))
d=dict(a)           #dict type error
print(d, type(d))
t=tuple(a)          #tuple type error
print(t, type(t))

#complex to other data types
c = 3 + 4j
print(c, type(c))
print(str(c), type(str(c)))
print(bool(c), type(bool(c)))
print(int(c), type(str(c)))     #int type error
print(float(c), type(bool(c)))  #float type error
print(list(c), type(str(c)))    #list type error
print(set(c), type(bool(c)))    #set type error
print(dict(c), type(str(c)))    #dict type error
print(tuple(c), type(bool(c)))  #tuple type error


#boolean to other data type
b = True
print(b, type(b))
print(int(b), type(int(b)))
print(float(b), type(float(b)))
print(str(b), type(str(b)))
print(complex(b), type(complex(b)))
print(list(b), type(list(b)))       #list type error
print(tuple(b), type(tuple(b)))     #tuple type error
print(set(b), type(set(b)))         #set type error
print(dict(b), type(complex(b)))    #dict type error

#string to other data type

s = "123"
print(s, type(s))
print(int(s), type(int(s)))
print(float(s), type(float(s)))
print(bool(s), type(bool(s)))
print(list(s), type(list(s)))
print(tuple(s), type(tuple(s)))
print(set(s), type(set(s)))
print(complex(s), type(complex(s)))
print(dict(s), type(dict(s)))   #dict type error


#list into other data types
lst = [1, 2, 3]
print(tuple(lst), type(tuple(lst)))
print(set(lst), type(set(lst)))
print(str(lst), type(str(lst)))
print(bool(lst), type(bool(lst)))
print(int(lst), type(int(lst))) #int type error
print(float(lst), type(float(lst)))#float type error
print(bool(lst), type(bool(lst)))#bool type error
print(complex(lst), type(complex(lst)))#complex type error

#set into other data types

st = {7, 8, 9}
print(list(st), type(list(st)))
print(tuple(st), type(tuple(st)))
print(str(st), type(str(st)))
print(bool(st), type(bool(st)))
print(dict(st), type(dict(st))) #dict type error
print(int(st), type(int(st)))   #int type error
print(float(st), type(float(st)))#float type error
print(complex(st), type(complex(st)))#complex type error


#dict into other datatype (it converts key only)
d = {"a": 1, "b": 2}
print(list(d), type(list(d)))
print(tuple(d), type(tuple(d)))
print(set(d), type(set(d)))
print(str(d), type(str(d)))
print(bool(d), type(bool(d)))
print(int(d), type(int(d))) #int type error
print(complex(d), type(complex(d)))#complex type error
print(float(d), type(float(d))) #float type error

#tuple into other data type

t = (4, 5, 6)
print(list(t), type(list(t)))
print(set(t), type(set(t)))
print(str(t), type(str(t)))
print(bool(t), type(bool(t)))
print(dict(t), type(dict(t)))   #dict type error
print(int(t), type(int(t))) #int type error
print(float(t), type(float(t)))#float type error
print(complex(t), type(complex))#complex type error


















