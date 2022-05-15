from create_db_schedule import Cursor
from data_from_school import confere_dia_da_semana, confere_materias, confere_sala, confere_turma, confere_professor
from decorative import decorative_add_schedule


def conferencia_disponibilidade(day, teacher, room, turma):
    """Confere a disponibilidade da sala, turma e professor"""
    consulta = Cursor.execute(' SELECT * FROM Schedule').fetchall()
    for n in consulta:
        if n[1] == day and n[3] == turma:
            print(f'A turma {turma} não está disponível na {day}.')
            return False
        elif n[1] == day and n[2] == room:
            print(f'A sala {room} não está disponível na {day}.')
            return False
        elif n[1] == day and n[0] == teacher:
            print(f'Professor indisponível na {day}.')
            return False
        else:
            return True


def add_class():
    """Recebe os dados, verifica sua validade com outros programas e depois insere-os no data base"""
    while True:
        day = confere_dia_da_semana()
        teacher = confere_professor()
        room = confere_sala()
        materia = confere_materias()
        turma = confere_turma()
        analise = conferencia_disponibilidade(day,teacher,room,turma)
        if analise == True or analise == None:
            Cursor.execute(f' INSERT INTO Schedule VALUES\n'
                               f'("{teacher}","{day}", "{room}", "{turma}", "{materia}") ')
            break
        else:
            print('Os dados inseridos não se ajustam aos horários disponíveis')
            break


def app_add_schedule():
    """Programa"""
    decorative_add_schedule()
    while True:
        mostrar_acabar_continuar = input('Show data, End program, Continue adding? [s][e][c]').lower().strip()
        if mostrar_acabar_continuar == 's':
            consulta = Cursor.execute(' SELECT * FROM Schedule').fetchall()
            print(consulta)
        elif mostrar_acabar_continuar == 'c':
            add_class()
        else:
            break

