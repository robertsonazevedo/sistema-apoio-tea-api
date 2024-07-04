from pydantic import BaseModel
from typing import Optional, List
from models.assistente_terapeutico import AssistenteTerapeutico

class AssistenteTerapeuticoSchema(BaseModel):
    """ Define como um novo terapeuta deve inserido e ser representado
    """
    nome: str = "Robertson Azevedo"
    telefone: Optional[int] = 2199995555
    cep: int = 24452001
    rua: str = "Rua 1"
    numero: Optional[int] = 100
    complemento: Optional[str] = "A"
    bairro: str = "Centro"
    cidade: str = "Rio de Janeiro"
    estado: str = "RJ"

class AssistenteTerapeuticoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do assistente terapeutico.
    """
    nome: str = "Robertson"

class AssistenteTerapeuticoBuscaEstadoSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca por estado. Que será
        feita apenas com base na UF do assistente terapeutico.
    """
    estado: str = "RJ"

class ListagemAssistenteTerapeuticoSchema(BaseModel):
    """ Define como uma listagem de terapeutas será retornada.
    """
    assistentes_terapeuticos:List[AssistenteTerapeuticoSchema]

def apresenta_assistentes_terapeuticos(assistentes_terapeuticos: List[AssistenteTerapeutico]):
    """ Retorna uma representação do terapeuta seguindo o schema definido em
        AssitenteTerapeuticoViewSchema.
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
    """ Define como um assistente terapeutico será retornado: Assistente Terapeutico.
    """
    id: int = 1
    nome: str = "Robertson"
    telefone: Optional[int] = 2199998888
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
    """ Retorna uma representação do assistente terapeutico seguindo o schema definido em
        AssitenteTerapeuticoViewSchema.
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


class ListagemUfAssistenteTerapeuticoSchema(BaseModel):
    """ Define como uma listagem de UF de terapeutas cadastrados será retornada.
    """
    assistentes_terapeuticos_uf:List[AssistenteTerapeuticoSchema]

def apresenta_ufs_assistentes_terapeuticos(assistentes_terapeuticos_uf: List[AssistenteTerapeutico]):
    """ Retorna uma representação de UF de terapeutas cadastrasdos seguindo o schema definido em
        AssitenteTerapeuticoViewSchema, apenas as UF.
    """
    result = []
    for assistente_terapeutico in assistentes_terapeuticos_uf:
        result.append({
            "estado": assistente_terapeutico.estado,
        })

    return {"assistentes_terapeuticos": result}