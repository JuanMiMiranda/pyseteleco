# Documentación de Uso de pyseteleco

## Introducción

La biblioteca `pyseteleco` es una herramienta diseñada para interactuar con diversos servicios catastrales y datos relacionados. 
Esta guía te mostrará cómo usar dos de sus funciones clave: `CatastroAPI.Consulta_DNPRC` y `CatastroHelper.consolidar_y_filtrar_viviendas`.

Listado de Funcionalidades:
- CatastroAPI
    -   Consulta_DNPRC

- CatastroHelper
    - consolidar_y_filtrar_viviendas   


## Instalación

Para usar `pyseteleco`, primero necesitas instalar la biblioteca. Puedes hacerlo usando `pip`:

```sh
pip install pyseteleco

```

## Usando CatastroAPI
CatastroAPI facilita la consulta de detalles catastrales desde la API de Catastro.

### Importando CatastroAPI
Primero, importa la clase CatastroAPI:
```sh
from pyseteleco.apis.CatastroAPI import CatastroAPI
```

### Función Consulta_DNPRC

Proporciona los datos catastrales no protegidos de un inmueble

        Este servicio es idéntico al de "Consulta de DATOS CATASTRALES NO
        PROTEGIDOS de un inmueble identificado por su localización" en todo
        excepto en los parámetros de entrada.

        :param str: Nombre de la provincia
        :param str: Nombre del municipio
        :param str: Referencia catastral
        :return: Retorna un dicionario con los datos de la consutla
        :rtype: dict

Para llamar a Consulta_DNPRC, necesitas proporcionar los parámetros provincia, municipio y ref_cat. En este ejemplo, dejamos provincia y municipio como cadenas vacías y proporcionamos una referencia catastral (ref_cat).

```sh
ref_cat = '28132A02500001'
resultado = CatastroAPI.Consulta_DNPRC('', '', ref_cat)
```

Esta función devuelve un JSON con los detalles de la referencia catastral.

####  Ejemplo Completo

Aquí tienes un ejemplo completo de cómo usar Consulta_DNPRC:
```sh
from pyseteleco.apis.CatastroAPI import CatastroAPI

ref_cat = '28132A02500001'
resultado = CatastroAPI.Consulta_DNPRC('', '', ref_cat)
print(resultado)
```


## Usando CatastroHelper
CatastroHelper es una clase dentro de la biblioteca pyseteleco diseñada para facilitar el manejo y procesamiento de datos catastrales obtenidos a través de la API del Catastro. Su propósito principal es transformar y consolidar la información para proporcionar un análisis más claro y útil.


### Importando CatastroHelper
Primero, importa la clase CatastroHelper:
```sh
from pyseteleco.helpers.CatastroHelper import CatastroHelper
```

### Función consolidar_y_filtrar_viviendas
Esta función consolida la información de viviendas con datos similares de la siguiente forma:

- Agrupa las viviendas por características comunes (puerta).
- Suma la superficie de las viviendas en cada grupo.
- Filtra los grupos que tienen una superficie total que cumple con el criterio especificado (por defecto, al menos 50 metros cuadrados).
- Retorna una lista de viviendas consolidadas que cumplen con el criterio de superficie, proporcionando un resumen consolidado por grupo.

#### Ejemplo completo de uso
```sh
from pyseteleco.apis.CatastroAPI import CatastroAPI
from pyseteleco.helpers.CatastroHelper import CatastroHelper

# Consulta de referencia catastral
ref_cat = '28132A02500001'
resultado = CatastroAPI.Consulta_DNPRC('', '', ref_cat)

# Creación de la instancia de CatastroHelper
helper = CatastroHelper(resultado)

# Consolidación y filtrado de viviendas
viviendas_list = helper.consolidar_y_filtrar_viviendas()
print(viviendas_list)

```

#### Ejemplo completo de resultado

```sh
from pyseteleco.helpers.CatastroHelper import CatastroHelper

# Supongamos que tenemos una respuesta JSON con datos catastrales


json_response = {
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

# Crear una instancia de CatastroHelper
helper = CatastroHelper(json_response)

# Llamar al método para consolidar y filtrar viviendas
viviendas_consolidadas = helper.consolidar_y_filtrar_viviendas()

print(viviendas_consolidadas)
# Resultado esperado: 
"""
[
            {"lcd": "VIVIENDA", "dfcons": {"stl": 55}, "dt": {"lourb": {"loint": {"pu": "01"}}}, "cons": [
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "30"}, "dt": {"lourb": {"loint": {"es": "1", "pu": "01"}}}},
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "25"}, "dt": {"lourb": {"loint": {"es": "2", "pu": "01"}}}}
                        ]},
            {"lcd": "VIVIENDA", "dfcons": {"stl": 100}, "dt": {"lourb": {"loint": {"pu": "05"}}}, "cons": [
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "50"}, "dt": {"lourb": {"loint": {"es": "1", "pu": "05"}}}},
                            {"lcd": "VIVIENDA", "dfcons": {"stl": "50"}, "dt": {"lourb": {"loint": {"es": "1", "pu": "05"}}}}
                        ]}
]
"""


```
