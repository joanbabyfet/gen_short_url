import contextlib 
from urllib.parse import urlencode
from urllib.request import urlopen
import qrcode
import utils

# 通过tinyurl生成短地址
def make_short_url(data):
    url = 'http://tinyurl.com/api-create.php?' + urlencode({'url': data})

    with contextlib.closing(urlopen(url)) as resp:
        ret = resp.read().decode('utf-8') # 调用decode返回字符串
        # 写入日志
        utils.logger('短网址: %s -> 网址: %s' % (ret, data))
        return ret

# 生成二维码图片
def make_qrcode(sn, url):
    qrcode_img = qrcode.make(data=url)
    filename = 'qrcode%s.png' % sn
    with open(filename, 'wb') as f:
        qrcode_img.save(f)
    return filename

def main():
    url = input('请输入网址: ') # 交互式输入
    list_url = url.split(' ') # 多地址可用空格为分隔符并返回列表

    sn = 1
    for v in list_url: # 逐条取出
        short_url = make_short_url(v)
        qrcode = make_qrcode(sn, short_url)
        sn = sn + 1
        print('短网址: %s 二维码图片: %s' % (short_url, qrcode))

if __name__ == '__main__': # 主入口
    main()