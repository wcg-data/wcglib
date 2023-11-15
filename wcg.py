import platform
from log_utils import log

class WCG:
    def get_os(self):
        os_name = platform.system()
        if os_name == 'Windows':
            return 'Windows'
        elif os_name == 'Linux':
            return 'Linux'
        elif os_name == 'Darwin':
            return 'Mac'
        else:
            return 'Unknown'
    

l
        