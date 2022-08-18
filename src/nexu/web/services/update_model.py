from flask import request

def register_routes(app, scouts):

    @app.route('/models/<id>', methods=['PUT'])
    def put_models(id):
        """id: name, average_price"""
        busqueda_params = request.get_json()

        if busqueda_params["average_price"] <= 100000:
            return {
                "error_code": -2,
                "message": "average_price must be greather than 100,000"
            }, 422

        error = None
        try:
            results = scouts.find_by_model(id)
            if results and len(list(results)) > 0:
                params = {
                    "_id": results["_id"],
                    "name": results["name"],
                    "brand_name": results["brand_name"],
                    "average_price": busqueda_params["average_price"]
                }
                scouts.update_model(params)
            else:
                return {
                    "error_code": -1,
                    "message": "Model not found"
                }

            return {
                       "code": 0,
                       "message": "Model updated successfully"
                   }, 200
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

