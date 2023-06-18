import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv("secrets.env")

ROOT = os.getenv('ROOT')
DBNAME = os.getenv('DBNAME')
DBUSER = os.getenv('DBUSER')
DBPASSWD = os.getenv('DBPASSWD')

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
mycursor.execute(f"DROP USER '{DBUSER}'@'%'")
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
mycursor.execute("CREATE TABLE CUSTOMERS("
                 "dni CHAR(9) PRIMARY KEY, "
                 "name VARCHAR(45) NOT NULL, "
                 "address VARCHAR(45) NOT NULL, "
                 "phone CHAR(9) NOT NULL)")

mycursor.execute("CREATE TABLE ACCOUNTS("
                 "id INT AUTO_INCREMENT PRIMARY KEY, "
                 "customer_id CHAR(9) NOT NULL, "
                 "alive TINYINT(1) NOT NULL, "
                 "CONSTRAINT FK_CUSTOMER FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(dni))")

mycursor.execute("CREATE TABLE TRANSACTIONS("
                 "account_id INT NOT NULL, "
                 "amount DOUBLE NOT NULL, "
                 "datetime DATETIME NOT NULL, "
                 "type ENUM('DEPOSIT', 'CHARGE', 'TRANSFER_SENT', 'TRANSFER_RECEIVED') NOT NULL, "
                 "account_id_transfer INT NOT NULL, "
                 "description VARCHAR(30) NOT NULL, "
                 "CONSTRAINT PK_TRANSACTIONS PRIMARY KEY (account_id, datetime), "
                 "CONSTRAINT FK_ACCOUNT_ID FOREIGN KEY (account_id) REFERENCES ACCOUNTS(id), "
                 "CONSTRAINT FK_ACCOUNT_ID_TRANSFER FOREIGN KEY (account_id_transfer) REFERENCES ACCOUNTS(id))")
