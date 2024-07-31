from pycatastro import PyCatastro
import json

class CatastroAPI:
    _pycatastro = PyCatastro  # Atributo de clase privado
    @staticmethod
    def funcion2():
        return "Hola desde CatastroAPI - funcion2!"
    @classmethod
    def ConsultaProvincia(cls):
        res = cls._pycatastro.ConsultaProvincia()
        json_content = json.dumps(res, indent=4)
        return json_content

    @classmethod
    def Consulta_DNPRC(cls, provincia, municipio, rc):
        """Proporciona los datos catastrales no protegidos de un inmueble

        Este servicio es idéntico al de "Consulta de DATOS CATASTRALES NO
        PROTEGIDOS de un inmueble identificado por su localización" en todo
        excepto en los parámetros de entrada.

        :param str: Nombre de la provincia
        :param str: Nombre del municipio
        :param str: Referencia catastral
        :return: Retorna un dicionario con los datos de la consutla
        :rtype: dict
        """
        res = PyCatastro.Consulta_DNPRC(provincia, municipio, rc)
        json_content = json.dumps(res, indent=4)
        return json_content