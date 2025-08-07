from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('mft2.db')


class Student(Model):
    name = CharField(max_length=20)
    family = CharField(max_length=20)

    class Meta:
        database = db
        db_table = "Student"


Student.create_table()
