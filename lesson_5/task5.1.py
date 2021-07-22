def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i

odd_to_4 = odd_nums(12)
for n in range(13 // 2 + 1):
    print(next(odd_to_4))
