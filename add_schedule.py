from create_db_schedule import Cursor
from data_from_school import confere_dia_da_semana, confere_materias, confere_sala


def consulta_teacher(t, d):
    """Consulta se o professor está disponível naquela data"""
    consulta = Cursor.execute(' SELECT * FROM Schedule').fetchall()
    for n in consulta:
        if n[0] == t:
            if n[1] == d:
                return False
            else:
                pass
        else:
            pass


def consulta_room(d, r):
    """Consulta se a sala está disponível naquela data"""
    consulta = Cursor.execute(' SELECT * FROM Schedule').fetchall()
    for n in consulta:
        if n[1] == d:
            if n[2] == r:
                return False
            else:
                pass
        else:
            pass


def add_class():
    """Recebe os dados, verifica sua validade com outros programas e depois insere-os no data base"""
    while True:
        day = str(input('Dia da semana: ->'))
        if confere_dia_da_semana(day) == False:
            return False
        teacher = str(input('Professor: ->'))
        a = consulta_teacher(teacher, day)
        if a == False:
            print('Teacher busy in this day')
            return False
        else:
            pass
        room = int(input('Sala: ->'))
        if confere_sala(room) == False:
            return False
        b = consulta_room(day, room)
        if b == False:
            print('Room not available')
            return False
        else:
            pass
        materia = input('Matéria: ->')
        if confere_materias(materia) == False:
            return False
        turma = input('Turma: ->')
        Cursor.execute(f' INSERT INTO Schedule VALUES\n'
                           f'("{teacher}","{day}", "{room}", "{turma}", "{materia}") ')
        return False


def sistem():
    """Programa"""
    while True:
        add_class()
        mostrar_acabar_continuar = input('show, end, continue? [s][e][c]').lower().strip()
        if mostrar_acabar_continuar == 's':
            consulta = Cursor.execute(' SELECT * FROM Schedule').fetchall()
            print(consulta)
        elif mostrar_acabar_continuar == 'c':
            pass
        else:
            return False

sistem()