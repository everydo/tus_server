import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()


setup(
    name='tusfilter',
    version='0.1.0',
    description='python wsgi filter for tus protocol 1.0.0',
    long_description=long_description,
    url='https://github.com/everydo/tusfilter',
    author='easydo.cn',
    author_email='info@easydo.cn',
    keywords='tus wsgi filter',
    license='MIT',

    py_modules=['tusfilter'],
    install_requires=['WebOb'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'License :: OSI Approved :: MIT License',
    ],

)