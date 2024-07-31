from setuptools import setup, find_packages

setup(
    name='pyseteleco',
    version='0.0.3',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    url='https://github.com/JuanMiMiranda/pyseteleco',
    license='GPLv3',
    author='JuanMi',
    author_email='juan.miranda@digital.gob.es',
    install_requires=[
        'pycatastro'
    ],
    description='Modulo SETELECO'
)