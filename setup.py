from setuptools import setup




setup(name='synonym_finder',
      version='0.0.1',
      description='This package consists of synonym finder class ',
      url='https://dev.azure.com/aloui0979/_git/synonym_finder',
      author='Aloui Amine',
      author_email='aloui@eurecom.fr',
      license='MIT',
      packages=['synonym_finder'],
      install_requires=['pywikibot', 'SPARQLWrapper', 'nltk', 'sentence_transformers','joblib'],
      python_requires='>=3.7',
      include_package_data=True,
      zip_safe=True)