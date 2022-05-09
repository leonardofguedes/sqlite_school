import sqlite3

Schedule_Class = sqlite3.connect('Schedule.db') #variavel criadora do banco de dados
Cursor = Schedule_Class.cursor()

"""
Cursor.execute(
   'CREATE TABLE Schedule ( Teacher text, Day_of_week text, Room int, Turma int, Matéria text)'
)
"""

