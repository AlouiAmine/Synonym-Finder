# Synonym Finder Project

The goal of this project is to find synonyms, abbreviation and related keywords for the wiki-term.

# Installation

``` pip install synonym_finder```

# Get started:

``` 
From synonym_finder import *
#### initialize the synonym finder class
sf = synonym_finder(bert_model = 'nli-bert-large')
#### get synonyms and related keywords
sf.get_synonyms(term = 'Machine learning', source = 'dbpedia', thr = 0.72)

```
