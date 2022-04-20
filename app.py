from classes import Person
from create_db import Cursor


def adicionar():
    nome = input('Nome: ->')
    cpf = (input('Cpf: ->'))
    turma = int(input('Turma: ->'))
    student1 = Person(nome,cpf,turma)
    return student1.__iter__()


def filtro(iteravel):
    lista = []
    for n in iteravel:
        lista.append(n)
    Cursor.execute(f' INSERT INTO Alunos VALUES ("{lista[0]}", "{lista[1]}", "{lista[2]}", "{lista[3]}" ) ')


def show():
    Consulta = Cursor.execute(' SELECT * FROM Alunos').fetchall()
    print(Consulta)


def app_add_student():
    while True:
        filtro(adicionar())
        dww = input('show?')
        if dww == 'y':
            show()
        dwb = input('y')
        if dwb == 'y':
            break


app_add_student()
