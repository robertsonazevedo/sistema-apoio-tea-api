from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from models import Session, AssistenteTerapeutico
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Sistema de Apoio ao TEA", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
assistente_terapeutico_tag = Tag(name="Assistente Terapeutico", description="Adição, visualização e remoção de assistentes terapeuticos à base")
comentario_tag = Tag(name="Comentario", description="Adição de um comentário à um produtos cadastrado na base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/assistente_terapeutico', tags=[assistente_terapeutico_tag],
          responses={"200": AssistenteTerapeuticoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_assistente_terapeutico(form: AssistenteTerapeuticoSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos assistentes terapeuticos e comentários associados.
    """
    assistente_terapeutico = AssistenteTerapeutico(
        nome = form.nome,
        telefone = form.telefone,
        cidade = form.cidade,
        estado = form.estado)
    logger.debug(f"Adicionando assistente_terapeutico de nome: '{assistente_terapeutico.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(assistente_terapeutico)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado assistente_terapeutico de nome: '{assistente_terapeutico.nome}'")
        return apresenta_assistente_terapeutico(assistente_terapeutico), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Assistente Terapeutico de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar assistente_terapeutico  '{assistente_terapeutico.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo assistente_terapeutico:/"
        logger.warning(f"Erro ao adicionar assistente_terapeutico  '{assistente_terapeutico.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/assistentes_terapeuticos', tags=[assistente_terapeutico_tag],
         responses={"200": ListagemAssistenteTerapeuticoSchema, "404": ErrorSchema})
def get_assistentes_terapeuticos():
    """Faz a busca por todos os assistentes terapeuticos cadastrados

    Retorna uma representação da listagem de assistentes terapeuticos.
    """
    logger.debug(f"Coletando assistentes terapeuticos")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    assistentes_terapeuticos = session.query(AssistenteTerapeutico).all()

    if not assistentes_terapeuticos:
        # se não há produtos cadastrados
        return {"assistentes_terapeuticos": []}, 200
    else:
        logger.debug(f"%d ASssistentes terapeuticos econtrados" % len(assistentes_terapeuticos))
        # retorna a representação de produto
        print(assistentes_terapeuticos)
        return apresenta_assistentes_terapeuticos(assistentes_terapeuticos), 200


@app.get('/assistente_terapeutico', tags=[assistente_terapeutico_tag],
         responses={"200": AssistenteTerapeuticoViewSchema, "404": ErrorSchema})
def get_assistente_terapeutico(query: AssistenteTerapeuticoBuscaSchema):
    """Faz a busca por um assistente terapeutico a partir da cidade solicitada

    Retorna uma representação dos assistentes terapeuticos e comentários associados.
    """
    terapeuta_nome = query.nome
    logger.debug(f"Coletando dados sobre assistentes terapeuticoa #{terapeuta_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    assistente_terapeutico = session.query(AssistenteTerapeutico).filter(AssistenteTerapeutico.nome == terapeuta_nome).first()

    if not assistente_terapeutico:
        # se o produto não foi encontrado
        error_msg = "Assistente terapeutico não encontrado na base :/"
        logger.warning(f"Erro ao buscar assistente terapeutico '{terapeuta_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Assistente terapeutico encontrado: '{assistente_terapeutico.nome}'")
        # retorna a representação de produto
        return apresenta_assistente_terapeutico(assistente_terapeutico), 200


@app.delete('/assistente_terapeutico', tags=[assistente_terapeutico_tag],
            responses={"200": AssistenteTerapeuticoDelSchema, "404": ErrorSchema})
def del_assistente_terapeutico(query: AssistenteTerapeuticoBuscaSchema):
    """Deleta um assistente terapeutico a partir do nome de assistente terapeutico informado

    Retorna uma mensagem de confirmação da remoção.
    """
    assistente_terapeutico_nome = unquote(unquote(query.nome))
    print(assistente_terapeutico_nome)
    logger.debug(f"Deletando dados sobre assistente terapeutico #{assistente_terapeutico_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(AssistenteTerapeutico).filter(AssistenteTerapeutico.nome == assistente_terapeutico_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado assistente terapeutico #{assistente_terapeutico_nome}")
        return {"mesage": "Assistente terapeutico removido", "id": assistente_terapeutico_nome}
    else:
        # se o produto não foi encontrado
        error_msg = "Assistente terapeutico não encontrado na base :/"
        logger.warning(f"Erro ao deletar assistente terapeutico #'{assistente_terapeutico_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
