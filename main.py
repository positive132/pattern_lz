from pattern import Singleton, TV, Radio, Remote, Book, Fruit, PriceCalculator

def main():
    s1 = Singleton()
    s2 = Singleton()
    print("Одиночка работает:", s1 is s2)

    tv_remote = Remote(TV())
    radio_remote = Remote(Radio())
    print(tv_remote.press_button())
    print(radio_remote.press_button())

    items = [Book(2000), Fruit(4, 250)]
    calc = PriceCalculator()
    
    total = sum(item.accept(calc) for item in items)
    print("Итоговая стоимость со скидками:", total)

if __name__ == "__main__":
    main()
