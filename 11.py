# from abc import ABC, abstractmethod
#
# 1-misoll
#
# class IshchiABC(ABC):
#     def __init__(self, id, ism, familiya, maosh):
#         self.id = id
#         self.ism = ism
#         self.familiya = familiya
#         self.maosh = maosh
#
#     @abstractmethod
#     def maosh_oshirish(self, foiz):
#         pass
#
#     def toliq_ism_olish(self):
#         return f"{self.ism} {self.familiya}"
#
#     def yillik_maosh(self):
#         return self.maosh * 12
#
#
# class Ishchi(IshchiABC):
#     def maosh_oshirish(self, foiz):
#         if foiz < 0:
#             raise ValueError("Foiz manfiy bo'lishi mumkin emas!")
#         self.maosh += self.maosh * foiz // 100
#
#
# ishchi = Ishchi(632322, "Elbek", "Umaraliyev", 5000)
# ishchi.maosh_oshirish(10)
# print("Ishchi:", ishchi.toliq_ism_olish(), "Yillik maosh:", ishchi.yillik_maosh())
#
# 2-misoll
#
# class AylanaABC(ABC):
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_circumference(self):
#         pass
#
#
# class Aylana(AylanaABC):
#     def get_area(self):
#         return 3.14 * self.radius * self.radius
#
#     def get_circumference(self):
#         return 2 * 3.14 * self.radius
#
#
# doira = Aylana(5, "Ko'k")
# print("Aylana yuzasi:", doira.get_area(), "Aylana uzunligi:", doira.get_circumference())
#
# 3-misoll
#
# class RectangleABC(ABC):
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
#
# class Rectangle(RectangleABC):
#     def get_area(self):
#         return self.height * self.width
#
#     def get_perimeter(self):
#         return 2 * (self.height + self.width)
#
#
# tortburchak = Rectangle(5, 10)
# print("To'rtburchak yuzasi:", tortburchak.get_area(), "Perimetri:", tortburchak.get_perimeter())
#
# 4-misoll
#
# class AccountABC(ABC):
#     def __init__(self, id, name, balance=0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     @abstractmethod
#     def credit(self, amount):
#         pass
#
#     @abstractmethod
#     def debit(self, amount):
#         pass
#
#
# class Account(AccountABC):
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def debit(self, amount):
#         if amount > self.balance:
#             print("Amount exceeded balance")
#         else:
#             self.balance -= amount
#         return self.balance
#
#
# account1 = Account("001", "Elbek", 500)
# account2 = Account("002", "Raxmatilo", 300)
# account1.credit(200)
# print("Yangi balans:", account1.balance)
#
# 5-misoll
#
# class DateABC(ABC):
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @abstractmethod
#     def toString(self):
#         pass
#
#
# class Date(DateABC):
#     def toString(self):
#         return f"{self.day:02}/{self.month:02}/{self.year}"
#
#
# date = Date(31, 12, 2025)
# print("Hozirgi sana:", date.toString())
#
#
# 6-misol
#
#
# class TimeABC(ABC):
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     @abstractmethod
#     def nextSecond(self):
#         pass
#
#
# class Time(TimeABC):
#     def nextSecond(self):
#         self.second += 1
#         if self.second == 60:
#             self.second = 0
#             self.minute += 1
#             if self.minute == 60:
#                 self.minute = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0
#         return self
#
#     def toString(self):
#         return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
#
#
# time = Time(23, 59, 59)
# time.nextSecond()
# print("Keyingi soniya:", time.toString())
#
#
# 7-misol
#
# class KitobABC(ABC):
#     def __init__(self, muallif, nomi, betlar, narx, nashr_yili):
#         self.muallif = muallif
#         self.nomi = nomi
#         self.betlar = betlar
#         self.narx = narx
#         self.nashr_yili = nashr_yili
# 
#     @abstractmethod
#     def malumot_korsat(self):
#         pass
#
#
# class Kitob(KitobABC):
#     def malumot_korsat(self):
#         print(f"Muallif: {self.muallif}, Kitob nomi: {self.nomi}, Betlar soni: {self.betlar}, Narxi: {self.narx}, Nashr yili: {self.nashr_yili}")
#
#
# yangi_kitob = Kitob("Umaraliyev Elbek", "Python dasturi", 550, 45.67, 2020)
# yangi_kitob.malumot_korsat()


# 1-misol
# from abc import ABC, abstractmethod
#
# class Kitob(ABC):
#     def __init__(self, nomi, muallif, nashr_yili):
#         self.nomi = nomi
#         self.muallif = muallif
#         self.nashr_yili = nashr_yili
#
#     @abstractmethod
#     def malumot(self):
#         pass
#
#
# class BadiiyKitob(Kitob):
#     def __init__(self, nomi, muallif, nashr_yili, janr):
#         super().__init__(nomi, muallif, nashr_yili)
#         self.janr = janr
#
#     def malumot(self):
#         return f"Nomi: {self.nomi}, Muallif: {self.muallif}, Nashr yili: {self.nashr_yili}, Janr: {self.janr}"
#
#
# class IlmiyKitob(Kitob):
#     def __init__(self, nomi, muallif, nashr_yili, yonalish):
#         super().__init__(nomi, muallif, nashr_yili)
#         self.yonalish = yonalish
#
#     def malumot(self):
#         return f"Nomi: {self.nomi}, Muallif: {self.muallif}, Nashr yili: {self.nashr_yili}, Yo‘nalish: {self.yonalish}"
#
#
# kitob1 = BadiiyKitob("Sherlar", "Alisher Navoiy", 1492, "She'riyat")
# kitob2 = IlmiyKitob("Fizika asoslari", "Umaraliyev Elbek", 1687, "Fizika")
# print(kitob1.malumot())
# print(kitob2.malumot())
#
#
# # 2 - misol
# class Talaba(ABC):
#     def __init__(self, ism, yosh, id_raqam):
#         if yosh < 18:
#             raise ValueError("Talaba yoshi 18 dan kichik bo‘lishi mumkin emas!")
#         if not id_raqam.isdigit() or len(id_raqam) < 8:
#             raise ValueError("ID raqam kamida 8 ta raqamdan iborat bo‘lishi kerak!")
#         self.ism = ism
#         self.yosh = yosh
#         self.id_raqam = id_raqam
#
#     @abstractmethod
#     def malumot(self):
#         pass
#
#
# class Bakalavr(Talaba):
#     def __init__(self, ism, yosh, id_raqam, yonalish):
#         super().__init__(ism, yosh, id_raqam)
#         self.yonalish = yonalish
#
#     def malumot(self):
#         return f"Ism: {self.ism}, Yosh: {self.yosh}, ID: {self.id_raqam}, Yo‘nalish: {self.yonalish}"
#
#
# class Magistr(Talaba):
#     def __init__(self, ism, yosh, id_raqam, ilmiy_ish):
#         super().__init__(ism, yosh, id_raqam)
#         self.ilmiy_ish = ilmiy_ish
#
#     def malumot(self):
#         return f"Ism: {self.ism}, Yosh: {self.yosh}, ID: {self.id_raqam}, Ilmiy ish: {self.ilmiy_ish}"
#
#
# talaba1 = Bakalavr("Olim", 20, "12345678", "Dasturlash")
# talaba2 = Magistr("Anvar", 24, "87654321", "Sun'iy intellekt")
# print(talaba1.malumot())
# print(talaba2.malumot())
#
#
#
