# pytexas_2017_mad_evil

The talk "Python Metaprogramming for Mad Scientists and Evil Geniuses" for PyTexas 2017

The presentation is inside the [Jupyter](http://jupyter.org/) notebook `mad_scientists_evil_geniuses.ipynb`, which uses [RISE](https://damianavila.github.io/RISE/).

This work is dedicated to the public domain using [Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).

The two scenarios demonstrate `sitecustomize.py`. Two use them, try running
Python with and without the directory containing a `sitecustomize.py` in your
PYTHONPATH.

For scenario 1, you need to:

1. Copy `scenario_1` and `scenario_1_test.py` someplace.
2. Edit the files to specify two different absolute paths to Python interpreters.
3. Execute `scenario_1_test.py` with and without `sitecustomize.py`.

Commands:

    ./scenario_1_test.py
    PYTHONPATH=$(pwd)/scenario_1 ./scenario_1_test.py

For scenario 2, you don't have to edit.

    ./scenario_2_test.py
    PYTHONPATH=$(pwd)/scenario_2 ./scenario_2_test.py
