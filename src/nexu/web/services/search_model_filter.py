import json

from bson import json_util
from flask import request

def register_routes(app, scouts):

    def both_params(greather, lower):
        results = scouts.find_models_gl(greather, lower)
        return results

    def get_greather(greather):
        results = scouts.find_models_g(greather)
        return results

    def get_lower(lower):
        results = scouts.find_models_l(lower)
        return results

    @app.route('/models', methods=['GET'])
    def get_models():
        """greater, lower"""
        multimap = request.args if request.method == 'GET' else request.form
        busqueda_params = multimap.to_dict(flat=True)
        response = []
        results = []
        error = None

        try:
            if "greater" in busqueda_params and "lower" in busqueda_params:
                results = both_params(busqueda_params["greater"], busqueda_params["lower"])
            elif "greater" in busqueda_params:
                results = get_greather(busqueda_params["greater"])
            elif "lower" in busqueda_params:
                results = get_lower(busqueda_params["lower"])
            else:
                results = scouts.find_all_models()

            for result in results:
                obj = {
                    "id": result["_id"],
                    "name": result["name"],
                    "average_price": result["average_price"]
                }
                response.append(obj)

            return json.loads(json_util.dumps(response))

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

