def concatenate(a: str, b: str) -> str:
    return a + ' ' + b

def repeat(a: str, b: int) -> str:
    results: str = ''
    for i in range(b):
        results += a

    return results
