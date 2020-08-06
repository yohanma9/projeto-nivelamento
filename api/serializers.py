from rest_framework import serializers

from .models import Cliente, Endereco, Pedido, Produto


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:

        model = Endereco
        exclude = ["deleted"]


class ClienteSerializer(serializers.ModelSerializer):

    endereco = EnderecoSerializer()

    class Meta:

        model = Cliente
        exclude = [
            "deleted",
            "is_active",
            "date_joined",
            "last_login",
            "user_permissions",
            "groups",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "is_staff",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.get("password")
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        password = validated_data.get("password")
        if password:
            instance.set_password(password)
            instance.save()
        return instance


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:

        model = Produto
        exclude = ["deleted"]


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:

        model = Pedido
        exclude = ["deleted"]
