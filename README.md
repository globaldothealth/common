# common

Common geographical data and tools

# Countries

The `countries.data` file contains one country per line, with the following data
separated by colons, when available:

* 2-letter ISO code
* Name
* Population
* List (separated with `|` characters) of bounding boxes for geographical parts
  of this country. The first item is expected to be the part of the country that
  one would expect to see on a map, if no centroid (see below) is supplied. This
  is not always a great assumption.
* centroid of the country.

# Updating the data

The script `./update_country_boundaries` updates a file `country_boundaries.json` which contains the bounding boxes (from Natural Earth) and centroids (from a Google data dump).

The script `./update` will fetch country names and populations from Wikipedia, and the centroids from the above `country_boundaries.json` file, and rewrite `countries.data`. It doesn't yet rewrite the bounding boxes.

Prerequisites for the scripts are defined in `requirements.txt` which you can use with `pip` to install them.

# Why do I care?

This data is used directly in the [map visualisation of global.health](https://map.covid-19.global.health). The front end directly fetches `countries.data` from the master branch on github in the browser, and uses it to configure the map display.
