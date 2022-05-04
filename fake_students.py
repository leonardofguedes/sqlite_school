from faker import Faker
import random
from classes import Student


def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        nome = fake.name()
        cpf = f'{random.randrange(100,999)}{random.randrange(100,999)}{random.randrange(100,999)}-{random.randrange(0,9)}'
        turma = random.randrange(400,405)
        matricula = random.randrange(0,quantidade_de_pessoas)
        p = Student(nome=nome, cpf=cpf, turma=turma, matricula=matricula)
        p.sql_in()

