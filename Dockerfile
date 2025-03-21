# Usa uma imagem base oficial do Python
FROM python:3.9-slim

# Mantainer 
LABEL maintainer="Brenda Verch <brenda_verch@hotmail.com>"

# Cria uma pasta /app no container
WORKDIR /app

# Copia o arquivo de requisitos primeiro
COPY requirements.txt /app

# Instala as bibliotecas
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o restante do código
COPY . /app

# Comando padrão ao iniciar o container
# Este comando vai rodar o script "app.py"
CMD ["python", "app.py"]
