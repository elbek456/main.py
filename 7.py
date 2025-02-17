# 1-misoll
# list_1: list = [1, 2, 2, 3, 3, 3, 4, 5, 4, 6, 7, 8, 6, 7, 9]
#
# set_1 = {}
#
# for son in list_1:
#     set_1[son] = set_1.get(son, 0) + 1
#
# natija = {son for son, soni in set_1.items() if soni == 1}
#
# print("Natija:", list(natija))



# 2-massala
# nomzodlar = [
#     {"ism": "Ali", "tajriba": 1, "loyihalar": 4},
#     {"ism": "Vali", "tajriba": 1, "loyihalar": 3},
#     {"ism": "Anvar", "tajriba": 2, "loyihalar": 2},
#     {"ism": "Dilnoza", "tajriba": 1, "loyihalar": 4},
#     {"ism": "Zuhra", "tajriba": 1, "loyihalar": 5},
#     {"ism": "Shavkat", "tajriba": 4, "loyihalar": 1},
#     {"ism": "Malika", "tajriba": 1, "loyihalar": 2},
#     {"ism": "Elbek", "tajriba": 2, "loyihalar": 5},
#     {"ism": "Iroda", "tajriba": 1, "loyihalar": 3},
#     {"ism": "Bobur", "tajriba": 1, "loyihalar": 4},
# ]
#
# set_1 = set()
#
# for nomzod in nomzodlar:
#     if nomzod['tajriba'] >= 2 and nomzod['loyihalar'] >= 5:
#         set_1.add(nomzod['ism'])
#
# print("mos nomzod:", set_1)



# 3-misol
# nomzodlar = [
#     {"ism": "Ali", "tajriba": 1, "loyihalar": 4},
#     {"ism": "Vali", "tajriba": 1, "loyihalar": 3},
#     {"ism": "Anvar", "tajriba": 2, "loyihalar": 2},
#     {"ism": "Dilnoza", "tajriba": 6, "loyihalar": 5},
#     {"ism": "Zuhra", "tajriba": 1, "loyihalar": 5},
#     {"ism": "Shavkat", "tajriba": 4, "loyihalar": 1},
#     {"ism": "Malika", "tajriba": 1, "loyihalar": 2},
#     {"ism": "Elbek", "tajriba": 3, "loyihalar": 7},
#     {"ism": "Iroda", "tajriba": 2, "loyihalar": 3},
#     {"ism": "Bobur", "tajriba": 1, "loyihalar": 4},
# ]
#
# set_1 = set()
#
# for nomzod in nomzodlar:
#     if nomzod['tajriba'] > 2 and nomzod['loyihalar'] > 5:
#         set_1.add(nomzod['ism'])
#
# print("mos nomzod:", set_1)


# 4-masala
# odamlar_1 = {'Raxmatilo', 'Kamolidin', 'Madina', 'Mexroj', 'Nigor', 'Elbek', 'Asad', 'Javlon'}
#
# taklif_q = input("isim kiriting")
#
# if taklif_q in odamlar_1:
#     odamlar_1.remove(taklif_q)
#     print("Xush kelibsiz:")
# else:
#     print(f"{taklif_q} taklif qilinmagan!")


# 5-masala
# istmasi_borlar = {'Elbek', 'Xudoyberdi', 'Olim', 'Kamolidin'}
# kozi_qzarganlar = {'Elbek', 'Madina', 'Mexroj', 'Nafisa'}
# boshqa_bemorlar = {'Elbek', 'Xudoyberdi', 'Mexroj', 'Kamolidin'}
#
#
# umumiy_bemorlar= istmasi_borlar &kozi_qzarganlar &boshqa_bemorlar
#
# print("Hamma joyi nosog'lom bemor:",umumiy_bemorlar)


# 6-masala
# talaba = {"ismi": "Elbek", "familiyasi": "Umaraliyev", "yoshi": 20}
#
# talaba["manzil"] = "Toshkent"
#
# del talaba['yoshi']
# print(talaba)


# 7-masala
# dict_1: dict = {"a": "nimadur", "b": "yana nimadur"}
# dict_2: dict = {"c": "kimdur", "d": "nima yozishni bilmadim"}
#
# dict_1.update(dict_2)
#
# print(dict_1)


# 8=misoll
# matn=input("matn kriting:")
#
# harflar_soni={}
#
# for harf in matn:
#     if harf in harflar_soni:
#         harflar_soni[harf]+=1
#     else:
#         harflar_soni[harf]=1
#
#
# print("xarflar soni:", harflar_soni)

