# shapefiles to geojson

https://www.ausgestrahlt.de/themen/atommuell/hochradioaktiv/endlagersuche/karte/

https://www.bge.de/de/endlagersuche/wesentliche-unterlagen/zwischenbericht-teilgebiete/

## convert from shapefile to geojson

`pip install -r requirements.txt`

`python main.py --data ~/Downloads/Digitale_Daten_zu_den_Teilgebieten.1/TG_Shapes_02112020`

## merge geojson files

`npm i -g @mapbox/geojson-merge`

For every result folder:

E.g.: `geojson-merge *.geojson > tongestein_ter.geojson`

## simplify geojson files

`npm i -g simplify-geojson`

E.g.: `cat tongestein_ter.geojson | simplify-geojson -t 0.001 > tongestein_ter_0.001.geojson`
