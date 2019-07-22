# msci_452_project

to run on your machine:

1. `$ git clone git@github.com:mllemango/msci_452_project.git`
2. `$ cd msci_452_project`
3. `$ pip install -r requirements.txt`
4. `$ python recursive.py`


There is a (currently commented out) graphing function, if you want to use, you'll need to download pygraphviz:

http://pygraphviz.github.io/documentation/pygraphviz-1.5/install.html

or follow the below instructions:

1. `$ brew install graphviz`
more info can be found here: http://graphviz.org/download/

2. `$ git clone https://github.com/pygraphviz/pygraphviz`
3. `$ pip install pygraphviz`

  **or**

  `$ python setup.py install --include-path=/usr/local/Cellar/graphviz/2.40.1_1/include/graphviz --library-path=/usr/local/Cellar/graphviz/2.40.1_1/lib`
