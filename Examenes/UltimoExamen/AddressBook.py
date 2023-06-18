from typeguard import typechecked
import xml.etree.ElementTree as ET
from xml.dom import minidom
import contact as ct


@typechecked
class AddressBook:
    __MAX_CONTACTS = 5

    def __init__(self, filename: str = ""):
        self.__contacts = {}
        if filename[-4:] == ".xml":
            self.__xml_import(filename)
        elif filename == "":
            pass
        else:
            raise ValueError("El fichero introducido no es válido. Debe ser XML.")

    def __xml_import(self, file):
        self.__xml_read_test(file)

        root = ET.parse(file).getroot()

        for contact in root:
            raw_contact = []
            if len(contact.attrib) != 1:
                raise ValueError("Documento mal formado. Debe tener un nombre.")

            raw_contact.append(contact.attrib['name'])
            for e in contact:
                raw_contact.append(e.text)

            self.register_contact(raw_contact[0], raw_contact[1], raw_contact[2], raw_contact[3])

    @staticmethod
    def __xml_read_test(filename):
        try:
            with open(filename, "r"):
                pass
        except FileNotFoundError as e1:
            raise e1
        except PermissionError as e2:
            raise e2

    @staticmethod
    def __xml_write_test(filename):
        try:
            with open(filename, "w"):
                pass
        except PermissionError as e1:
            raise e1

    def register_contact(self, name: str, phone: str, email: str, address: str = ""):
        if len(self.__contacts) >= AddressBook.__MAX_CONTACTS:
            raise MaxNumberContactsExceeded()

        try:
            self.__contacts[name]
        except KeyError:
            pass
        else:
            raise ContactAlreadyExists()

        self.__contacts[name] = ct.Contact(name, phone, email, address)

    def delete_contact(self, name: str):
        try:
            self.__contacts.pop(name)
        except KeyError as e:
            raise ContactDoesNotExists(e)

    def search_contact(self, name: str):
        try:
            return self.__contacts[name]
        except KeyError as e:
            raise ContactDoesNotExists(e)

    def xml_export(self, filename):
        self.__xml_write_test(filename)

        with open(filename, "wt") as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n<address_book>\n</address_book>')
        root = ET.parse(filename).getroot()

        for contact in self.__contacts.values():
            cont = ET.Element('contact', {'name': contact.name})
            ET.SubElement(cont, 'phone').text = contact.phone
            ET.SubElement(cont, 'email').text = contact.email
            ET.SubElement(cont, 'address').text = contact.address
            root.append(cont)

        xml_minidom = minidom.parseString(ET.tostring(root))
        xml_str = xml_minidom.toprettyxml()
        with open(filename, 'w', encoding="UTF-8") as f:
            f.write(xml_str)

    @property
    def contacts(self):
        values = []
        for x in self.__contacts:
            values.append(self.__contacts[x])
        return tuple(values)


class MaxNumberContactsExceeded(Exception):
    def __init__(self, *args, **kwargs):
        pass


class ContactAlreadyExists(Exception):
    def __init__(self, *args, **kwargs):
        pass


class ContactDoesNotExists(Exception):
    def __init__(self, *args, **kwargs):
        pass
