import gradio as gr
import io
import sys
from functions.validacao import validar_dados_excel

def validar_dados(caminho_arquivo):
    print(f"Validando o arquivo: {caminho_arquivo}")
    validar_dados_excel(caminho_arquivo)
    # Simulação de validação
    print("Validação concluída!")

def handle_upload(file):
    if file is None:
        return "Nenhum arquivo recebido."
    
    caminho_arquivo = file.name
    sys.stdout = io.StringIO()  # Redireciona a saída do terminal
    validar_dados(caminho_arquivo)
    output = sys.stdout.getvalue()  # Captura os prints
    sys.stdout = sys.__stdout__  # Restaura a saída padrão
    
    return output

with gr.Blocks() as app:
    gr.Markdown("## Upload de Arquivo para Validação")
    file_input = gr.File(label="Faça o upload do seu arquivo")
    output_text = gr.Textbox()
    file_input.change(handle_upload, inputs=file_input, outputs=output_text)

app.launch()
