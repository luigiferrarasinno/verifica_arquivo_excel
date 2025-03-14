# verifica_arquivo_excel# Verifica Arquivo Excel

Este projeto foi desenvolvido por Luigi Ferrara e tem como objetivo validar os dados de um arquivo Excel, identificando e salvando os dados incorretos em um novo arquivo.

## Descrição

O script `main.py` lê um arquivo Excel, infere o esquema de dados com base nas três primeiras linhas de cada coluna e valida os dados de acordo com o esquema inferido. Os dados incorretos são salvos em um novo arquivo Excel chamado `dados_incorretos.xlsx`.

## Requisitos

- Python 3.x
- Pandas
- Pandera

## Instalação

1. Clone este repositório:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd verifica_arquivo_excel
    ```
3. Instale as dependências:
    ```sh
    pip install pandas pandera
    ```

## Uso

1. Coloque o arquivo Excel que deseja validar no diretório do projeto.
2. Edite a última linha do arquivo `main.py` para incluir o nome do seu arquivo Excel:
    ```python
    validar_dados_excel("seu_arquivo.xlsx")
    ```
3. Execute o script:
    ```sh
    python main.py
    ```

## Exemplo

```python
# Exemplo de chamada da função
validar_dados_excel("teste3.xlsx")