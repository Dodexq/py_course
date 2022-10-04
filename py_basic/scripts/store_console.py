#!/usr/bin/env python3

import sys

def get_argv():
    argv_products = [i for n, i in enumerate(sys.argv[1:]) if n%2 == 0]
    argv_price = [int(i) for n, i in enumerate(sys.argv[1:]) if n%2 != 0]
    return (argv_products, argv_price)

def sepor(num=10):
    print("=" * num)

def main():
    products, price = get_argv()
    print("  *ЧЕК*\n")
    sepor()
    for i, n in zip(products, price):
        print(i, n)
    sepor()
    print("\nКол-во продуктов:", len(products), "\nСумма:", sum(price))

main()