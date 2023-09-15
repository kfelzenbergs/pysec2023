from libs.AuthLogParser import AuthLogParser
from libs.SysLogParser import SysLogParser

authLogParser = AuthLogParser()
authLogParser.info()
authLogParser.readFile()


# print(SysLogParser.log_file_path)
sysLogParser = SysLogParser()
# print(sysLogParser.info())
# print(sysLogParser.getLogFilePath())

