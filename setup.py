from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    README = f.read()
with open(path.join(here, 'CHANGES.txt'), encoding='utf-8') as f:
    CHANGES = f.read()


setup(
    name='uwsgi-stub',
    version='0.1.2',

    description='A stub file with correct signatures and docstrings for the python uwsgi module',
    long_description=README + '\n\n' + CHANGES,

    exclude_package_data={'': ['.gitignore']},
    zip_safe=True,

    author='Daniel Kraus',
    author_email='dakra-python@tr0ll.net',
    url='https://github.com/dakra/uwsgi-stub',
    license='ISC',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='uwsgi',
    py_modules=['uwsgi'],
)
