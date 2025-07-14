# Usa uma imagem oficial Python
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Instala as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Comando para rodar o projeto
# Altere "main.py" para o nome do seu arquivo principal, se necessário
CMD ["python", "main.py"]