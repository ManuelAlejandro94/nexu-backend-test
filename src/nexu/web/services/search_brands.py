from flask import request


def register_routes(app, scouts):

    @app.route('/brands', methods=['GET'])
    def search_brands():
        multimap = request.args if request.method == 'GET' else request.form
        busqueda_params = multimap.to_dict(flat=True)

        results = []
        error = None
        try:
            results = scouts.search_brands(busqueda_params)
            averages = []
            count = 0
            for result in results:
                obj = {
                    "id": count,
                    "nombre": result["_id"],
                    "average_price": result["average_price"]
                }
                averages.append(obj)
                count += 1
            return averages
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

