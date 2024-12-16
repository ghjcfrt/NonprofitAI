try:
    pass
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)


def test(a: int, b: int, *, up: bool) -> int:
    if up:
        return a + b
    return a - b


foo = False
print(test(10, 5, up=foo))
