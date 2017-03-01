# Sexual Misconduct
The Daily Californian's database of sexual misconduct cases in the University of California
- `data/uc_misconduct.xlsx` contains data from the documents released by the UC that have been parsed by the DC's news staff

##To run:
Make sure to have python2.7x installed. If not, go into `anaconda3/lib/python3.4/site-packages/copytext.p` and change the two function calls to `unicode` to `str`

1. Clone the repository

2. `pip install -r requirements.txt`

3. `python manage.py migrate`

4. `python manage.py load`

5. `python manage.py runserver`

6. Point your browser to http://localhost:8000/.
