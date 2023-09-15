class SysLogParser(object):
    log_file_path = '/var/log/syslog'

    def info(self):
        return "This is syslog parser!"

    def getLogFilePath(self):
        return self.log_file_path
