import graphene
from graphene import ObjectType, Int, String, Float, Boolean, Field, List
from .data import productos

# Definicion de los tipos de datos para ser usados por GraphQL
class ProductoType(ObjectType  ):
    id = Int()
    nombre = String()
    precio = Float()
    stock = Int()
    disponible = Boolean()

# DEfinicion de la consulta
class Query(ObjectType):
    productos = List(ProductoType)

    def resolve_productos(self, info):
        return productos
    
# Mutation para cambiar el stock del producto
class ModificarStock(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        cantidad = Int(required=True)

    producto = Field(lambda:ProductoType)

    def mutate(self, info, id, cantidad):
        for p in productos:
            if p["id"] == id:
                p["stock"] += cantidad
                if p["stock"] <= 0:
                    p["stock"] = 0
                    p["disponible"] = False
                else:
                    p["disponible"] = True
                return ModificarStock(producto=p)
        raise Exception("Producto no encontrado")
    
#Mutacivon disponible
class Mutation(graphene.ObjectType):
    modificarStock  = ModificarStock.Field()

# Definicion del esquema
schema = graphene.Schema(query=Query, mutation=Mutation)