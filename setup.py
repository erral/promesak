from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='promesak',
      version=version,
      description="Promesak, promesak, promesak",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Mikel Larreategi',
      author_email='mlarreategi@codesyntax.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'django',
          'gunicorn',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
