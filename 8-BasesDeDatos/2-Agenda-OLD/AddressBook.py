from typeguard import typechecked
import xml.etree.ElementTree as ET
from xml.dom import minidom
import contact as ct
import mysql.connector


@typechecked
class AddressBook:
    __MAX_CONTACTS = 99999

    def __init__(self, root: str, database_name: str, username: str, password: str, host: str = "localhost"):
        self.__contacts = {}

        self.__database_cursor = None

        self.__create_database(root, database_name, username, password, host)

    def __create_database(self, root: str, dbname: str, dbuser: str, dbpasswd: str, host: str):
        ROOT, DBNAME, DBUSER, DBPASSWD = root, dbname, dbuser, dbpasswd

        MYDB = mysql.connector.connect(
            host="localhost",
            user=ROOT,
            password=ROOT
        )

        mycursor = MYDB.cursor()

        # Creamos la Base de Datos
        mycursor.execute(f"DROP DATABASE IF EXISTS {DBNAME}")
        mycursor.execute(f"CREATE DATABASE {DBNAME}")

        # Creamos Usuario
        mycursor.execute(f"DROP USER IF EXISTS '{DBUSER}'@'%'")
        mycursor.execute(f"CREATE USER '{DBUSER}'@'%' IDENTIFIED BY '{DBPASSWD}'")
        mycursor.execute(f"GRANT ALL PRIVILEGES ON {DBNAME}.* TO '{DBUSER}'@'%'")
        mycursor.execute("FLUSH PRIVILEGES")

        # Cambiamos al nuevo usuario
        MYDB = mysql.connector.connect(
            host="localhost",
            user=DBUSER,
            password=DBPASSWD,
            database=DBNAME
        )
        mycursor = MYDB.cursor()

        # Creamos las tablas
        mycursor.execute("CREATE TABLE CONTACTS("
                         "name VARCHAR(45) PRIMARY KEY, "
                         "phone CHAR(9) NOT NULL, "
                         "email VARCHAR(45) NOT NULL, "
                         "address VARCHAR(25) NOT NULL, "
                         "CONSTRAINT PHONE_CHECK CHECK (phone REGEXP '^[679][0-9]{8}$'), "
                         "CONSTRAINT EMAIL_CHECK CHECK (email REGEXP '[^@ \t\r\n]+@[^@ \t\r\n]+\\.[^@ \t\r\n]+'))")

        self.__database_cursor = mycursor

    def register_contact(self, name: str, phone: str, email: str, address: str = ""):
        ct.Contact(self.__database_cursor, name, phone, email, address)

    def delete_contact(self, name: str):
        self.__database_cursor.execute(f"DELETE * FROM contacts WHERE name = {name}")

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
        result = self.__database_cursor.execute("SELECT * FROM contacts").fetchall()
        return result


class MaxNumberContactsExceeded(Exception):
    def __init__(self, *args, **kwargs):
        pass


class ContactAlreadyExists(Exception):
    def __init__(self, *args, **kwargs):
        pass


class ContactDoesNotExists(Exception):
    def __init__(self, *args, **kwargs):
        pass
