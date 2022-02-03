shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 정렬해야함.
# 최대 할인율 = 최대금액 * (1 - 최대쿠폰 * 0.01)

def get_max_discounted_price(prices, coupons):
    prices_idx = 0
    coupons_idx = 0
    max_discount = 0

    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    while prices_idx < len(shop_prices) and coupons_idx < len(user_coupons):
        max_discount += prices[prices_idx] * (100 - coupons[coupons_idx]) / 100
        prices_idx += 1
        coupons_idx += 1
    
    while prices_idx < len(shop_prices):
        max_discount += prices[prices_idx]
        prices_idx += 1
    
    return max_discount


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.