from __future__ import print_function
import os.path
import os
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Obter informações de data e hora da modificação do arquivo
def obter_data_mod_arquivo(caminho_arquivo):
    data_mod_timestamp = os.path.getmtime(caminho_arquivo)
    data_mod = datetime.datetime.fromtimestamp(data_mod_timestamp)
    return data_mod

# Obter o arquivo mais recente dentro de uma pasta

def obter_arquivo_mais_recente(caminho_pasta):
    arquivos = os.listdir(caminho_pasta)
    arquivos = [arquivo for arquivo in arquivos if os.path.isfile(os.path.join(caminho_pasta, arquivo))]
    data_mod_arquivos = [(arquivo, os.path.getmtime(os.path.join(caminho_pasta, arquivo))) for arquivo in arquivos]
    arquivo_mais_recente = max(data_mod_arquivos, key=lambda x: x[1])[0]
    return arquivo_mais_recente

def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Loga o usuário caso exista uma "token.json"
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            #Caso o token esteja expirado, faz um refresh nele
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Salva as credenciais para a proxima vez
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    
    # Fim da parte de autenticação do acesso

    # Ler informações do Google Sheets
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId='1o5XkucKJXtlM4eaG3IFWLBJCpj2Keoj4OKWGDgHRdFE',
                                range='BKPNuvem!B2:B2').execute()
    values = result.get('values', [])
    print(values)
    
    # Começo de teste de leitura de backup
    
    range_name = 'BKPNuvem!B:B'
    result = service.spreadsheets().values().get(
    spreadsheetId='1o5XkucKJXtlM4eaG3IFWLBJCpj2Keoj4OKWGDgHRdFE', range=range_name).execute()
    valuesraw = result.get('values', [])

    vetor_clientes = [value[0] for value in valuesraw if value]
    
    print(vetor_clientes)

    # Começo de teste de leitura de arquivos

    # Pegando o arquivo mais recente

    caminho_pasta = f'//192.168.1.211/ftp/{vetor_clientes[1]}/Bkp$implesDelphi'
    arquivo_recente = obter_arquivo_mais_recente(caminho_pasta)

    print(f"O arquivo mais recente na pasta é: {arquivo_recente}")

    # Pegando a data de modificação do arquivo mais recente
    
    caminho_arquivo = caminho_pasta
    data_mod = obter_data_mod_arquivo(caminho_arquivo)
    print(f"A data de modificação do arquivo é: {data_mod}")


"""
    # adicionar/editar valores no Google Sheets
    valores_adicionar = [
        ["Dezembro", "R$ 70.000,00"],
        ["Janeiro/22", "R$80.000,00"],
        ["Fevereiro/22", "R$127.352,00"],
    ]
    result = sheet.values().update(spreadsheetId='id_sua_planilha',
                                range='Página1!A13', valueInputOption="RAW",
                                   body={"values": valores_adicionar}).execute()
"""
if __name__ == '__main__':
    main()