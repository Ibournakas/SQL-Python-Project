import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import  mechanize
import pandas as pd
from sodapy import Socrata


fp = urllib.request.urlopen("https://data.buffalony.gov/Quality-of-Life/Monthly-Recycling-and-Waste-Collection-Statistics/2cjd-uvx7/data")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()


client = Socrata("data.buffalony.gov","jP9NndBOFmY8yNVacKeXqrnWC", "diadem_anorak.0u@icloud.com","nydvud-6pUjso-koxtas")

# First 2000 results, returned as JSON from API / converted to Python list of dictionaries by sodapy.
results = client.get("2cjd-uvx7", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
#print(results_df)
results_df.to_csv('data.csv')