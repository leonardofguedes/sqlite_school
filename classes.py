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
        return self.nome, self.id, self.cpf, self.turma, self.matricula

