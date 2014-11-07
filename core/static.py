# -*- coding: utf-8 -*-

BUS_URL = 'http://www.basbus.cn/m/line?id={0}'
BUS_URL_REVERSE = 'http://www.basbus.cn/m/line?id={0}&t=2'

UA_HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20100101 Firefox/15.0',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-cn,en-us;q=0.7,en;q=0.3',
    'Accept-Charset': 'utf-8;q=0.7,*;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}

# DELIMITER_BUS_NUMBER = '.headinfo'
# DELIMITER_BUS_START_STATION = '.leftspan01'
# DELIMITER_BUS_END_STATION = '.rightspan01'
# DELIMITER_BUS_TIME = '.leftspan02'
#
# DELIMITER_ALL_STATION = '.buslineinfo > ul'
# DELIMITER_ONE_BUS = 'ul'
# DELIMITER_STATION = '.li_01'
# DELIMITER_STATION_NUMBER = '.yuanicon'
# DELIMITER_STATION_GPS = 'p'