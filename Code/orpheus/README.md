## Installing

pip install -r requirements.txt

## Python3.7

Python 3.8 is only compatable with tensorflow 2.X, and the benepar tree parser
we use is a tensorflow 1.X series model. So we must additionally install python3
using the deadsnakes ppa.

* http://phoenixnap.com/kb/how-to-install-python-3-ubuntu

Then if you run, you would get the 
```
benepar/chart_decoder.c:17:10: fatal error: Python.h: No such file or directory
       17 | #include "Python.h"
          |          ^~~~~~
    compilation terminated.
    error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
```

sudo apt-get install python3.7-dev # for python3.x installs

requires virtualenv as well

```sh
virtualenv --python=/usr/bin/python3.7 ./virtualenv
source ./virtualenv/bin/activate  # sh, bash, or zsh
python3.7 -m pip install --upgrade pip
pip list  
deactivate 
```

`python --version` should show Python3.7.X and likewise `pip --version` should
by under python3. You should also see the (virtualenv) before your usual termanl
prompt.

Now run `pip install -r requirements.txt` and follow that with `pip install -r
requrements_2.txt`. These are separate to avoid a dependency cycle experienced
in testing.

* python -m spacy download en

* https://pypi.org/project/benepar/

python3.7
```py
import nltk
nltk.download('punkt')
import benepar
benepar.download('benepar_en')
```

`mkdir logs`

## Running

Expects excel file with one sheet and two columns: `author_id` and `review_contents`

type `make features` to generate features

## Troubleshooting

Problem:

```
 File "feature_extraction/sample_parser.py", line 47, in <module>
    nlp = spacy.load('en')

    ...

    FileNotFoundError: [Errno 2] No such file or directory: '... Code/orpheus/virtualenv/lib/python3.7/site-packages/spacy/data/en/__init__.py'
```
Solution:
virtualenv/bin/python3.7 -m spacy link en_core_web_sm en --force

https://github.com/explosion/spaCy/issues/2406

