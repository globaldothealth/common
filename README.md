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
  one would expect to see on a map.
