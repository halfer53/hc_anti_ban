import sys
sys.path.append('/tools/python_common')
from common_func import get_ip_list_from_locale

for ip in get_ip_list_from_locale():
    print ip
