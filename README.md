# 📊 Food Inflation ML Docker

Este projeto contém um **modelo de Machine Learning** para previsão da inflação de alimentos. Ele foi desenvolvido dentro de um ambiente **Docker** para facilitar a execução e replicação.

![GitLab CI](https://img.shields.io/badge/GitLab-CI/CD-orange)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2.0-green)
![Docker](https://img.shields.io/badge/Docker-20.10.16-lightblue)
---

## 📌 **1. Descrição do Projeto**

Solução de machine learning para previsão de inflação de alimentos com pipeline completo de CI/CD no GitLab. Este projeto demonstra:

- Pré-processamento de dados e modelagem com Random Forest
- Containerização com Docker
- Testes automatizados e verificações de qualidade
- Integração e Deployment Contínuos

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
| **CI/CD**        | GitLab Pipelines                             |

---

## 📂 **3. Estrutura dos Arquivos**

A estrutura do repositório é a seguinte:
Estrutura

food-inflation-docker/
├── app.py # Pipeline principal de ML
├── tests/ # Testes unitários
│ └── test_app.py
├── requirements.txt # Dependências
├── Dockerfile # Configuração do container
├── .gitlab-ci.yml # Pipeline de CI/CD
└── README.md

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

## 🚀 **5. Pipeline CI/CD**

O pipeline no GitLab contém três estágios:

Lint: Verificação de qualidade de código (Pylint, Flake8)

Test: Testes unitários com relatório de cobertura

Build: Criação e push da imagem Docker