#!/bin/bash

echo "Drop the db...";
dropdb -h localhost boundaries;
echo "Create the db...";
createdb -h localhost boundaries;
echo "Create GIS extension...";
psql -h localhost -d boundaries -c "CREATE EXTENSION postgis;";
echo "Run syncdb...";
./manage.py syncdb --noinput
echo "Load shapefiles...";
./manage.py loadshapefiles
echo "Done.";
