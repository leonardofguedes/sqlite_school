import unidecode

professores = [
    # Professores listados
    'leonardo', 'paulo', 'marina', 'marcos', 'gabriel', 'joaquim', ' maria', 'rosana', 'isadora',
]

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

def confere_dia_da_semana():
    """Função para conferir os dias inseridos no programa"""
    while True:
        day = str(input('Dia da semana: ->')).strip().lower()
        if day in dias_da_semana:
            return day
        if day not in dias_da_semana:
            print('Esse dia não é válido.')

def confere_professor():
    """Função para conferir a validade dos professores inseridas no programa"""
    while True:
        professor = str(input('Professor: ->'))
        if professor in professores:
            return professor
        if professor not in professores:
            print('Esse professor não está cadastrado.')

def confere_sala():
    """Função para conferir se as salas do programa estão disponíveis"""
    while True:
        room = int(input('Sala: ->'))
        if room in salas:
            return room
        if room not in salas:
            print('Essa sala não existe.')

def confere_materias():
    """Função para conferir a validade das matérias inseridas no programa"""
    while True:
        materia = str(input('Matéria: ->')).lower()
        a = unidecode.unidecode(materia)
        if a in materias:
            return a
        if a not in materias:
            print('Essa não é válida')

def confere_turma():
    """Função para conferir se a turma existe"""
    while True:
        turma = int(input('Turma: ->'))
        if turma in turmas_escola:
            return turma
        if turma not in turmas_escola:
            print('Essa turma não existe.')