from typeguard import typechecked
import re


@typechecked
class Contact:
    def __init__(self, name: str, phone: str, email: str, address: str = ""):
        self.__name = name
        self.__phone = self.__check_phone(phone)
        self.__email = self.__check_email(email)
        self.__address = address

    @staticmethod
    def __check_phone(phone):
        regex = re.match("[679]\d{8}", phone)
        if regex is None or len(phone) != 9:
            raise PhoneIsNotValid()
        else:
            return phone

    @staticmethod
    def __check_email(email):
        regex = re.match("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", email)
        if regex is None:
            raise EmailIsNotValid()
        else:
            return email

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, new_phone):
        self.__phone = self.__check_phone(new_phone)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = self.__check_email(new_email)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address


class PhoneIsNotValid(Exception):
    def __init__(self, *args, **kwargs):
        pass


class EmailIsNotValid(Exception):
    def __init__(self, *args, **kwargs):
        pass

