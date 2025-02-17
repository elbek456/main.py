# 1-misol 5 talik
# from abc import ABC, abstractmethod
#
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
#         return f"Nomi: {self.nomi}, Muallif: {self.muallif}, Nashr yili: {self.nashr_yili}, Yo'nalish: {self.yonalish}"
#
#
#
# kitob1 = BadiiyKitob("Sherlar", "Alisher Navoiy", 1492, "She'riyat")
# kitob2 = IlmiyKitob("Fizika asoslari", "Umaraliyev Elbek", 1687, "Fizika")
#
# print(kitob1.malumot())
# print(kitob2.malumot())
