from collections import Counter

def sepor(num=10):
    print("=" * num)

def print_chech(basket, summa):
    if not basket:
        print("Вы ушли без товара")
        return None
    
    print("*ЧЕК*")
    c = Counter(basket)
    sepor()
    [print (i,v,"шт.") for i,v in c.items()]
    sepor()
    print("Сумма", sum(summa))

def main():
    basket = []
    summa = []
    cash = 1000
    product_map = {"Хлеб":50,"Кофе":450,"Масло":200,"Пиво":100,\
            "Молоко":90,"Рыба":150,"Сок":100,"Кефир":100}

    while True:

        my_choise = input("Для выхода(печать чека) - q, для вызова цен - p," + 
            " для добавления продуктов в корзину - a: "
            "баланс - с: ")
        print("Список продуктов:", ", ".join(product_map.keys()))
        
        if my_choise == "q":
            print_chech(basket, summa)
            break
        elif my_choise == "p":
            [print(aa,bb) for aa,bb in product_map.items()]
        elif my_choise == "a":
            append_product = input("В магазине " + str(len(product_map)) \
            + " продуктов, добавлю в корзину: ".lower())

            if append_product in product_map:
                summa.append(product_map[append_product])
                basket.append(append_product)
                print("Продукт", append_product, "добавлен в корзину, баланс = ", \
                    cash - sum(summa))
            else:
                print("Нет такого товара!")
                continue
        elif my_choise == "c":
            print(cash - sum(summa))

        if cash < sum(summa):
            print("Денег больше нет!")
            print_chech(basket, summa)
            break

main()