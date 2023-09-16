
# import whois

# query = whois.whois('va.lv')
# print(query.text)


from scapy.all import *
from scapy.layers.dns import DNSRR, DNS, DNSQR
from dblib import create_connection, create_table, create_record
from utils import getIpByDomainName, getGeoData

database = r'./dns.db'

conn = create_connection(database)

with conn:
    try:
        create_table(conn)
    except Exception as ex:
        print("table already exist.. continuing")

def packetProcessor(pkt):
    if pkt.haslayer(DNS):
        if pkt.qdcount > 0 and isinstance(pkt.qd, DNSQR):
            name = pkt.qd.qname
        elif pkt.ancount > 0 and isinstance(pkt.an, DNSRR):
            name = pkt.an.rdata

        try:
            domain_name = bytes(name).decode()
            ip = getIpByDomainName(domain_name)
            geo = getGeoData(ip)
            print(domain_name, ip, geo)

            with conn:
                create_record(conn, [domain_name, ip, geo['country_code'], geo['country_name'], geo['city'], geo['latitude'], geo['longitude']])
        except Exception as ex:
            print("Failed for entry {} with exception {}".format(domain_name, ex))


sniff(iface='enp0s31f6', prn=packetProcessor, filter='udp and port 53', store=0)
