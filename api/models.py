from django.db import models

class Operadora(models.Model):
    registro_ans = models.CharField(max_length=20, primary_key=True)
    cnpj = models.CharField(max_length=20)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255, blank=True)
    modalidade = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    ddd = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, blank=True)
    endereco_eletronico = models.EmailField(max_length=255, blank=True)
    representante = models.CharField(max_length=255)
    cargo_representante = models.CharField(max_length=100)
    regiao_comercializacao = models.CharField(max_length=2)
    data_registro_ans = models.DateField()

    class Meta:
        db_table = 'operadoras'
        ordering = ['razao_social']

    def __str__(self):
        return f"{self.razao_social} (ANS: {self.registro_ans})"
