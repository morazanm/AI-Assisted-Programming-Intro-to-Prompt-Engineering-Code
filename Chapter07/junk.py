def map(f, L):
    return [f(x) for x in L]

def filter(f, L):
    return [x for x in L if f(x)]

def foldl(f, acc, L):
    for x in L:
        acc = f(acc, x)
    return acc

def foldr(f, acc, L):
    for x in reversed(L):
        acc = f(x, acc)
    return acc

def andMap(f, L):
    return foldl(lambda x, acc: acc and f(x), L, True)

def orMap(f, L):
    return foldl(lambda x, acc: acc or f(x), L, False)

def compose(f, g):
    return lambda x: f(g(x))



def test_map():
    assert map(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert map(str, [1, 2, 3]) == ['1', '2', '3']