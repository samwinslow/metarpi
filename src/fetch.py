import urllib.request
from bs4 import BeautifulSoup


def fetch_metars(station_string):
  """Fetch latest METAR data for station (ICAO identifier)"""
  source_url = f'https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=3&mostRecent=true&stationString={station_string}'

  raw_strings = []
  with urllib.request.urlopen(source_url) as response:
    xml = response.read()
    tree = BeautifulSoup(xml, 'lxml')
    metars = tree.find_all('metar')
    for metar in metars:
      raw_strings.append(metar.raw_text.get_text())

  return '\n'.join(raw_strings)
