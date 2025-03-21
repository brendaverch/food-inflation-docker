# Food Inflation ML Docker

Este projeto contém um script de Machine Learning que lê dados de inflação (CPI_dataset.csv), faz pré-processamento e treina um modelo de regressão.

## 📂 Estrutura

- `app.py` - Script principal que lê o CSV, treina e avalia o modelo.
- `requirements.txt` - Bibliotecas necessárias (pandas, numpy, scikit-learn, etc.).
- `Dockerfile` - Define a imagem Docker.
- `.dockerignore` - Ignora arquivos/pastas desnecessárias.

## 🚀 Como Rodar o Docker

### 1️⃣ Baixar a Imagem do Docker Hub

```bash
docker pull brendaverch/food-inflation:1.0
