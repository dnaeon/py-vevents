from setuptools import setup

setup(name='vevents',
      version='0.1.0',
      description='Viewing VMware vSphere Events from the command-line',
      author='Marin Atanasov Nikolov',
      author_email='dnaeon@gmail.com',
      license='BSD',
      scripts=[
        'src/vevents-cli',
      ],
      install_requires=[
        'pyvmomi >= 5.5.0',
        'docopt >= 0.6.1',
        'vconnector >= 0.2.0',  
      ]
)
