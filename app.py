from classes import Student
from create_db import Cursor
from itertools import chain


def adicionar():
    """recebe dados do usuário e insere na class"""
    nome = input('Nome: ->')
    cpf = (input('Cpf: ->'))
    turma = int(input('Turma: ->'))
    matricula = int(input('Matricula: ->'))
    student1 = Student(nome, cpf, turma, matricula)
    return student1.__iter__()


def filtro(iteravel):
    """recolhe dados da Class e insere no dbase"""
    lista = []
    for n in iteravel:
        lista.append(n)
    Cursor.execute(f' INSERT INTO Alunos VALUES ("{lista[0]}", "{lista[1]}", "{lista[2]}", "{lista[3]}", "{lista[4]}") ')


def show_all():
    """function mostra todos os dados do db"""
    Consulta = Cursor.execute(' SELECT * FROM Alunos').fetchall()
    print(Consulta)


def list_classes(iteravel):
    """function que extrai apenas int do iterável e ignora turmas repetidas"""
    temp = map(lambda i: str(i), chain.from_iterable(iteravel))
    d = []
    for ele in temp:
        if ele in d:
            pass
        else:
            print(f'Turma: {ele}')
            d.append(ele)


def show_classes():
    """function mostra dados do db"""
    Consulta1 = Cursor.execute('SELECT Turma FROM Alunos').fetchall()
    list_classes(Consulta1)


def show():
    """function que recebe a info do usuario sobre mostrar dados"""
    dww = input('Show all? [Y][N][C]').lower()
    if dww == 'y':
        show_all()
    elif dww == 'c':
        print('Show Classes')
        show_classes()
    else:
        pass


def add_or_end():
    """ function p/ encerrar o programa ou continuar a adicionar"""
    while True:
        try:
            a = input('Do you want to ADD more or END the program? [ADD][END]').strip().lower()
            if a == 'end':
                return False
            elif a == 'add':
                return True
            else:
                print('Wrong answer')
        except:
            print('Wrong answer')


def app_add_student():  # app
    while True:
        filtro(adicionar())
        show()
        if not add_or_end():
            break
        else:
            pass


app_add_student()
