from libs.AuthLogParser import AuthLogParser
from libs.SysLogParser import SysLogParser
from datetime import datetime


authLogParser = AuthLogParser()
authLogParser.info()
authEvents = authLogParser.readFile()


sysLogParser = SysLogParser()
sysLogEvents = sysLogParser.readFile()


commonLog = authEvents + sysLogEvents


sortedLog = sorted(commonLog, key=lambda d: d['date'])
for event in sortedLog:
    event['date'] = datetime.utcfromtimestamp(event['date']).strftime("%Y %b %d %H:%M:%S")
    print(event)
