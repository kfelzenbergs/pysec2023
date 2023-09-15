from libs.utils import readFile

class SysLogParser(object):
    log_file_path = 'syslog.example'
    keywords = [
        'fatal',
        'failed',
        'error'
    ]

    keywords_users = [
        'root'
    ]

    def info(self):
        return "This is syslog parser!"

    def getLogFilePath(self):
        return self.log_file_path

    def readFile(self):
        lines = readFile(self.log_file_path)
        for log_dict in lines:
            for keyword in self.keywords_users:
                if keyword in log_dict['info']:
                    print(
                        '''----log----
                            date: {}
                            message: {}
                            '''.format(
                        '{} {} {}'.format(log_dict['month'], log_dict['day'], log_dict['time']),
                        log_dict['info']
                    ))
