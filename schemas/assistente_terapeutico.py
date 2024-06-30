from pydantic import BaseModel
from typing import Optional, List
from models.assistente_terapeutico import AssistenteTerapeutico

class AssistenteTerapeuticoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Robertson Azevedo"
    telefone: Optional[int] = 123456789
    cep: int = 21999988
    rua: str = "Rua 1"
    numero: Optional[int] = 100
    complemento: Optional[str] = "A"
    bairro: str = "Centro"
    cidade: str = "Rio de Janeiro"
    estado: str = "RJ"

class AssistenteTerapeuticoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Robertson"

class ListagemAssistenteTerapeuticoSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    assistentes_terapeuticos:List[AssistenteTerapeuticoSchema]

def apresenta_assistentes_terapeuticos(assistentes_terapeuticos: List[AssistenteTerapeutico]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for assistente_terapeutico in assistentes_terapeuticos:
        result.append({
            "nome": assistente_terapeutico.nome,
            "telefone": assistente_terapeutico.telefone,
            "cep": assistente_terapeutico.cep,
            "rua": assistente_terapeutico.rua,
            "numero": assistente_terapeutico.numero,
            "complemento": assistente_terapeutico.complemento,
            "bairro": assistente_terapeutico.bairro,
            "cidade": assistente_terapeutico.cidade,
            "estado": assistente_terapeutico.estado,
        })

    return {"assistentes_terapeuticos": result}

class AssistenteTerapeuticoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    nome: str = "Robertson"
    telefone: int = 2199998888
    cep: int = 21999988
    rua: str = "Rua 1"
    numero: int = 100
    complemento: Optional[str] = "A"
    bairro: str = "Centro"
    cidade: str = "Rio de Janeiro"
    estado: str = "RJ"

class AssistenteTerapeuticoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str

def apresenta_assistente_terapeutico(assistente_terapeutico: AssistenteTerapeutico):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": assistente_terapeutico.id,
        "nome": assistente_terapeutico.nome,
        "telefone": assistente_terapeutico.telefone,
        "cep": assistente_terapeutico.cep,
        "rua": assistente_terapeutico.rua,
        "numero": assistente_terapeutico.numero,
        "complemento": assistente_terapeutico.complemento,
        "bairro": assistente_terapeutico.bairro,
        "cidade": assistente_terapeutico.cidade,
        "estado": assistente_terapeutico.estado
    }
