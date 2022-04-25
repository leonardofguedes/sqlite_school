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

