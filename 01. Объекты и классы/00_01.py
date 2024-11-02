# -----------------------------------------
x = None
y = None

print( f'{type(x)=}')
print( f'{id(x)=}, {id(y)=}' )
print( f'x == y -> {x == y}' )
print( f'x is y -> {x is y}' )
print('='*60)

# -----------------------------------------
x = 42
y = 42

print( f'{type(x)=}')
print( f'{id(x)=}, {id(y)=}' )
print( f'x == y -> {x == y}' )
print( f'x is y -> {x is y}' )
print('='*60)

# -----------------------------------------
x = 257
y = 257

print( f'{type(x)=}')
print( f'{id(x)=}, {id(y)=}' )
print( f'x == y -> {x == y}' )
print( f'x is y -> {x is y}' )
print('='*60)

# -----------------------------------------
x = 1007024
y = 1007024

print( f'{type(x)=}')
print( f'{id(x)=}, {id(y)=}' )
print( f'x == y -> {x == y}' )
print( f'x is y -> {x is y}' )
print('='*60)

# -----------------------------------------
a = 'some sting'
b = 'some sting'

print( f'{type(a)=}')
print( f'{id(a)=}, {id(b)=}' )
print( f'a == b -> {a == b}' )
print( f'a is b -> {a is b}' )
print('='*60)

import sys
a = sys.intern('come string')
b = sys.intern('come string')
print( f'{id(a)=}, {id(b)=}' )


# -----------------------------------------
a = [1,2,3]
b = [1,2,3]

print( f'{type(a)=}')
print( f'{id(a)=}, {id(b)=}' )
print( f'a == b -> {a == b}' )
print( f'a is b -> {a is b}' )
print('='*60)

