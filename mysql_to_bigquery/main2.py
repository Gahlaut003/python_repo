from faker import Faker
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tinyint_col = Column(Integer)
    smallint_col = Column(Integer)
    mediumint_col = Column(Integer)
    int_col = Column(Integer)
    bigint_col = Column(Integer)
    float_col = Column(Float)
    double_col = Column(Float)
    decimal_col = Column(Float)
    bit_col = Column(Boolean)
    bool_col = Column(Boolean)
    boolean_col = Column(Boolean)
    year_col = Column(Integer)
    date_col = Column(DateTime)
    time_col = Column(DateTime)
    datetime_col = Column(DateTime)
    timestamp_col = Column(DateTime)
    char_col = Column(String(10))
    varchar_col = Column(String(255))
    tinytext_col = Column(String(255))
    text_col = Column(String(65535))
    mediumtext_col = Column(String(16777215))
    longtext_col = Column(String(4294967295))
    binary_col = Column(String(10))
    varbinary_col = Column(String(255))
    enum_col = Column(String(10))
    set_col = Column(String(10))
    json_col = Column(String(255))

fake = Faker()

# MySQL connection settings
mysql_config = {
    "user": "root",
    "password": "root",
    "host": "3306",
    "database": "demo_db"
}


# Create an SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{mysql_config['user']}:{mysql_config['password']}@{mysql_config['host']}:{mysql_config['port']}/{mysql_config['database']}")

# Create the employee table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Generate and insert 100 records
for _ in range(100):
    employee = Employee(
        tinyint_col=fake.random_int(min=0, max=127),
        smallint_col=fake.random_int(min=0, max=32767),
        mediumint_col=fake.random_int(min=0, max=8388607),
        int_col=fake.random_int(min=0, max=2147483647),
        bigint_col=fake.random_int(min=0, max=9223372036854775807),
        float_col=fake.random_float(),
        double_col=fake.random_float(),
        decimal_col=fake.pydecimal(right_digits=2, positive=True),
        bit_col=fake.pybool(),
        bool_col=fake.pybool(),
        boolean_col=fake.pybool(),
        year_col=fake.year(),
        date_col=fake.date_time(),
        time_col=fake.date_time(),
        datetime_col=fake.date_time(),
        timestamp_col=fake.date_time(),
        char_col=fake.pystr(min_chars=5, max_chars=10),
        varchar_col=fake.pystr(min_chars=1, max_chars=255),
        tinytext_col=fake.text(max_nb_chars=255),
        text_col=fake.text(max_nb_chars=65535),
        mediumtext_col=fake.text(max_nb_chars=16777215),
        longtext_col=fake.text(max_nb_chars=4294967295),
        binary_col=fake.binary(length=10),
        varbinary_col=fake.binary(length=255),
        enum_col=fake.random_element(elements=('Option1', 'Option2', 'Option3')),
        set_col=','.join(fake.random_elements(elements=('OptionA', 'OptionB', 'OptionC'), unique=True)),
        json_col=fake.random_element()
    )
    session.add(employee)

# Commit the changes and close the session
session.commit()
session.close()
