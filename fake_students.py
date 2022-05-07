from faker import Faker
import random
from classes import Student

turmas_escola = [100,101,200,201,300,301,400,401,500,501]

def criando_pessoas(quantidade_de_pessoas):
    """Criando alunos falsos para facilitar análise de dados"""
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        nome = fake.name()
        cpf = f'{random.randrange(100,999)}{random.randrange(100,999)}{random.randrange(100,999)}-{random.randrange(0,9)}'
        turma_escola = random.choice(turmas_escola)
        ano_nascimento = random.randrange(1998,2021)
        p = Student(nome=nome, cpf=cpf, turma=turma_escola, ano_nascimento=ano_nascimento)
        p.sql_in()
