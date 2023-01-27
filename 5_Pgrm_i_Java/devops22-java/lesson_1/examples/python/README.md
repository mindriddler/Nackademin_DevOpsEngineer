# Python bytecode

## Human readable bytecode

```bash
# Change directory to the python folder
cd lesson_1/examples/python

# Inspect hello world program
python3 -m dis hello.py

# Inspect hello world class
python3 -m dis example.py
```

## Compile to bytecode

```bash

# Compile python
python3 -m compileall .

# Inspect the files created in __pycache__
cd __pycache__

# Open with text editor or vscode
```
