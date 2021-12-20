"""Agrega un país e idioma al enchant."""
import wget
import site
import shutil
import os
import sys

def descargar_diccionario(idioma: str, pais: str) -> None:
    """
    Hace la descarga de los correspondientes archivos .dic y .aff

    Parameters
    ----------
    idioma
        Idioma del diccionario
    pais
        País concreto del diccionario
    """
    
    URL = "https://cgit.freedesktop.org/libreoffice/dictionaries/plain/"
    wget.download(URL + '/' + idioma + '/' + pais + '.aff', pais + '.aff')
    wget.download(URL + '/' + idioma + '/' + pais + '.dic', pais + '.dic') 

def main():
    """Método principal."""

    if sys.argv[1] == "--agregar":
        # Obtiene la carpeta donde se instalan las dependencias
        # sea de entorno virtual o no
        site_packages = site.getsitepackages()[1]
        ruta_huspell = "/enchant/data/mingw64/share/enchant/hunspell/"
        ruta_tokenize = "/enchant/tokenize/"
        idioma = sys.argv[2]
        pais = sys.argv[3]

        if not os.path.isfile(site_packages + ruta_huspell + pais + '.dic'):

            # Descarga los archivos
            descargar_diccionario("es", "es_CO")

            # Mueve los archivos
            shutil.move(pais + '.aff',
                        site_packages + ruta_huspell + pais + '.aff')
            shutil.move(pais + '.dic',
                        site_packages + ruta_huspell + pais + '.dic')

            # Copia el archivo de idioma
            if not os.path.isfile(site_packages + ruta_tokenize + idioma + ".py"):
                shutil.copy(site_packages + ruta_tokenize + "en.py",
                            site_packages + ruta_tokenize + idioma + ".py")
        else:
            print("Ya existe el país, importación cancelada.")
    else:
        os.system('pydocstyle --convention=numpy ' + sys.argv[-1])

if __name__ == '__main__':
    main()
    sys.exit()
