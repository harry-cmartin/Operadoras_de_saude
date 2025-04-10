import pandas as pd
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import Operadora

class Command(BaseCommand):
    help = 'Impport de operadoras'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        try:
           
            df = pd.read_csv(csv_file, sep=';', encoding='utf-8')
            
            # substitui string vazia
            df.columns = df.columns.str.lower().str.replace(' ', '_')
            
            # Só funciona assim
            df['data_registro_ans'] = pd.to_datetime(df['data_registro_ans'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
            
            operadoras = []
            for _, row in df.iterrows():
                operadora = Operadora(
                    registro_ans=row['registro_ans'],
                    cnpj=row['cnpj'],
                    razao_social=row['razao_social'],
                    nome_fantasia=row['nome_fantasia'],
                    modalidade=row['modalidade'],
                    logradouro=row['logradouro'],
                    numero=row['numero'],
                    complemento=row['complemento'],
                    bairro=row['bairro'],
                    cidade=row['cidade'],
                    uf=row['uf'],
                    cep=str(row['cep']),
                    ddd=str(row['ddd']),
                    telefone=str(row['telefone']),
                    fax=str(row['fax']),
                    endereco_eletronico=row['endereco_eletronico'],
                    representante=row['representante'],
                    cargo_representante=row['cargo_representante'],
                    regiao_comercializacao=str(row['regiao_de_comercializacao']),
                    data_registro_ans=row['data_registro_ans']
                )
                operadoras.append(operadora)
            
            Operadora.objects.bulk_create(operadoras)
            
            self.stdout.write(self.style.SUCCESS(f'Sucesso importando {len(operadoras)} operadoras'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error : {str(e)}'))
