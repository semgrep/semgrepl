# semgrepl

Cool hack project.

## Hacking on semgrepl in ipython

Python package dependencies can be installed using
`pip3 install -r requirements.txt`.

When developing semgrepl it is convenient to have ipython autoreload modules.
That way you can keep ipython open and it reloads the module when you save a
file. Type the following magic commands when ipython is first loaded:

```
%load_ext autoreload
%autoreload 2
```

The main entrypoint into semgrepl is `utils.py` which can be loaded in ipython
with:

```
# From src directory
import utils
```

For example, to find all function definitions in the file `semgrepl.py`.

```
target = 'semgrepl.py'
rules_dir = '../rules'
utils.find_all_function_defs(target, rules_dir)
```
