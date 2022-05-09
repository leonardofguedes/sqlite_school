from create_db import Cursor


class Person:
    matricula = 0

    def __init__(self, nome, cpf):
        Person.matricula += 1
        self.nome = nome.strip().title()
        self.matricula = Person.matricula
        self.cpf = cpf

    def __str__(self):
        return self.nome, self.matricula, self.cpf


class Student(Person):

    def __init__(self, nome, cpf, turma, ano_nascimento):
        Person.__init__(self, nome, cpf)
        self.turma = turma
        self.ano_nascimento = ano_nascimento

    def sql_in(self):
        student = self.nome, self.matricula, self.cpf, self.turma, self.ano_nascimento
        Cursor.execute(f' INSERT INTO Alunos VALUES\n'
                       f'("{student[0]}","{student[1]}", "{student[2]}", "{student[3]}", "{student[4]}") ')


class Teacher(Person):

    def __init__(self, nome, cpf, materia):
        self.materia = materia.capitalize()
        Person.__init__(self, nome, cpf)


    def __str__(self):
        return self.nome, self.cpf, self.materia


