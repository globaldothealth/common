import country_converter
import geo_util
import sys

def extract_location_info_from_csv(rows, country_index, location_index,
                                   lat_index, lng_index, out_file):
    location_info = {}
    for row in rows:
        geoid = geo_util.make_geoid(row[lat_index], row[lng_index])
        if geoid not in location_info:
            country_str = row[country_index]
            country_code = country_converter.code_from_name(country_str)
            if not country_code or country_code == "":
                print("WARNING Couldn't get code for " + country_str)
                continue
            location_str = row[location_index].strip()
            if location_str != "" and location_str != country_str:
                # Often times the location name also contains the country
                if location_str.endswith(", " + country_str):
                    crop_length = len(country_str) + len(", ")
                    location_str = location_str[:-crop_length]
                location_info[geoid] = [location_str, country_code]
            else:
                location_info[geoid] = [country_code]
    output_location_info(location_info, out_file)

def compile_location_info(in_data, out_file,
                          keys=["country", "province", "city"], quiet=False):
    if not quiet:
        print("Exporting location info...")
    location_info = {}
    for item in in_data:
        geo_id = item['geoid']
        if geo_id not in location_info:
            name = str(item[keys[0]])
            # 2-letter ISO code for the country
            if name == "nan":
                code = ""
            else:
                code = country_converter.code_from_name(name)
            # Some special cases.
            if code == "" and item[keys[1]] == "Taiwan":
                code = "TW"
            if code == "":
                print("Oops, I couldn't find a code: " + str(item))
            location_info[geo_id] = [(str(item[key]) if str(item[key]) != "nan"
                                      else "") for key in
                                     [keys[2], keys[1]]] + [code]
    output_location_info(location_info, out_file)

def output_location_info(location_info_data, out_file):
    output = []
    for geoid in location_info_data:
        output.append(geoid + ":" + "|".join(location_info_data[geoid]))
    with open(out_file, "w") as f:
        f.write("\n".join(output))
        f.close()
