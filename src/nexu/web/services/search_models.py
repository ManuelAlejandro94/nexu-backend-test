from flask import request

def register_routes(app, scouts):

    @app.route('/brands/<id>/models', methods=['GET'])
    def search_by_brand(id):
        """id: brand_name"""
        multimap = request.args if request.method == 'GET' else request.form
        busqueda_params = multimap.to_dict(flat=True)

        response = []
        error = None
        try:
            results = scouts.find_by_brand(id)
            for result in results:
                obj = {
                    "id": result["_id"],
                    "name": result["name"],
                    "average_price": result["average_price"]
                }
                response.append(obj)
            return response
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

