import pytest


from pyseteleco.helpers.CatastroHelper import CatastroHelper

class TestCatastroHelper:
    def setup_method(self):
        """
        ESTRUCTURA DE LA API DEL CATASTRO:
        -----------------------------------
        <lcons>LISTA DE UNIDADES CONSTRUCTIVAS DE CADA REF CATASTRAL </lcons>
            <cons>UNIDAD CONSTRUCTIVA </cons>
                <lcd>USO DE LA UNIDAD CONSTRUCTIVA</lcd>
                <dfcons>
                    <stl>SUPERFICIE DE LA UNIDAD CONSTRUCTIVA</stl>
                </dfcons>
                <lourb>Localización urbana </lourb>
                    <loint>LOCALIZACIÓN INTERNA (SI EXISTE)
                    <bq>BLOQUE (SI EXISTE)</bq>
                    <es>ESCALERA (SI EXISTE)</es>
                    <pt>PLANTA (SI EXISTE)</pt>
                    <pu>PUERTA (SI EXISTE)</pu>

        :return:
        """
        self.json_response = '''
        {
            "consulta_dnp": {
                "bico": {
                    "lcons": {
                        "cons": [
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "30"}, "dt": {"lourb": {"loint": {"es": "1", "pu": "01"}}}},
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "25"}, "dt": {"lourb": {"loint": {"es": "2", "pu": "01"}}}},
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "45"}, "dt": {"lourb": {"loint": {"es": "1", "pu": "04"}}}},
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "50"}, "dt": {"lourb": {"loint": {"es": "1", "pu": "05"}}}},
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "50"}, "dt": {"lourb": {"loint": {"es": "1", "pu": "05"}}}}
                        ]
                    }
                }
            }
        }
        '''
        self.helper = CatastroHelper(self.json_response)

    def test_consolidar_y_filtrar_viviendas(self):
        """
        Se esperan dos viviendas
        :return:
        """
        result = self.helper.consolidar_y_filtrar_viviendas()
        expected = [
            {"lcd": "VIVIENDA", "dfcons": {"stl": 55}, "dt": {"lourb": {"loint": {"pu": "01"}}}, "cons": [
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "30"}, "dt": {"lourb": {"loint": {"es": "1", "pu": "01"}}}},
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "25"}, "dt": {"lourb": {"loint": {"es": "2", "pu": "01"}}}}
                        ]},
            {"lcd": "VIVIENDA", "dfcons": {"stl": 100}, "dt": {"lourb": {"loint": {"pu": "05"}}}, "cons": [
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "50"}, "dt": {"lourb": {"loint": {"es": "1", "pu": "05"}}}},
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "50"}, "dt": {"lourb": {"loint": {"es": "1", "pu": "05"}}}}
                        ]}
        ]
        assert result == expected

if __name__ == "__main__":
    pytest.main()