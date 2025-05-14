from flask import Flask, request, jsonify
from flask_cors import CORS
import graphene

class Producto(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
    precio = graphene.Float()
    stock = graphene.Int()
    disponible = graphene.Boolean()

productos = [
    {"id": 1, "nombre": "Ferrari", "precio": 500000, "stock": 3, "disponible": True},
    {"id": 2, "nombre": "Mercedes a45 AMG", "precio": 60000, "stock": 6, "disponible": True},   
    {"id": 3, "nombre": "BMW m4", "precio": 130000, "stock": 4, "disponible": True},

]

class Query(graphene.ObjectType):
    productos = graphene.List(Producto)

    def resolve_productos(self, info):
        return productos

class ModificarStock(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        cantidad = graphene.Int(required=True)

    producto = graphene.Field(Producto)

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

# ==== DECLARACIÓN DE MUTACIONES ====
class Mutation(graphene.ObjectType):
    modificar_stock = ModificarStock.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
CORS(app) 

@app.route("/graphql", methods=["GET", "POST", "OPTIONS"])
def graphql_server():
    if request.method == "OPTIONS":
        response = app.make_default_options_response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return response

    if request.method == "GET":
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>GraphiQL</title>
            <link href="https://unpkg.com/graphiql/graphiql.min.css" rel="stylesheet" />
        </head>
        <body style="margin: 0;">
            <div id="graphiql" style="height: 100vh;"></div>
            <script crossorigin src="https://unpkg.com/react/umd/react.production.min.js"></script>
            <script crossorigin src="https://unpkg.com/react-dom/umd/react-dom.production.min.js"></script>
            <script crossorigin src="https://unpkg.com/graphiql/graphiql.min.js"></script>
            <script>
            const graphQLFetcher = graphQLParams =>
                fetch('/graphql', {
                    method: 'post',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(graphQLParams),
                }).then(response => response.json());

            ReactDOM.render(
                React.createElement(GraphiQL, { fetcher: graphQLFetcher }),
                document.getElementById('graphiql'),
            );
            </script>
        </body>
        </html>
        '''

    elif request.method == "POST":
        data = request.get_json()
        if not data or "query" not in data:
            return jsonify({"error": "No query provided"}), 400

        result = schema.execute(
            data["query"],
            variable_values=data.get("variables"),
            operation_name=data.get("operationName")
        )

        response = {}
        if result.errors:
            response["errors"] = [str(error) for error in result.errors]
        if result.data:
            response["data"] = result.data
        return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
