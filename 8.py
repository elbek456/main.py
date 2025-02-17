# 1-masalla
#
# list_1: list = [2, 5, 67, 66, 78, 23, 56, 78, 90, 101]
#
# toq_sonlar = list(filter(lambda n1: n1 % 2 != 0, list_1))
#
# juft_sonlaer = list(filter(lambda n2: n2 % 2 == 0, list_1))
#
# print("juft sonlar", juft_sonlaer)
# print("toq sonlar", toq_sonlar)
#


# 2-masalla
# list_1 = ['Elbek', 'sovun', 'sovuq', 'yomgir', 'qor', 'gular', 'daraxt', 'dacha', 'xonadon',
#           'asal', 'magazin', 'non', 'momaqaldiroq', 'ariq', 'chelak', 'ayiq', 'sumka',
#           'gugurt', 'chang', 'arvox']
#
# filter_list = list(filter(lambda x: len(x) >= 5, list_1))
#
# capitalized_list = list(filter(lambda x: x.lower(), filter_list))
#
#
# print("5 va undan ortiq harflar:")
# print(filter_list)


# 3-masalla
# list_1 = ['Elbek', 'sovun', 'sovuq', 'yomgir', 'Qor', 'gular', 'daraxt', 'dacha', 'xonadon',
#           'asal', 'Magazin', 'non', 'momaqaldiroq', 'Ariq', 'chelak', 'ayiq', 'sumka',
#           'gugurt', 'chang', 'arvox']
#
# katta_harf = list(filter(lambda x: x[0].isupper(), list_1))
#
# print(katta_harf)

# 4-masalla
# list_1 = ['Elbek', 'sovun', 'sovuq', 'yomgir', 'Qor', 'gular', 'daraxt', 'dacha', 'xonadon',
#           'asal', 'Magazin', 'non', 'momaqaldiroq', 'Ariq', 'chelak', 'ayiq', 'sumka',
#           'gugurt', 'chang', 'arvox']
#
# list_2 = sorted(list_1, key=lambda n1: len(n1))
# print(list_2)
# list_3 = sorted(list_1, key=lambda n1: len(n1), reverse=True)
# print(list_3)


# 5-masalla
# numbers = [9, 6, 3, 4, 8, 7, 2, 5, 23, 34, 57, 89, 12, 35, 67, 90, 32, 65, 21, 94]
#
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
#
# n1 = even_numbers + odd_numbers
#
# print(n1)


# 6-masalla
# numbers = [9, 6, 3, 4, 8, 7, 2, 5, 23, 34, 57, 89, 12, 35, 67, 90, 32, 65, 21, 94]
#
# even_numbers = sorted(filter(lambda x: x % 2 == 0, numbers))
# odd_numbers = sorted(filter(lambda x: x % 2 != 0, numbers),)
#
# n1 = even_numbers + odd_numbers
#
# print(n1)


# 7-masalla
# list_1 = [9, 6, 3, 4.45, 8, 7, 2.68, 5, 23, 34, 57, 89, 12.5, 35, 67, 90.3, 32, 65, 21, 94]
#
# list_2 = list(map(lambda n1: n1 * 2, list_1))
# print(list_2)
#


# 8-masalla
# list_1 = ['Elbek', 'sovun', 'sovuq', 'yomgir', 'Qor', 'gular', 'daraxt', 'dacha', 'xonadon', 'asal']
#
# list_2 = list(map(lambda n1: n1.upper(), list_1))
#
# print(list_2)
#


# 9-masalla
# import random
#
# # 20 ta tasodifiy ballni yaratish (1 dan 5 gacha)
# oquvchilar = [random.randint(1, 5) for _ in range(20)]
# print("Boshida:", oquvchilar)
#
# n1 = list(map(lambda n2: n2 + 2 if n2 == 5 else n2, oquvchilar))
# print("Yangilangan:", n1)
