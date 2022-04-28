class Person:
    id = 0

    def __init__(self, nome, cpf, turma):
        Person.id += 1
        self.__nome = nome.strip().title()
        self.__id = Person.id
        self.__cpf = cpf
        self.__turma = turma

    def __iter__(self):
        return [self.__nome, self.__id, self.__cpf, self.__turma]


class Student(Person):

    def __init__(self, nome, cpf, turma, matricula):
        Person.__init__(self, nome, cpf, turma)
        self.__matricula = matricula

    def __iter__(self):
        lis = []
        for n in Person.__iter__(self):
            lis.append(n)
        lis.append(self.__matricula)
        return lis

