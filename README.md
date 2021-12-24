# pyenchantlen

Corrector ortográfico de docstrings en python simplificado basado en pyenchant.

Podría decirse que el código expresado aquí es una envolura de pyenchant con pylint para que funcione exclusivamente como corrector ortográfico de docstrings en python, y evitar comandos complicados [^fn3].

## Instalación

Para instalar la versión más reciente de ``pyenchantlen`` usando pip:

1. Descargar el archivo .tar.gz mediante el siguiente [link](https://github.com/lobogral/pyenchantlen/releases/latest/download/pyenchantlen.tar.gz).

2. Ejecutar el comando:

        $ pip install pyenchantlen.tar.gz

Si se desea instalar para desarrollo, ejecutar lo siguiente:

    $ git clone https://github.com/lobogral/pyenchantlen.git
    $ cd pyenchantlen
    $ pip install -e .

## Ejecución

Sólo es necesario escribir el comando, el código del país, y la carpeta o archivo a analizar, por ejemplo:

    $ pyenchantlen es_CO dist.py
    
## Agregar diccionario
    
Si se desea agregar un diccionario de otro país (se utilizan diccionarios de LibreOffice [^fn1][^fn2]), incluso si no se usa el idioma español, se puede usar el comando, con idioma y país, por ejemplo:

    $ pyenchantlen --add-pais es es_AR 
    
[^fn1]: https://pyenchant.github.io/pyenchant/install.html

[^fn2]: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/

[^fn3]: https://stackoverflow.com/questions/27162315/automated-docstring-and-comments-spell-check
