from dotenv import load_dotenv
from os import getenv
import mysql.connector

load_dotenv("secrets.env")


class SqlDAO:
    def __init__(self):
        self.__root_user = getenv('ROOT_USER')
        self.__root_password = getenv('ROOT_PASSWORD')
        self.__database = None

    def create_database(self, db_name, db_user, db_password):
        db = mysql.connector.connect(
            host="localhost",
            user=self.__root_user,
            password=self.__root_password
        )

        my_cursor = db.cursor()

        # Creamos la Base de Datos
        my_cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        my_cursor.execute(f"CREATE DATABASE {db_name}")

        # Creamos Usuario
        my_cursor.execute(f"DROP USER IF EXISTS '{db_user}'@'%'")
        my_cursor.execute(f"CREATE USER '{db_user}'@'%' IDENTIFIED BY '{db_password}'")
        my_cursor.execute(f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'%'")
        my_cursor.execute("FLUSH PRIVILEGES")

        # Cambiamos al nuevo usuario
        self.__database = mysql.connector.connect(
            host="localhost",
            user=db_user,
            password=db_password,
            database=db_name
        )
        my_cursor = self.__database.cursor()

        # Creamos las tablas
        my_cursor.execute("CREATE TABLE CONTACTS("
                          "name VARCHAR(45) PRIMARY KEY, "
                          "phone CHAR(9) NOT NULL, "
                          "email VARCHAR(45) NOT NULL, "
                          "address VARCHAR(25) NOT NULL, "
                          "CONSTRAINT PHONE_CHECK CHECK (phone REGEXP '^[679][0-9]{8}$'), "
                          "CONSTRAINT EMAIL_CHECK CHECK (email REGEXP '[^@ \t\r\n]+@[^@ \t\r\n]+\\.[^@ \t\r\n]+'))")

    def use_database(self, db_name, db_user, db_password):
        self.__database = mysql.connector.connect(
            host="localhost",
            user=db_user,
            password=db_password,
            database=db_name
        )

    # def create_user(self, name: str, phone: str, email: str, address: str = ""):
    # my_cursor = self.__database.cursor()

    # my_cursor.execute(f"INSERT INTO contacts VALUES ({name}, {phone}, {email}, {address})")

    def create_contact(self, contact):
        my_cursor = self.__database.cursor()

        # sql = "INSERT INTO contacts (name, phone, email, address) VALUES (%s, %s, %s, %s)"
        # val = (contact.name, contact.phone, contact.email, contact.address)

        my_cursor.execute(f"INSERT INTO contacts VALUES ("
                          f"'{contact.name}', '{contact.phone}', '{contact.email}', '{contact.address}')")
        self.__database.commit()

    def delete_contact(self, name: str):
        my_cursor = self.__database.cursor()

        my_cursor.execute(f"DELETE FROM contacts WHERE name = '{name}'")
        self.__database.commit()

    @property
    def contacts(self):
        my_cursor = self.__database.cursor()
        my_cursor.execute("SELECT * FROM contacts")
        return my_cursor.fetchall()
