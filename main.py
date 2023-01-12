import contextlib 
from urllib.parse import urlencode
from urllib.request import urlopen
import logging
import time
import qrcode

# 日志文件
log_file = 'url_' + time.strftime("%Y%m%d", time.localtime()) + '.log'

# 通过tinyurl生成短地址
def make_short_url(sn, data):
    url = 'http://tinyurl.com/api-create.php?' + urlencode({'url': data})

    with contextlib.closing(urlopen(url)) as resp:
        short_url = resp.read().decode('utf-8') # 调用decode返回字符串

        qrcode_img = qrcode.make(data=short_url)
        filename = 'qrcode%s.png' % sn
        with open(filename, 'wb') as f:
            qrcode_img.save(f)
        
        logger('短网址: %s -> 网址: %s' % (short_url, data)) # 写入日志
        return [short_url, filename]

# 写入日志
def logger(data):
    logging.basicConfig(filename = log_file, encoding = 'utf-8', level = logging.DEBUG, 
        format = '[%(asctime)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(data) # 根据日期生成日志

def main():
    url = input('请输入网址: ') # 交互式输入
    list_url = url.split(' ') # 多地址可用空格为分隔符并返回列表

    sn = 1
    for v in list_url: # 逐条取出
        ret = make_short_url(sn, v)
        sn = sn + 1
        print('短网址: %s 二维码图片: %s' % (ret[0], ret[1]))

if __name__ == '__main__': # 主入口
    main()