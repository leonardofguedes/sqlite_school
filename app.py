from classes import Person, Student
from create_db import Cursor
from itertools import chain
from fake_students import criando_pessoas


def adicionar():
    """recebe dados do usuário e insere na class"""
    nome = input('Nome: ->')
    cpf = (input('Cpf: ->'))
    turma = int(input('Turma: ->'))
    matricula = int(input('Matricula: ->'))
    student1 = Student(nome, cpf, turma, matricula)
    return student1.sql_in()


def filtro(iteravel):
    """recolhe dados da Class e insere no dbase"""
    Cursor.execute(f' INSERT INTO Alunos VALUES\n'
                   f'("{iteravel[0]}","{iteravel[1]}", "{iteravel[2]}", "{iteravel[3]}", "{iteravel[4]}") ')


def show_all():
    """function mostra todos os dados do db"""
    consulta = Cursor.execute(' SELECT * FROM Alunos').fetchall()
    return consulta


def show_students():
    """function mostra os students de uma turma"""
    Consulta = Cursor.execute(' SELECT * FROM Alunos').fetchall()
    try:
        turma = int(input('Turma a consultar: ->'))
        print('Nome | ID | CPF | Turma | Matricula')
        for n in Consulta:
            if n[3] == turma:
                print(n)
    except:
        pass


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
    consulta = Cursor.execute('SELECT Turma FROM Alunos').fetchall()
    list_classes(consulta)


def show():
    """function que recebe a info do usuario sobre mostrar dados"""
    dww = input('Show all? [Y][N][E]').lower()
    if dww == 'y':
        print(show_all())
    elif dww == 'n':
        pass
    else:
        print('Show especifics:')
        especifics = input('Classes [C] or Students of Classes [SC]: ->').strip().lower()
        if especifics == 'c':
            print('Show Classes:')
            show_classes()
        if especifics == 'sc':
            show_students()
        else:
            pass


def add_or_end():
    """ function p/ encerrar o programa ou continuar a adicionar"""
    while True:
        try:
            a = input('Do you want to: ADD more, LOOK again or END the program? [ADD][LOOK][END]').strip().lower()
            if a == 'end':
                return False
            elif a == 'add':
                return True
            elif a == 'look':
                show()
            else:
                print('Wrong answer')
        except:
            print('Wrong answer')


def app_add_student():  # app
    criando_pessoas(50)
    while True:
        filtro(adicionar())
        show()
        if not add_or_end():
            break
        else:
            pass


app_add_student()
