import unidecode


materias = [
    # Matérias aceitas na escola
    'matematica', 'fisica', 'geografia','artes','biologia','portugues','ingles','quimica','historia'
]

dias_da_semana = {
    # Dias da semana que as aulas são ministradas
    'segunda-feira', 'segunda', 'terça-feira', 'terça', 'quarta-feira', 'quinta-feira', 'quinta', 'quarta', 'sexta',
    'sexta-feira'
}

salas = [
    # Salas de aula disponíveis
    1,2,3,4,5,6,7,8,9,10
]

turmas_escola = [
    100,101,200,201,300,301,400,401,500,501
]

def confere_materias(word):
    """Função para conferir a validade das matérias inseridas no programa"""
    a = unidecode.unidecode(word)
    if a in materias:
        pass
    if a not in materias:
        print('Essa matéria não é válida')
        return False


def confere_dia_da_semana(word):
    """Função para conferir os dias inseridos no programa"""
    if word in dias_da_semana:
        pass
    if word not in dias_da_semana:
        print('Esse dia não é válido.')
        return False


def confere_sala(word):
    """Função para conferir se as salas do programa estão disponíveis"""
    if word in salas:
        pass
    if word not in salas:
        print('Essa sala não existe.')
        return False

def confere_turma():
    """Função para conferir se a turma existe"""
    while True:
        turma = int(input('Turma: ->'))
        if turma in turmas_escola:
            return turma
        if turma not in turmas_escola:
            print('Essa turma não existe.')