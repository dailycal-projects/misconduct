# Sexual Misconduct
The Daily Californian's database of sexual misconduct cases in the University of California
- `data/uc_misconduct.csv` contains data from the documents released by the UC that have been processed by DC staff

## To run:
Make sure to have python2.7x installed.

1. Clone the repository

2. `pip install -r requirements.txt`

3. `python manage.py migrate`

4. `python manage.py load`

5. `python manage.py runserver`

6. Point your browser to http://localhost:8000/

## To upload to DocumentCloud

Set the environment variables `DOCUMENTCLOUD_USERNAME` and `DOCUMENTCLOUD_PASSWORD`, then run `python manage.py upload_documentcloud`.

## To bake the site into flat files

Run `python manage.py build`.
