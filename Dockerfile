# Usa imagem base oficial estável do Python 3.12
FROM python:3.12-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Instala dependências do sistema que podem ser necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos do projeto, incluindo o banco SQLite
COPY . .

# Cria e ativa um ambiente virtual isolado
# ENV VIRTUAL_ENV=/opt/venv
# RUN python -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Instala as dependências listadas
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expõe a porta que o Flask usa
EXPOSE 5000

# Define variáveis para rodar o Flask corretamente
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Define volume opcional para persistência do SQLite
VOLUME ["/app/database.db"]

# Comando padrão para iniciar a aplicação
CMD ["flask", "run"]
