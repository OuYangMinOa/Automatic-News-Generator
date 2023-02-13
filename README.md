
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

	Add token in `.env`

3. Install ImageMagick
    
    For linux : sudo apt install imagemagick

    For windows : [url](https://imagemagick.org/script/download.php)

4. costomize `utils/NewGraber.py` : Use crawlers to crawl the content and the image,

5. Costomize `utils/NewGenerator.py` : Add Fixed clips 

