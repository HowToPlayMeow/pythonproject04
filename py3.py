def funcA( ) :
    print('AAA')
    print('BBB')
    return ' WOW Meow'

def funcB( ) :
    return 999,True, 10 + 20

print( funcA( ) )
x = funcA

a, b, c = funcB
print(f'{a} {b} {c}')