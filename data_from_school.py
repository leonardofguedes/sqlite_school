import unidecode

materias = [
    'matematica', 'fisica', 'geografia','artes','biologia','portugues','ingles','quimica','historia'
]

dias_da_semana = {
    'segunda-feira', 'segunda', 'terça-feira', 'terça', 'quarta-feira', 'quinta-feira', 'quinta', 'quarta', 'sexta',
    'sexta-feira'
}

salas = [
    1,2,3,4,5,6,7,8,9,10
]


def confere_materias(word):
    a = unidecode.unidecode(word)
    if a in materias:
        pass
    if a not in materias:
        print('Essa matéria não é válida')
        return False


def confere_dia_da_semana(word):
    if word in dias_da_semana:
        pass
    if word not in dias_da_semana:
        print('Esse dia não é válido.')
        return False


def confere_sala(word):
    if word in salas:
        pass
    if word not in salas:
        print('Essa sala não existe.')
        return False