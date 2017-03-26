from setuptools import setup, find_packages

install_requires = [
    'croniter',
    'python-dateutil',
    'hug',
    'mongoengine',
]

extras = {
    'test': ['mongomock', 'pytest', 'pytest-env']
}

setup(
    name='prefect',
    version='0.0',
    description='',
    long_description=open('README.md').read(),
    url='https://gitlab.com/jlowin/prefect',
    author='jlowin',
    author_email='jlowin@apache.org',
    install_requires=install_requires,
    extras_require=extras,
    scripts=[],
    packages=find_packages(),
    include_package_data=True,)
