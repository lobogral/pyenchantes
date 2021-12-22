from setuptools import setup, find_packages


def url_release(package: str) -> str:
    """Retorna el URL faltante de un paquete.

    Retorna el URL faltante de un paquete para
    descargar el release de la última versión.
    """
    retorno = '/releases/latest/download/'
    retorno += package + '.tar.gz'
    return retorno


setup(
    name="pyenchantlen",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pylint',
        'pyenchant',
        'wget'
    ],
    entry_points={
        'console_scripts': [
            'pyenchantlen = pyenchantlen.main:main'
        ]
    }
)
