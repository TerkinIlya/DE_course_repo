from collections import defaultdict

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(data: list[dict]) -> float:
    revenue = 0
    for dct in data:
        revenue += dct['price'] * dct['quantity']
    return revenue


def items_by_category(data: list[dict]) -> dict:
    res_dict = defaultdict(list)
    for dct in data:
        key = dct.get('category')
        value = dct.get('item')
        res_dict[key].append(value)
    return res_dict


def expensive_purchases(data: list[dict], min_price: float) -> list:
    res_list = []
    for dct in data:
        if dct.get('price') > min_price:
            res_list.append(dct)
    return res_list


def average_price_by_category(data: list[dict]) -> dict:
    res_dict = defaultdict(list)
    for dct in data:
        key = dct.get('category')
        value = dct.get('price')
        res_dict[key].append(value)
    for key, value in res_dict.items():
        res_dict[key] = sum(value) / len(value)
    return res_dict


def most_frequent_category(data: list[dict]) -> str:
    res_dict = defaultdict(int)
    for dct in data:
        key = dct.get('category')
        value = dct.get('quantity')
        res_dict[key] += value
    return max(res_dict, key=res_dict.get)


total_revenue = total_revenue(purchases)
items_by_category = dict(items_by_category(purchases))
min_price = 1.0
expensive_purchases = expensive_purchases(purchases, min_price)
average_price_by_category = dict(average_price_by_category(purchases))
most_frequent_category = most_frequent_category(purchases)


print(f'Общая выручка: {total_revenue}\n'
      f'Товары по категориям: {items_by_category}\n'
      f'Покупки дороже {min_price}: {expensive_purchases}\n'
      f'Средняя цена по категориям: {average_price_by_category}\n'
      'Категория с наибольшим количеством проданных товаров: '
      f'{most_frequent_category}')
