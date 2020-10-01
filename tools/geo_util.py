import glob
import os

LAT_LNG_DECIMAL_PLACES = 4

def round_latlng(l):
    l = str(l)
    if "." not in l:
        l += ".0000"
    (intpart, dec) = l.split(".")
    if len(dec) > LAT_LNG_DECIMAL_PLACES:
        # Just truncate
        dec = dec[0:4]
    elif len(dec) < LAT_LNG_DECIMAL_PLACES:
        dec += "0" * (LAT_LNG_DECIMAL_PLACES - len(dec))
    return intpart + "." + dec

def make_geoid(lat, lng):
    return round_latlng(lat) + "|" + round_latlng(lng)

def clean():
    for daily in glob.glob("d/*.json"):
        os.remove(daily)
    for country in glob.glob("c/*.json"):
        os.remove(country)
