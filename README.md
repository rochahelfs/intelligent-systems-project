# Desafio Machine Learning Engineer

Repositório de apoio do teste para a posição de Machine Learning Engineer no Elo7.

O projeto utiliza o repositório inicial como base com algumas alterações.

A parte de treinamento se encontra no diretório *training/*, o servidor se encontra no diretório *server/*.

Na pasta *data/* são mantidos os dados de treinamento e dados para testes. Quando treinado o modelo, também são salvos neste diretório um arquivo com as métricas de performance do modelo e o modelo para ser consumido.

## Treinamento

Para construir o container necessário:

```bash
docker-compose build
```

Para subir o ambiente Jupyter, execute o comando:

```bash
docker-compose up
```

Clique no link que for mostrado no terminal para abrir o ambiente. 

Dentro do ambiente, o treinamento do modelo está localizado em *training.ipynb*, com os devidos comentários.

Ao executar todo o processo, serão salvos os arquivos *model.pkl* e *metrics.txt* no diretório de dados do projeto. Esses arquivos que representam o modelo serializado e as métricas do treinamento, respectivamente.

## Servidor

Utilizei FastAPI para servir o modelo, alterando o repositório original com o que foi necessário.

### Sobre a implementação

Criei o esquema dos dados para a API considerando as colunas utilizadas no treinamento.

Os dados estão como opcionais, dessa forma para requisições sem dados para as colunas, é retornada a categoria mais frequente do treinamento do modelo (Lembrancinhas).

Há um arquivo com testes relevantes da API na pasta *tests/*

### Construindo e servindo
Para construir o container necessário:

```bash
docker-compose build
```

Para subir o servidor, execute o comando:

```bash
docker-compose up
```

Assim que o serviço subir, a API ficará disponível em http://0.0.0.0:5000.

Em http://0.0.0.0:5000/docs é possível ver o que a API pode receber de requisições e o que retorna.

#### Testes

Para testar a implementação, com o container rodando, execute o comando:

```bash
docker-compose exec api pytest
```
