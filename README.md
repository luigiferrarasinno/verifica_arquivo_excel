# Verifica Arquivo Excel

Este projeto foi desenvolvido por Luigi Ferrara e tem como objetivo validar os dados de um arquivo Excel, identificando e salvando os dados incorretos em um novo arquivo.

## Descrição

O script `main.py` utiliza a biblioteca Gradio para criar uma interface web que permite o upload de arquivos Excel para validação. O arquivo é validado com base em um esquema inferido das três primeiras linhas de cada coluna. Os dados incorretos são salvos em um novo arquivo Excel chamado `dados_incorretos.xlsx`.

## Requisitos

- Python 3.x
- Pandas
- Pandera
- Gradio

## Instalação

1. Clone este repositório:
    ```sh
    git clone <https://github.com/luigiferrarasinno/verifica_arquivo_excel.git>
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd verifica_arquivo_excel
    ```
3. Instale as dependências:
    ```sh
    pip install pandas pandera gradio
    ```

## Uso

1. Execute o script `main.py` para iniciar a interface web:
    ```sh
    python main.py
    ```
2. Acesse a interface web no seu navegador.
3. Faça o upload do arquivo Excel que deseja validar.
4. O resultado da validação será exibido na interface e, se houver dados incorretos, um arquivo `dados_incorretos.xlsx` será gerado no diretório do projeto.

## Exemplo

```python
# Exemplo de chamada da função diretamente
from functions.validacao import validar_dados_excel
validar_dados_excel("seu_arquivo.xlsx")
```