def foo():
    a = 10
    return 20

@dec1
def bar():
    b = 'hello'
    return 30

@dec1
@dec2()
@dec3('hello')
def foobar():
    k = {'a': 'b'}
    return k
