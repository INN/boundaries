from datetime import date

from django.contrib.humanize.templatetags.humanize import ordinal

from boundaryservice import utils

SHAPEFILES = {
    'Community Areas': {
        'file': 'community-areas/geo_export_08c6fa60-92cb-47d1-b68c-2c95e2ddf0e2.shp',
        'singular': 'Community Area',
        'kind_first': False,
        'ider': utils.simple_namer(['AREA_NUMBE']),
        'namer': utils.simple_namer(['COMMUNITY'], normalizer=lambda s: s.title()),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'Neighborhoods': {
        'file': 'neighborhoods/Neighborhoods_2012b.shp',
        'singular': 'Neighborhood',
        'kind_first': False,
        'ider': utils.simple_namer(['pri_neigh']),
        'namer': utils.simple_namer(['pri_neigh']),
        'authority': 'City of Chicago',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
        'notes': '',
        'encoding': ''
    },
    'Police Beats': {
        'file': 'police-beats/geo_export_3445aa13-fe4e-4455-b210-5eff6933304c.shp',
        'singular': 'Police Beat',
        'kind_first': True,
        'ider': utils.simple_namer(['BEAT_NUM']),
        'namer': utils.simple_namer(['BEAT_NUM'], normalizer=lambda s: '#%s' % s),
        'authority': 'Chicago Police Department',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 13),
        'href': 'http://gis.chicagopolice.org/',
        'notes': '',
        'encoding': ''
    },
    'Police Districts': {
        'file': 'police-districts/geo_export_6ee9e671-13a3-44d2-a660-76a457767083.shp',
        'singular': 'Police District',
        'kind_first': False,
        'ider': utils.simple_namer(['DIST_NUM']),
        'namer': utils.simple_namer(['DIST_NUM'], normalizer=lambda s: ordinal(s)),
        'authority': 'Chicago Police Department',
        'domain': 'Chicago',
        'last_updated': date(2010, 12, 13),
        'href': 'http://gis.chicagopolice.org/',
        'notes': '',
        'encoding': ''
    },
}
