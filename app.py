from classes import Person
from create_db import Cursor
from itertools import chain


def adicionar(): # recolhe os dados e insere na Classe
    nome = input('Nome: ->')
    cpf = (input('Cpf: ->'))
    turma = int(input('Turma: ->'))
    student1 = Person(nome,cpf,turma)
    return student1.__iter__()


def filtro(iteravel): # recolhe os dados da Class e insere no Data Base
    lista = []
    for n in iteravel:
        lista.append(n)
    Cursor.execute(f' INSERT INTO Alunos VALUES ("{lista[0]}", "{lista[1]}", "{lista[2]}", "{lista[3]}" ) ')


def show_all(): # mostra o banco de dados
    Consulta = Cursor.execute(' SELECT * FROM Alunos').fetchall()
    print(Consulta)


def list_classes(iteravel): # função para extrair apenas int do iterável e não mostrar turma repetida
    temp = map(lambda i: str(i), chain.from_iterable(iteravel))
    d = []
    for ele in temp:
        if ele in d:
            pass
        else:
            print(f'Turma: {ele}')
            d.append(ele)

def show_classes(): # mostra as turmas no DBase
    Consulta1 = Cursor.execute('SELECT Turma FROM Alunos').fetchall()
    list_classes(Consulta1)

def show(): #recebe a info do usuário sobre as turmas na DBase
    dww = input('Show all? [Y][N][C]').lower()
    if dww == 'y':
        show_all()
    if dww == 'c':
        print('Show Classes')
        show_classes()


def app_add_student(): # app
    while True:
        filtro(adicionar())
        show()
        try:
            dwb = input('End program?[Y][N]').lower()
            if dwb == 'y':
                break
            elif dwb == 'n':
                pass
        except:
            print('Not Understand')


app_add_student()
