from classes import Student
from create_db import Cursor
from itertools import chain
from fake_students import criando_pessoas
from validate_docbr import CPF
from decorative import decorative_add_student
from data_from_school import confere_turma

def cpf_analysis():
    """Recebe e analisa a validade do CPF"""
    while True:
        cpf1 = str(input('Cpf: ->')).replace('.', '').replace('-', '')
        cpf = CPF()
        if cpf.validate(cpf1):
            return cpf1
        else:
            print('Invalid CPF')
            print('*'*30)


def adicionar():
    """Recebe dados do usuário e insere na class"""
    nome = input('Nome: ->')
    cpf = cpf_analysis()
    turma = confere_turma()
    ano_nascimento = int(input('Ano de nascimento: ->'))
    student1 = Student(nome, cpf, turma, ano_nascimento)
    return student1.sql_in()


def show_all():
    """function mostra todos os dados do db"""
    consulta = Cursor.execute(' SELECT * FROM Alunos').fetchall()
    return consulta


def show_students():
    """Function mostra os students de uma turma"""
    consulta = Cursor.execute(' SELECT * FROM Alunos').fetchall()
    try:
        turma = int(input('Turma a consultar: ->'))
        print('Nome | ID | CPF | Turma | Matricula')
        for n in consulta:
            if n[3] == turma:
                print(n)
    except:
        pass


def show_matricula():
    """Pesquisar matricula específica"""
    consulta = Cursor.execute(' SELECT * FROM Alunos').fetchall()
    matricula = int(input('Matricula a consultar: ->'))
    for n in consulta:
        if n[1] == matricula:
            print(f'Nome: {n[0]}, Matricula {n[1]}, CPF {n[2]}, Turma: {n[3]}, Ano de Nascimento: {n[4]}')



def list_classes(iteravel):
    """Function que extrai apenas int do iterável e ignora turmas repetidas"""
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
        especifics = input('Classes [C] or Students of Classes [SC] or Matriculas [MA]: ->').strip().lower()
        if especifics == 'c':
            print('Show Classes:')
            show_classes()
        elif especifics == 'sc':
            show_students()
        elif especifics == 'ma':
            show_matricula()
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
    criando_pessoas(500)
    decorative_add_student()
    while True:
        adicionar()
        show()
        if not add_or_end():
            break
        else:
            pass



