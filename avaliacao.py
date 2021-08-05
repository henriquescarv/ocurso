from questao import Questao

class Avaliacao:
    def __init__(
                self,
                nome_avaliacao: str,
                questao: Questao,
                lista_questoes: list,
                nota: int,
                total_acertos: int):
            self.__nome_avaliacao = nome_avaliacao
            self.__questao = questao
            self.__lista_questoes = lista_questoes
            self.__lista_questoes.append(questao)
            self.__nota = nota
            self.__total_acertos = total_acertos
            
    @property
    def nome_avaliacao(self):
        return self.__nome_avaliacao

    @property
    def questao(self):
        return self.__questao

    @property
    def lista_questoes(self):
        return self.__lista_questoes

    @property
    def nota(self):
        return self.__nota

    @property
    def total_acertos(self):
        return self.__total_acertos

    @nome_avaliacao.setter
    def nome_avaliacao(self, nome_avaliacao):
        self.__nome_avaliacao = nome_avaliacao

    @questao.setter
    def questao(self, questao):
        self.__questao = questao

    @lista_questoes.setter
    def lista_questoes(self, lista_questoes):
        self.__lista_questoes = lista_questoes

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    @total_acertos.setter
    def total_acertos(self, total_acertos):
        self.__total_acertos = total_acertos