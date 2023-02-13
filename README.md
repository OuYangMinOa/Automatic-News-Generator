
# Status
    Due to the confusion of the original code, continuous integration...

# Build your own

This project is develop base on [python](https://www.python.org). Python3 is require for installation.

1. Install python virtual environment
    ```shell
    sudo pip install pipenv
    pipenv --python 3.10
    pipenv install
    ```
2. Add personal token 

	add your token in `.env`

3. costomize `utils/NewGraber.py`

    Use crawlers to crawl the content you want

4. Activate virtual environment and run
    ```shell
    pipenv shell
    python3 main.py
    ```

    