#need to edit for my project
# look at what Anne has in hers, will have to iterate to figure out what imports you need
#keep looking for places that say project name all over

import os
import re

from codecs import open as copen  # to use a consistent encoding
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

# get the long description from the relevant file
with copen(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def read(*parts):
    with copen(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


__version__ = find_version('kg_envpolyreg', '__version__.py')

test_deps = [
    'pytest',
    'pytest-cov',
    'coveralls',
    'validate_version_code',
    'codacy-coverage',
    'parameterized'
]

extras = {
    'test': test_deps,
}

setup(
    name='kg_envpolyreg',
    version=__version__,
    description='KG hub for kg_envpolyreg',
    long_description=long_description,
    url='https://github.com/Knowledge-Graph-Hub/kg_envpolyreg',
    author='Lauren Chan',
    author_email='chanl@oregonstate.edu',
    python_requires='>=3.7',

    # choose your license
    license='BSD-3',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    tests_require=test_deps,
    # add package dependencies
    install_requires=[
        'tqdm',
        'wget',
        'compress_json',
        'click',
        'pyyaml',
        'kgx',
        'sphinx',
        'sphinx_rtd_theme',
        'recommonmark',
        'parameterized',
        'validate_version_code',
        'pandas',
        'networkx',
        # Extra packages added
        'six', # needed by rdflib
        'ordered-set', #needed by kgx
        'requests', # needed by kgx
        'ShExJSG', # needed by linkml-runtime
        'jsonasobj==1.2.1', #deprecated # needed by kgx
        'prefixcommons', # needed by kgx
        'packaging', #needed by deprecation
        'cachetools', # needed by kgx
        'jsonlines', # needed by kgx
        'neo4jrestclient', # needed by kgx
        'validators', # needed by kgx
        'stringcase', # needed by kgx
        'linkml_model', # needed by kgx
        'isodate', # needed by rdflib
        'deprecated', # needed by linkml-runtime
        'hbreader', # needed by jsonasobj
        'bmt', # needed by kgx
        'jsonstreams', # needed by kgx
        'ijson', # needed by kgx
    ],
    extras_require=extras,
)
