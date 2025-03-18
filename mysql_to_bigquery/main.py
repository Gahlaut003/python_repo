from faker import Faker
import mysql.connector

fake = Faker()

# MySQL connection settings
mysql_config = {
    "user": "root",
    "password": "root",
    "port": "3306",
    "database": "demo_db"
}

# Create a connection to MySQL database
mysql_connection = mysql.connector.connect(**mysql_config)
cursor = mysql_connection.cursor()

# Generate and insert 100 records
for _ in range(1):
    cursor.execute("""
        INSERT INTO employee (
            tinyint_col, smallint_col, mediumint_col, int_col, bigint_col,
            float_col, double_col, decimal_col, bit_col, bool_col,
            boolean_col, year_col, date_col, time_col, datetime_col,
            timestamp_col, char_col, varchar_col, tinytext_col, text_col,
            mediumtext_col, longtext_col, binary_col, varbinary_col,
            enum_col, set_col, json_col
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s
        )
    """, (
        fake.random_int(min=0, max=127),  # tinyint_col
        fake.random_int(min=0, max=32767),  # smallint_col
        fake.random_int(min=0, max=8388607),  # mediumint_col
        fake.random_int(min=0, max=2147483647),  # int_col
        fake.random_int(min=0, max=9223372036854775807),  # bigint_col
        fake.pyfloat(),  # float_col
        fake.pyfloat(),  # double_col
        fake.pydecimal(right_digits=2, positive=True),  # decimal_col
        fake.pybool(),  # bit_col
        fake.pybool(),  # bool_col
        fake.pybool(),  # boolean_col
        fake.year(),  # year_col
        fake.date(),  # date_col
        fake.time(),  # time_col
        fake.date_time(),  # datetime_col
        fake.date_time(),  # timestamp_col
        fake.pystr(min_chars=5, max_chars=10),  # char_col
        fake.pystr(min_chars=1, max_chars=255),  # varchar_col
        fake.text(max_nb_chars=255),  # tinytext_col
        fake.text(max_nb_chars=65535),  # text_col
        fake.text(max_nb_chars=16777215),  # mediumtext_col
        fake.text(max_nb_chars=4294967295),  # longtext_col
        fake.binary(length=10),  # binary_col
        fake.binary(length=255),  # varbinary_col
        fake.random_element(elements=('Option1', 'Option2', 'Option3')),  # enum_col
        ','.join(fake.random_elements(elements=('OptionA', 'OptionB', 'OptionC'), unique=True)),  # set_col
        fake.random_element()  # json_col
    ))



# Commit the changes and close the connection
mysql_connection.commit()
mysql_connection.close()
