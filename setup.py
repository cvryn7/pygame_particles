from setuptools import setup
# get install_requires from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# get verson from version.py
with open('version.py') as f:
    version = f.read().splitlines()[0].split('=')[1].strip().strip('"')

setup(
    name='pygame_particles',
    version=version,
    author='Bejamin Frakline',
    description='A brief synopsis of the project',
    long_description='A much longer explanation of the project and helpful resources',
    url='https://github.com/BenjaminFranline',
    keywords='development, setup, setuptools',
    python_requires='>=3.7, <4',
    packages=['pygame_particles'],
    install_requires=requirements,
    package_data={
        'sample': ['sample_data.csv'],
    },
    entry_points={
        'runners': [
            'sample=sample:main',
        ]
    }
)