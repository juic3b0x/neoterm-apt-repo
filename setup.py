from setuptools import setup

# https://packaging.python.org/distributing/#packaging-your-project

def readme():
    with open('README.rst') as f:
        return f.read()
setup(
    name = 'neoterm-apt-repo',
    version = '0.5',
    license='Apache License 2.0',
    description = 'Script to create NeoTerm apt repositories',
    long_description = readme(),
    author = 'juic3b0x',
    author_email = '70825623+juic3b0x@users.noreply.github.com',
    url = 'https://github.com/juic3b0x/neoterm-apt-repo',
    scripts = ['neoterm-apt-repo'],
    classifiers = (
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3'
    )
)
