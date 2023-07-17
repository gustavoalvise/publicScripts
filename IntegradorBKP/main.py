from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


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

    # Call the Sheets API
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
    values = result.get('values', [])

    vetor = [value[0] for value in values if value]
    
    print(vetor)
       
    
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