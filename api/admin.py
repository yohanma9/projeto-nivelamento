from django.contrib import admin

from .models import Cliente, Endereco, Pedido, Produto

# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        "nome",
        "sobrenome",
        "aniversario",
        "cpf",
        "rg",
        "telefone",
        "email",
        "endereco",
    ]


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = [
        "logradouro", "numero", "complemento", "bairro", "cidade", "estado"
    ]


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["produto", "descricao", "preco"]


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["cliente", "observacoes", "data", "valor", "status"]
    filter_horizontal = [
        "produtos",
    ]
