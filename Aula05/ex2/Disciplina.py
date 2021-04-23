class Disciplina():
    def __init__(self, nome='Disciplina 1', nota=1.0):
        self.nome = nome
        self.nota = nota

    def __del__(self):
        print('Disciplina',self.nome,'removida')