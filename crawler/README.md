# DNS Analyzer
This tool listens on a given network interface and caputers DNS packets. Furtheron each domain is resolved to IP and geolocation is added. Finally data is saved in a local sqlite database.

Note that running packet sniffer requires elevated system privileges

## Setup
1. Register on https://geolocation-db.com/ and get your API key
2. Export the `GEOAPI_KEY` variable on your system as elevated user
```
# on linux
export GEOAPI_KEY=<your api key>

# on windows
set GEOAPI_KEY=<your api key>
```

## Running (as elevated user)
```
python3 -m venv venv

# on linux
. venv/bin/activate

# on windows
venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

You can connect to the local sqlite database file and query contents as follows
```
sqlite3 dns.db
.tables
select * from dns_domains;
```
