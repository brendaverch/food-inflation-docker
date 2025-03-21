# 📊 Food Inflation ML Docker

Este projeto contém um **modelo de Machine Learning** para previsão da inflação de alimentos. Ele foi desenvolvido dentro de um ambiente **Docker** para facilitar a execução e replicação.

---

## 📌 **1. Descrição do Projeto**

O objetivo deste projeto é analisar a inflação de alimentos utilizando um dataset do **Kaggle** e um modelo preditivo simples. Para isso, utilizamos **Python**, bibliotecas de ciência de dados, e empacotamos tudo em um **container Docker** para garantir um ambiente padronizado.

O container Docker contém:
- Um script app.py que faz a leitura do dataset, pré-processamento e treinamento do modelo.
- Um Dockerfile que define a imagem para execução do projeto.
- Um requirements.txt listando todas as bibliotecas necessárias.

---

## 🛠 **2. Tecnologias Utilizadas**

O projeto foi desenvolvido com as seguintes tecnologias:

| Tecnologia        | Descrição                                      |
|------------------|----------------------------------------------|
| **Python 3.9**   | Linguagem principal para análise e modelagem |
| **Docker**       | Para empacotar e executar o ambiente isolado |
| **Scikit-Learn** | Biblioteca para aprendizado de máquina       |
| **Pandas & NumPy** | Manipulação e análise de dados             |
| **GitHub**       | Controle de versão e repositório do projeto  |

---

## 📂 **3. Estrutura dos Arquivos**

A estrutura do repositório é a seguinte:
Estrutura

- app.py - Script principal que lê o CSV, treina e avalia o modelo.
- requirements.txt - Bibliotecas necessárias (pandas, numpy, scikit-learn, etc.).
- Dockerfile - Define a imagem Docker.
- .dockerignore - Ignora arquivos/pastas desnecessárias.

## 🚀 **4. Como Rodar o Docker**

### 1️⃣ Baixar a Imagem do Docker Hub

``` bash
docker pull brendaverch/food-inflation:1.0
```
### 2️⃣ Executar o Container

``` bash
docker run brendaverch/food-inflation:1.0
```

Isso irá rodar o script app.py, que carrega o dataset, realiza o pré-processamento, treina o modelo e exibe as métricas de avaliação no terminal.
