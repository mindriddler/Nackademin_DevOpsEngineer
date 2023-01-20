# Pythons built-in module for Unit Tests

## Instructions

- Create a branch before you start coding

## Unit tests

### Setup

Test run a specific test:

```bash
# Run from the project root
python -m unittest -v tests/test_hello_world.py
```

Setup and test run in your code editor:

- [Python testing in Visual Studio Code](https://code.visualstudio.com/docs/python/testing)
- [Testing your first python application in PyCharm](https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html)

### Exercise 1

Use the (Red - Green - Refactor) mentality to solve this exercise.

The goal is to write a function that returns the sum of x, y and multiply with 2. i.e

- x = 5, y=1 should return 12
- x = -5, y=1 should return -8

#### Exercise 1 - Steps

1. Create a test file in the tests folder (make sure to name it according to the default discovery pattern test*.py)
2. Create a minimal function definition in `basic.py` i.e:

   ```python
   def your_function():
      pass
   ```

3. Run the test in your code editor, verify that it fails **RED**
4. Run the test through the terminal, verify that it fails **RED**
5. Write the function code so that the test passes
6. Run the test and make sure it passes **GREEN**
7. Refactor if something can be improved **REFACTOR**
8. Repeat step 3 - 7 and add more tests, i.e
   1. negative values
   2. wrongful types i.e x = "3", y = -1

### Extra Exercises

- Create a new test file and function file

1. Create a function that calculates the area of a rectangle
2. Create a function that calculates the area of a triangle
3. Create a function that returns true for values above 2
4. Create a function that takes first name, last name and returns "hello firstname lastname"
5. Create a function that accepts multiple values as arguments and returns the sum, i.e 2, 2, 2 = 6
6. Create a function that accepts multiple values as arguments and returns the product, i.e 2, 2, 2 = 8

## Hand in instructions

Open a pull request against main in GitHub