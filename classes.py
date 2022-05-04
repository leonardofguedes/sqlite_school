from create_db import Cursor


class Person:
    id = 0

    def __init__(self, nome, cpf, turma):
        Person.id += 1
        self.nome = nome.strip().title()
        self.id = Person.id
        self.cpf = cpf
        self.turma = turma

    def __str__(self):
        return self.nome, self.id, self.cpf, self.turma


class Student(Person):

    def __init__(self, nome, cpf, turma, matricula):
        Person.__init__(self, nome, cpf, turma)
        self.matricula = matricula

    def sql_in(self):
        student = self.nome, self.id, self.cpf, self.turma, self.matricula
        Cursor.execute(f' INSERT INTO Alunos VALUES\n'
                       f'("{student[0]}","{student[1]}", "{student[2]}", "{student[3]}", "{student[4]}") ')
