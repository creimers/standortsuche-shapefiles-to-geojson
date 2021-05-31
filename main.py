import argparse

import os
import geopandas


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", help="the input data directory", required=True)

    args = parser.parse_args()

    base_dir = os.path.abspath(args.data)
    for dir in os.listdir(base_dir):
        if dir.split("_")[0].isnumeric():
            shape_file_dir = os.path.join(base_dir, dir)
            for filename in os.listdir(shape_file_dir):
                if filename.endswith(".shp"):
                    shape_file_path = os.path.join(shape_file_dir, filename)
                    data = geopandas.read_file(shape_file_path)
                    w = data.Wirtsgeste
                    e = data.Einheit
                    stone = w[0]
                    unit = e[0]
                    if stone == "Tongestein":
                        if "Tertiär" in unit:
                            stone_dir = os.path.join(base_dir, f"{stone}-Tertiär")
                        else:
                            stone_dir = os.path.join(base_dir, f"{stone}-Pretertiär")
                    else:
                        stone_dir = os.path.join(base_dir, stone)
                    if not os.path.exists(stone_dir):
                        os.mkdir(stone_dir)
                    try:
                        data.to_crs(epsg=4326, inplace=True)
                        outfile = os.path.join(stone_dir, f"{dir}.geojson")
                        data.to_file(outfile, driver="GeoJSON")
                    except Exception as e:
                        print(e)


if __name__ == "__main__":
    main()
