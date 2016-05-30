# Django Boundary Service for INN projects

This repository uses [Django Boundary Service](https://github.com/newsapps/django-boundaryservice) with shapefiles used in INN projects.

## Getting started

Clone the repository:

    git clone git@github.com:INN/boundaries.git
    cd boundaries

Create a virtualenv:

    mkvirtualenv boundaries

Install requirements:

    workon boundaries
    pip install -r requirements.txt

Install postgresql:

    brew update
    brew install postgresql

Run postgresql:

    pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

Run the included `drop_create_db.sh` script:

    ./drop_create_db.sh

Run the development server:

    ./manage.py runserver

Visit the dev site to verify it is working:

    http://localhost:8000/1.0/boundary/


## Notes:

To stop postgresql, run:

    pg_ctl -D /usr/local/var/postgres stop -s -m fast
