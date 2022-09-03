def fib(n):
    f_n_2 = 0
    f_n_1 = 1
    for _ in range(n):
        f_n_1, f_n_2 = f_n_1 + f_n_2, f_n_1
        yield f_n_2

gen1 = fib(100)
gen2 = fib(10)

for i in gen1:
    print(i)

print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))

def gen2():
    yield from range(0,100,20)

for i in gen2():
    print(i)

