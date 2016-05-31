# Django Boundary Service for INN projects

This repository uses [Django Boundary Service](https://github.com/newsapps/django-boundaryservice) with shapefiles used in INN projects.

## Getting started

Clone the repository:

    git clone git@github.com:INN/boundaries.git
    cd boundaries

Create a virtualenv:

    mkvirtualenv boundaries

Make sure you have libevent installed:

    brew update
    brew install libevent

Make sure you have GDAL installed:

    brew update
    brew install gdal

See "Compatibility hack for newer versions of GDAL" in the notes at the bottom of this guide if you receive a "Could not parse version info string" error.

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

### Stopping postgresql

To stop postgresql, run:

    pg_ctl -D /usr/local/var/postgres stop -s -m fast

### Compatibility hack for newer versions of GDAL

It may be necessary to modify line 120 of Django's /path/to/your/virtualenv/site-packages/django/contrib/gis/geos/libgeos.py file to work properly with newer versions of GDAL.

If you see receive a "Could not parse version info string" error, try changing that line to:

    ver = geos_version().decode().split(' ')[0]

Be sure and change "/path/to/your/virtualenv/" in the file path to an *actual* file path on your machine.
