def lstSquare(n):
    def gen_list(i):
        if i > n:
            return []
        return [i] + gen_list(i + 1)
    return list(map(lambda x: x**2, gen_list(1)))

print(lstSquare(3))