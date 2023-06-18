from typeguard import typechecked
import xml.etree.ElementTree as ET
from xml.dom import minidom
import contact as ct
# import Sql_DAO


@typechecked
class AddressBook:
    def __init__(self, dao):
        self.__DAO = dao

    def register_contact(self, name: str, phone: str, email: str, address: str = ""):
        self.__DAO.create_contact(ct.Contact(name, phone, email, address))

    def delete_contact(self, name: str):
        self.__DAO.delete_contact(name)

    @property
    def contacts(self):
        return self.__DAO.contacts

    def xml_export(self, filename):
        self.__xml_write_test(filename)

        with open(filename, "wt") as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n<address_book>\n</address_book>')
        root = ET.parse(filename).getroot()

        for contact in self.contacts:
            cont = ET.Element('contact', {'name': contact[0]})
            ET.SubElement(cont, 'phone').text = contact[1]
            ET.SubElement(cont, 'email').text = contact[2]
            ET.SubElement(cont, 'address').text = contact[3]
            root.append(cont)

        xml_minidom = minidom.parseString(ET.tostring(root))
        xml_str = xml_minidom.toprettyxml()
        with open(filename, 'w', encoding="UTF-8") as f:
            f.write(xml_str)

    def xml_import(self, file):
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


class ContactAlreadyExists(Exception):
    def __init__(self, *args, **kwargs):
        pass


class ContactDoesNotExists(Exception):
    def __init__(self, *args, **kwargs):
        pass
