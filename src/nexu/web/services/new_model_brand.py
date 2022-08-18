from flask import request

def register_routes(app, scouts):

    @app.route('/brands/<id>/models', methods=['POST'])
    def post_models(id):
        """id: brand_name, name, average_price"""
        busqueda_params = request.get_json()

        if busqueda_params["average_price"] <= 100000:
            return {
                "error_code": -2,
                "message": "average_price must be greather than 100,000"
            }, 422

        response = []
        error = None
        model = busqueda_params["name"]
        try:
            results = scouts.find_by_model_brand(id, None)
            if results and len(list(results)) > 0:
                params = {
                    "_id": results["_id"],
                    "name": results["name"],
                    "brand_name": results["brand_name"],
                    "average_price": busqueda_params["average_price"]
                }
                scouts.update_model_empty(params)
            else:
                results = scouts.find_by_model_brand(id, model)
                if results and len(list(results)) > 0:
                    return {
                               "error_code": -1,
                               "message": "Model already exists"
                           }, 422
                else:
                    results = scouts.find_by_brand(id)
                    if results and len(list(results)) <= 0:
                        return {
                            "error_code": -1,
                            "message": "Not exist brand"
                        }, 422
                    params = {
                        "_id": results["_id"],
                        "name": results["name"],
                        "brand_name": id,
                        "average_price": busqueda_params["average_price"]
                    }
                    scouts.insert_model(params)

            return {
                       "code": 0,
                       "message": "Model added successfully"
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

