# Replace unittest with pytest

The goal with this exercise is to replace unittest with pytest

## Steps

1. Install pytest

    ```bash
    pip install pytest
    pip list --format=freeze
    # Copy the pytest row to your requirements.txt
    ```

2. Test run a specific test:

    ```bash
    # Run from the project root
    python -m pytest tests/lesson_2/test_basic.py
    ```

3. Add a pytest.ini file or add the following to tox.ini

    ```ini
    [pytest]
    pythonpath = .
    ```

    Now python will recognize your folder structure and you can run:

    ```bash
    pytest tests
    ```

    Another method is to add a empty `__init__.py` file to the tests folder.

4. In .vscode/settings.json

    ```json
    {
        "python.testing.pytestArgs": [
            "tests"
        ],
        "python.testing.unittestEnabled": false,
        "python.testing.pytestEnabled": true,
        "editor.formatOnSave": true,
        "python.linting.enabled": true,
        "python.linting.flake8Enabled": true
    }
    ```

    You may need to restart vscode after this change. Then test run all tests in GUI.

5. Update tox.ini to use pytest

    ```bash
    # change coverage run --branch -m unittest discover tests to

    coverage run --branch -m pytest tests

    ```

6. Test your change with tox

    ```Bash
    # Use recreate to force a dependency installation
    tox --recreate
    ```

7. Change your test files to the pytest format

    ```python
    # Unittest
    def test_add(self):
        self.assertEqual(basic.add(1, 1), 7)
    ```

    ```python
    # Pytest format without class
    def test_add():
        assert basic.add(1, 1) == 7
    ```

8. You should also remove the unittest import and the code `unittest.main()`

## Coverage

1. Run tox in your pytest converted project
2. Now you have 40% coverage for `basic.py`
   1. Inspect the `basic.py` file with coverage gutter extensions in VSCode
   2. Run coverage report in your terminal
3. Write the missing test so that you achieve 100% coverage
4. Run tox again, and verify that `basic.py` have 100% coverage
