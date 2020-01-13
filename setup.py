from setuptools import setup, find_packages

setup(name='maboss_test',
    version="1.0.0",
    author="Nicolas Levy",
    author_email="nicolaspierrelevy@gmail.com",
    description="A python and jupyter api for the MaBoSS software",
	install_requires = ['maboss'],
	packages=['maboss_test'],
)
