# global var: menu_list: list, order: list, total_price: int:
# add_order(), outof_order()


menu_list = ["coffee", "latte", "tea"]
menu_price = [2500, 3000, 3000]
dic_menu_list = {'coffee': 2500, 'latte': 3000, 'tea': 3000}
order = list()
total_price = 0


def add_order(menu, count):
    global dic_menu_list, menu_list, menu_price, order, total_price
    jumunlist = list()
    jumunlist.append(menu)
    jumunlist.append(count)
    order.append(jumunlist)
    total_price += (count * dic_menu_list[menu])


def outof_menu(menu):
    global dic_menu_list, menu_list, menu_price, order, total_price
    if menu == "coffee" or menu == "latte" or menu == "tea":
        return False
    else:
        return True


while True:
    jumun = input('주문하실래요? yes/no: ')
    if jumun == 'no':
        print(f'주문내역: {order}\n주문총액:{total_price}')
        break
    elif jumun == 'yes':
        menu = input('메뉴) coffee, latte, tea 중 선택: ')
        if outof_menu(menu) == False:
            gaesoo = int(input('해당 메뉴 개수)'))
            add_order(menu, gaesoo)
        else:
            print('잘못된 메뉴를 입력하셨습니다.')
            continue
    else:
        print('yes나 no로만 답해주세요')