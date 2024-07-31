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