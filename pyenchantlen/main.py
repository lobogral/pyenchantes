"""Agrega un país e idioma al enchant."""
import site
import shutil
import os
import sys
import wget


def descargar_diccionario(idioma: str, pais: str) -> None:
    """Hace la descarga de archivos (.dic y .aff).

    Parameters
    ----------
    idioma
        Idioma del diccionario
    pais
        País concreto del diccionario
    """
    url = "https://cgit.freedesktop.org/libreoffice/dictionaries/plain/"
    wget.download(url + '/' + idioma + '/' + pais + '.aff', pais + '.aff')
    wget.download(url + '/' + idioma + '/' + pais + '.dic', pais + '.dic')


def main():
    """Método principal."""
    if sys.argv[1] == "--add-pais":
        # Obtiene la carpeta donde se instalan las dependencias
        # sea de entorno virtual o no
        site_packages = site.getsitepackages()[1]
        ruta_huspell = "/enchant/data/mingw64/share/enchant/hunspell/"
        ruta_tokenize = "/enchant/tokenize/"
        idioma = sys.argv[2]
        pais = sys.argv[3]

        if not os.path.isfile(site_packages + ruta_huspell + pais + '.dic'):

            # Descarga los archivos
            descargar_diccionario(idioma, pais)

            # Mueve los archivos
            shutil.move(pais + '.aff',
                        site_packages + ruta_huspell + pais + '.aff')
            shutil.move(pais + '.dic',
                        site_packages + ruta_huspell + pais + '.dic')

            # Copia el archivo de idioma
            archivo = site_packages + ruta_tokenize + idioma + ".py"
            if not os.path.isfile(archivo):
                shutil.copy(site_packages + ruta_tokenize + "en.py",
                            site_packages + ruta_tokenize + idioma + ".py")
        else:
            print("Ya existe el país, importación cancelada.")
    else:
        comando = 'pylint --disable all --enable spelling --spelling-dict '
        os.system(comando + sys.argv[1] + ' ' + sys.argv[2])


if __name__ == '__main__':
    main()
    sys.exit()
