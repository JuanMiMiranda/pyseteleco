import json


class CatastroHelper:
    def __init__(self, json_response):
        self.data = json.loads(json_response)

    def consolidar_y_filtrar_viviendas(self):
        """Consolida viviendas con la misma puerta y filtra aquellas con superficie total >= 50 metros.

        :return: Lista de viviendas consolidadas que cumplen con el criterio de superficie
        :rtype: list
        """
        # Obtener todas las viviendas
        viviendas = self.superficie_vivienda_entre(0)

        # Diccionario para consolidar viviendas por puerta
        viviendas_consolidadas = {}

        for vivienda in viviendas:
            # Extraer la puerta
            puerta = vivienda.get('dt', {}).get('lourb', {}).get('loint', {}).get('pu', '')

            # Inicializar la superficie si la puerta no está en el diccionario
            if puerta not in viviendas_consolidadas:
                viviendas_consolidadas[puerta] = {
                    'lcd': 'VIVIENDA',
                    'dfcons': {'stl': 0},
                    'dt': {'lourb': {'loint': {'pu': puerta}}}
                }

            # Sumar la superficie de la vivienda actual
            viviendas_consolidadas[puerta]['dfcons']['stl'] += int(vivienda['dfcons']['stl'])

        # Filtrar las viviendas consolidadas que tienen superficie total >= 50 metros
        viviendas_filtradas = [
            vivienda for vivienda in viviendas_consolidadas.values()
            if vivienda['dfcons']['stl'] >= 50
        ]

        return viviendas_filtradas

    def superficie_vivienda_entre(self, min_surface, max_surface=float('inf')):
        """Filtra las viviendas cuyo valor de superficie está entre los valores especificados.
            :param min_surface: Superficie mínima
            :param max_surface: Superficie máxima (opcional, por defecto es infinito)
            :return: Lista de viviendas que cumplen con el rango de superficie
            :rtype: list
        """
        # Accede a la lista de viviendas desde la estructura JSON
        cons = self.data.get('consulta_dnp', {}).get('bico', {}).get('lcons', {}).get('cons', [])

        # Filtrar las viviendas con superficie dentro del rango especificado
        viviendas_filtradas = [
            vivienda for vivienda in cons
            if vivienda.get('lcd') == 'VIVIENDA'
               and min_surface <= int(vivienda.get('dfcons', {}).get('stl', '0')) <= max_surface
        ]
        return viviendas_filtradas