"""
Задание 1
Реализуйте класс «Человек».
Необходимо хранить в полях класса: ФИО, дату рождения,
контактный телефон, город, страну, домашний адрес.
Реализуйте методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса.
"""

class Human():

    def __init__(self, name_surname_patronymic, bithtday, telephone_num, city, country, adress):
        self.name_surname_patronymic = name_surname_patronymic
        self.bithtday = bithtday
        self.telephone_num = telephone_num
        self.city = city
        self.country = country
        self.adress = adress

    def print_public_inf(self):
        show_public_inf = str(self.name_surname_patronymic) + " " + self.city + " " + self.country
        return (self.name_surname_patronymic, self.city, self.country)

    def print_privat_inf(self):
        show_privat_inf = str(self.name_surname_patronymic) + " " + self.bithtday + " " + self.telephone_num \
                          + " " + self.city + " " + self.country + " " + self.adress
        return (self.name_surname_patronymic, self.bithtday, self.telephone_num, self.city, self.country, self.adress)

    def print_publick_inf_1(self):
        return self.print_privat_inf

homo_sapiens = Human(
    "Носов Сергей Андреевич",
    "08.10.1996",
    89118946914,
    "Псков",
    "Россия",
    "Юбилейная улица"

)

print(homo_sapiens.print_public_inf())


