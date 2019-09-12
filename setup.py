from setuptools import setup

setup(name='doltpy',
      version='0.1',
      packages=['doltpy', 'doltpy_etl'],
      install_requires=['pandas>=0.25.0', 'pyarrow>=0.14.1'],
      author='Liquidata',
      author_email='oscar@liquidata.co',
      description='',
      url='https://github.com/liquidata-inc/doltpy',
      project_urls={'Bug Tracker': 'https://github.com/liquidata-inc/doltpy/issues'})