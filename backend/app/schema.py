import graphene
from graphene import ObjectType, Int, String, Float, Boolean, Field, List
from .data import productos

class ProductoType(ObjectType):
    id = Int()
    nombre = String()
    precio = Float()
    stock = Int()
    disponible = Boolean()

class Query(ObjectType):
    productos = List(ProductoType)

    def resolve_productos(root, info):
        return productos

class ModificarStock(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        cantidad = Int(required=True)

    producto = Field(lambda: ProductoType)

    def mutate(self, info, id, cantidad):
        for prod in productos:
            if prod["id"] == id:
                prod["stock"] += cantidad
                if prod["stock"] <= 0:
                    prod["stock"] = 0
                    prod["disponible"] = False
                else:
                    prod["disponible"] = True
                return ModificarStock(producto=prod)
        raise Exception("Producto no encontrado")

class Mutation(ObjectType):
    modificar_stock = ModificarStock.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
