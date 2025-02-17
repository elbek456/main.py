# 1-misoll

# def merge_unique_ids(active_users: list, new_users: list) -> list:
#
#     unique_ids = list(set(active_users + new_users))
#
#     unique_ids.sort()
#     return unique_ids
#
#
# active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001']
# new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']
#
# result = merge_unique_ids(active_users, new_users)
# print(result)
# 2-misoll
# def sorted_by_prise(products: list) -> list:
#     return sorted(products, key=lambda x: int(x[1]), reverse=True)
#
#
# products = [
#     ("Olma", "12000", "5%"),
#     ("Banan", "5000", "10%"),
#     ("Gilos", "15000", "7%"),
#     ("Apelsin", "5000", "8%"),
#     ("Anor", "30000", "2%"),
#     ("Uzum", "7000", "9%"),
#     ("Tarvuz", "25000", "15%"),
#     ("Shalgil", "18000", "6%"),
#     ("Qovun", "4000", "25%"),
#     ("Qulupnay", "35000", "10%"),
# ]
#
# sorted_products = sorted_by_prise(products)
# for products in sorted_products:
#     print((products))

 # 3-misoll
# def are_numbers_ascending(text: str) -> bool:
#     numbers=[]
#     words = text.split()
#     for word in words:
#         if word.isdigit():
#             numbers.append(int(word))
#      return all(numbers[i]<numbers[i+1] for i in range(len(numbers)-1))
# print(are_numbers_ascending("1 qutida 5 ta yashil, 9 ta qizil, 12 ta sariq to’p bor edi"))
# print(are_numbers_ascending("musobaqada 5 ga 5 ko‘rinishda o‘yinlar o‘tkazildi"))
# print(are_numbers_ascending("26 o’quvchidan 3 tasi 5 baxo oldi"))
