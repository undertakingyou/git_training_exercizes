def concatenate(a: str, b: str) -> str:
    return a + ' ' + b

def repeat(a: str, b: int, spacer: str = None) -> str:
    result: str = ''

    for i in range(b):
        result += a
        if spacer and i != b - 1:
            result += spacer

    return result