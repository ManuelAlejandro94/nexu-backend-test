from enum import Enum


class Paises(object):
    def __init__(self, pais, id):
        self.pais = pais
        self.id = id


class PaisesList(Paises, Enum):
    MEXICO = ("mexico", 1)
    PANAMA = ("panama", 2)


def pais_from_id(id) -> 'PaisesList':
    for tipo in PaisesList:
        if tipo.id == id:
            return tipo.pais


def validate_parameters(parametros, request):
    for parametro in parametros.keys():
        for validacion in parametros[parametro]:
            validacion.is_valid(argument=request.get(parametro), parameter=parametro)


def is_blank(string):
    return not (string and string.strip())
