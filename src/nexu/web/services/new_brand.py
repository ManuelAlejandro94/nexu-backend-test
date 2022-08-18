from flask import request

def register_routes(app, scouts):

    @app.route('/brands', methods=['POST'])
    def post_brand():
        busqueda_params = request.get_json()

        response = []
        error = None
        try:
            results = scouts.find_by_brand(busqueda_params["name"])
            if len(list(results)) > 0:
                return {
                    "error_code": -1,
                    "message": "Already exists"
                }, 422
            scouts.insert_brand(busqueda_params["name"])
            return {
                "code": 0,
                "message": "Brand added successfully"
            }, 201
        except Exception as e:
            error = {
                "codigo": str(e.error.value[0].value[0]) + "." + str(e.error.value[1]),
                "detalle": str(e.detalle),
                "mensaje": str(e.args[0])
            }
            raise e
        except Exception as e:
            error = e
            raise e

