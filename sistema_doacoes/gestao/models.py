from django.db import models


class Doador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome


class Beneficiario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Item(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Doacao(models.Model):
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantidade} x {self.item.nome} de {self.doador.nome} para {self.beneficiario.nome}"


from django.db import models

# Create your models here.
