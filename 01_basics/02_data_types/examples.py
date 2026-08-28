# ? ============================================================
# ? Python Data Types
# ? ============================================================
x = "Hello World"	#str	
print(type(x))	#<class 'str'>
x = 20	#int	
print(type(x))	#<class 'int'>
x = 20.5	#float	
print(type(x))	#<class 'float'>
x = 1j	#complex	
print(type(x))	#<class 'complex'>
x = ["apple", "banana", "cherry"]	#list	
print(type(x))	#<class 'list'>
x = ("apple", "banana", "cherry")	#tuple	
print(type(x))	#<class 'tuple'>
x = range(6)	#range	
print(type(x))	#<class 'range'>
x = {"name" : "John", "age" : 36}	#dict	
print(type(x))	#<class 'dict'>
x = {"apple", "banana", "cherry"}	#set	
print(type(x))	#<class 'set'>
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
print(type(x))	#<class 'frozenset'>
x = True	#bool	
print(type(x))	#<class 'bool'>
x = b"Hello"	#bytes	
print(type(x))	#<class 'bytes'>
x = bytearray(5)	#bytearray	
print(type(x))	#<class 'bytearray'>
x = memoryview(bytes(5))	#memoryview	
print(type(x))	#<class 'memoryview'>
x = None	#NoneType	
print(type(x))	#<class 'NoneType'>
