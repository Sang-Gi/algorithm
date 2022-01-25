shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    temp_menus = set(menus) # 중복 제거하면서 메뉴 정렬

    for i in orders:
        if i not in temp_menus:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)