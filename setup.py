from setuptools import setup
import re


requirements = []

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = ''
with open('__init__.py') as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('readme.md') as f:
    readme = f.read()

setup(name='SpaceAc_tools',
      version=version,
      description='A Python wrapper for the Space c Ground station',
      long_description=readme,
      url='https://github.com/Retaehc-pop/SpaceAc_tools',
      author='Retaehc_pop',
      author_email='Papop2003@gmail.com',
      license='MIT',
      zip_safe=False,
      install_requires=requirements,
      python_requires='>3.8.0')
