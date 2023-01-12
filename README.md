## About
基于 Python3 生成短链接与二维码图片，通过tinyurl短地址服务实现

## Feature

* 调用 http://tinyurl.com/api-create.php?url=http://URL 生成短地址URL
* 引用 qrcode 库, 生成二维码图片
* 支持多地址转换, 以空格为分隔符, 例如: url1 url2 url3
* 保存到日志文件

## Requires
Python 3.11.0  
qrcode 7.3.1  

## Usage
```
python main.py
```

## Change Log
v1.0.0  

## Maintainers
Alan

## LICENSE
[MIT License](https://github.com/joanbabyfet/gen_short_url/blob/master/LICENSE)