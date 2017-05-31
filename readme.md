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

### Compile error when `pip install -r requirements.txt`

If you have already done `brew install libevent` but it's complaining about `event.h`, try this instead:

    CFLAGS="-I /usr/local/Cellar/libevent/2.1.8/include -L /usr/local/Cellar/libevent/2.1.8/lib" pip install -r requirements.txt

This tells the compiler where libevent is. TO find the correct paths, use `brew info libevent`

### Wrong version of libevent

```
gevent/core.c:2750:47: error: no member named 'ev_flags' in 'struct event'
```

If your `pip install -r requirements.txt` includes an error like that, run `brew info libevent`:

```
$ brew info libevent
libevent: stable 2.1.8 (bottled)
Asynchronous event library
http://libevent.org
Conflicts with:
  pincaster (because both install `event_rpcgen.py` binaries)
/usr/local/Cellar/libevent/2.1.8 (847 files, 2.2MB) *
  Poured from bottle on 2017-05-31 at 16:46:47
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/libevent.rb
==> Dependencies
Build: autoconf ✔, automake ✔, doxygen ✘, libtool ✔, pkg-config ✔
Required: openssl ✔
(inn-boundaries)blk@oyster:~/software/boundaries$ 
```

Looks like this version of `gevent` only works with libevent version 2.0.x

Brew doesn't provide a way to choose an outdated version of the formula; good luck installing it by hand from http://libevent.org/
