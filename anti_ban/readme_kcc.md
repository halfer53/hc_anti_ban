##
7台抓取机器在天津机房
公司买的代理ip，网络部在每台机器上都绑定了代理ip，大概每台机器有60个ip可以供抓取用
准备工作：
1、把所有的代理ip都存放到mongo库里，表(tj_ips)：{'IP':x.x.x.x, 'ID':TJ_01},其中ID表示是哪台机器上的序号。['TJ_01', 'TJ_02', ..., 'TJ_07']
2、还有一个表 tj_proxy： {'ip': 'http://x.x.x.x:port', 'source_ip': x.x.x.x, 'user_pass': tj_user_x_x:xxxxx}
3、其中，还有从本机获取的选项，get_ip_list_from_locale(获取本机所有的ip)， get_usefulness_ip(指定出口ip吧？)

之后在用的时候 就按照Readme.md里的规则就可以。
这个通用的中间件，可以拿来改改，用在不是这种模式的代理也应该可以的。
