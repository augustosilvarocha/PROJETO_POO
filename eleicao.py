from abc import ABC, abstractmethod

class Urna_Eletronica:
    def __init__(self,local,status=False):
        self.local=local
        self.status=status

    def iniciar_votacao(self):
        self.status=True

    def adicionar_voto(self,eleitor):
        pass

    def encerrar_votacao(self):
        self.status=False

class Boletim:
    def __init__(self):
        self.resultados=[]

    def exibir_resultado(self):
        pass

class Local:
    def __init__(self, escola, zona, sessao, quantidadeEleitores):
        self.__escola = escola
        self.__zona = zona
        self.__sessao = sessao
        self.__quantidadeEleitores = quantidadeEleitores

    def get_escola(self):
        return self.__escola

    def set_escola(self, escola):
        self.__escola = escola

    def get_zona(self):
        return self.__zona

    def set_zona(self, zona):
        self.__zona = zona

    def get_sessao(self):
        return self.__sessao

    def set_sessao(self, sessao):
        self.__sessao = sessao

    def get_quantidadeEleitores(self):
        return self.__quantidadeEleitores

    def set_quantidadeEleitores(self, quantidadeEleitores):
        self.__quantidadeEleitores = quantidadeEleitores

class Partido:
    def __init__(self,nome):
        self.nome=nome
        self.membros=[]
        self.partidos=[]

    def adicionar_membros(self,membro):
        self.membros.append(membro)

class Eleitor:
    def __init__(self, nome, titulo, sessao, idade):
        self.__nome = nome
        self.__titulo = titulo
        self.__sessao = sessao
        self.__idade = idade
        self.eleitores=[]

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_sessao(self):
        return self.__sessao

    def set_sessao(self, sessao):
        self.__sessao = sessao

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def _Votar(self,urna):
        if urna.status==False:
            print("Não está no momento de votar ainda...")
        else:
            print("Vote")
    
    def exibir_proposta_candidatos(self):
        pass

class Candidato(Eleitor,Partido):
    def __init__(self, nome, titulo, sessao, idade,partido):
        super().__init__(nome, titulo, sessao, idade)
        self.partido=partido

    @abstractmethod
    def realizar_comicio(self):
        pass

class Prefeito(Candidato):
    def __init__(self, nome, titulo, sessao, idade, partido):
        super().__init__(nome, titulo, sessao, idade, partido)
        self.proposta=[]

    def adicionar_candidato_a_partido(self):
        pass

class Vereador(Candidato):
    def __init__(self, nome, partido):
        super().__init__(nome, partido)
    
    def realizar_comicio(self):
        pass

class Cidade:
    def __init__(self,nome,estado,cep):
        self.nome=nome
        self.estado=estado
        self.cep=cep

class Debate:
    def debater(self):
        pass



eleitor= Eleitor("Ruth Ellen","400","00",20)

local_ruth= Local("EEFAM","400","007",700)

urna_1= Urna_Eletronica(local_ruth)

eleitor._Votar(urna_1)

urna_1.iniciar_votacao()
eleitor._Votar(urna_1)

pariido_1= Partido("PT")
partido_2= Partido("PSDB")

partido_2.adicionar_membros()




