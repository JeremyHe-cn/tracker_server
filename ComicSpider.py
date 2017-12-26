from urllib import request
import re
import hashlib

# req = request.Request("http://www.manhuagui.com/comic/883/")

def manhuagui(url):
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
    with request.urlopen(req) as resp:
        html = resp.read().decode('UTF-8')
        titlePattern = re.compile(r'.*<h1>(.*)</h1>.*最近于 \[<span class="red">(\d{4}-\d+-\d+)</span>] 更新至 \[ <a.*class="blue">(第\d*[回话].*)</a> ].*')

        md5 = hashlib.md5()
        md5.update(url.encode('UTF-8'))
        with open('./%s' % md5.hexdigest(), 'w') as error:
            error.write(html)
        
        match = re.match(titlePattern, html)
        if match:
            return match.groups()
        else:
            with open('./%s' % hash(url), 'w') as error:
                error.write(html)
            return ('','','')

urls = [
    "http://www.manhuagui.com/comic/883/",
    "http://www.manhuagui.com/comic/17965/"
]

for url in urls:
    comic = manhuagui(url)
    print(comic[0])
    print(comic[1], comic[2])
    print('------------')
