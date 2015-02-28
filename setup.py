
from setuptools import setup, find_packages

setup_args = dict(
    name = 'itc',
    version = '0.1',
    author = 'Sergei Syrov',
    author_email = 'me@sergelab.ru',
    url = '',
    description = 'ITCProject',
    long_description = open('README.md').read(),
    install_requires = [
        'setuptools',
        'zc.buildout',
    ],
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    zip_safe = True
)

if __name__ == '__main__':
    setup(**setup_args)
