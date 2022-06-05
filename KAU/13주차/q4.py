def price(menu, count):
    order = list()
    menu_list = {'coffee': 2500, 'latte': 3000, 'tea': 3000}
    
    order.append(menu)
    order.append(count)

    total = menu_list[menu] * count

    print(f"주문내역: {order}")
    print(f"주문총액: {total}")



menu = input("메뉴) coffee, latte, tea 중에 선택: ")
count = int(input("해당 메뉴 개수) "))

price(menu, count)