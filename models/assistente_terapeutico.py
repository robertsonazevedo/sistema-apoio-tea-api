from sqlalchemy import Column, String, Integer
from  models import Base

class AssistenteTerapeutico(Base):
    __tablename__ = 'assistente_terapeutico'

    id = Column("pk_assistente_terapeutico", Integer,primary_key=True)
    nome = Column(String(120))
    telefone = Column(String(120))
    cep = Column(Integer)
    rua = Column(String(120))
    numero = Column(Integer)
    complemento = Column(String(120))
    bairro = Column(String(120))
    cidade = Column(String(120))
    estado = Column(String(120))



    def __init__(self,nome,telefone,cep,rua,numero,complemento,bairro,cidade,estado):
        self.nome = nome
        self.telefone = telefone
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f'{self.nome} | {self.telefone} | {self.cep} | {self.rua} | {self.numero} | {self.complemento} | {self.bairro} | {self.cidade} | {self.estado}'  