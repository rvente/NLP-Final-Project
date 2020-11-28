## Installing

pip install -r requirements.txt

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


```py
import nltk
nltk.download('punkt')
import benepar
benepar.download('benepar_en')
```

`mkdir logs`

## Running

Expects excel file with one sheet and two columns: `author_id` and 

type `make features` to generate features
