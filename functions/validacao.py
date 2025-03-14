import pandas as pd
import pandera as pa

def validar_dados_excel(file_path):
    """Valida os dados de um arquivo Excel e salva os dados incorretos em um novo arquivo."""
    
    df = pd.read_excel(file_path)

    def infer_schema(df):
        """Infere o esquema de um DataFrame com base nas 3 primeiras linhas de cada coluna."""
        schema_dict = {}

        for col in df.columns:
            first_3_rows = df[col].dropna().head(3)  # Pega as 3 primeiras linhas não nulas
            
            # Se todos os valores são numéricos (int ou float)
            if first_3_rows.apply(lambda x: isinstance(x, (int, float)) and not isinstance(x, bool)).all():
                if first_3_rows.apply(lambda x: isinstance(x, int)).all():
                    schema_dict[col] = pa.Column(int, nullable=True)  # Inteiro
                else:
                    schema_dict[col] = pa.Column(float, nullable=True)  # Float
            else:
                schema_dict[col] = pa.Column(str, nullable=True)  # String
            
        return pa.DataFrameSchema(schema_dict)

    # Criar esquema Pandera com inferência aprimorada
    schema = infer_schema(df)
    #print(schema)

    # Mapeamento de tipos do Pandera/Numpy para Python
    dtype_mapping = {
        "int64": int,
        "float64": float,
        "str":str,
        "object": str
    }

    # Lista para armazenar os dados incorretos
    dados_incorretos = []

    # Percorrer todas as colunas e validar os dados
    for coluna in df.columns:
        dtype_esperado = schema.columns[coluna].dtype  # Tipo esperado da coluna
        tipo_python = dtype_mapping.get(str(dtype_esperado), object)  # Converte para tipo Python

        print(f"📌 Coluna: {coluna} (Tipo esperado: {tipo_python})")

        for index, valor in df[coluna].items():
            if pd.isna(valor):
                print(f"  🚫 Linha {index}: {valor} (nulo)")
            elif isinstance(valor, pd.Timestamp):
                print(f"  🕒 Linha {index}: {valor} (Timestamp)")
            elif type(valor) == tipo_python:
                print(f"  ✅ Linha {index}: {valor} (Correto)")
            else:
                # Adiciona os dados incorretos na lista
                dados_incorretos.append({
                'Coluna': coluna,
                'Linha': index,
                'Valor Esperado': tipo_python,
                'Valor Atual': type(valor),
                'Dado Incorreto': valor
                })
                print(f"  ❌ Linha {index}: {valor} (Erro: esperado {tipo_python}), valor atual {type(valor)})")
            
        print("-" * 40)  # Separador visual

    # Se houver dados incorretos, cria um arquivo Excel
    if dados_incorretos:
        df_incorretos = pd.DataFrame(dados_incorretos)
        output_file = 'dados_incorretos.xlsx'
        df_incorretos.to_excel(output_file, index=False)
        print(f"Arquivo com dados incorretos salvo em: {output_file}")
    else:
        print("Nenhum dado incorreto encontrado.")

# Exemplo de chamada da função
#validar_dados_excel("teste3.xlsx")