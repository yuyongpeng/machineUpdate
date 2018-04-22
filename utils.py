# -*- coding: utf-8 -*-

import hashlib
import requests
import os

def check_hash256(file, checksum):
    """检测文件和checksum是否匹配"""
    f = open(file, 'rb')
    sh = hashlib.sha256()
    sh.update(f.read())
    if sh.hexdigest() == checksum:
        f.close()
        return True
    else:
        return False


def download_file(url, local):
    """下载文件到本地"""
    filename = os.path.basename(url)
    r = requests.get(url)
    with open(local + "/" + filename, "wb") as code:
        code.write(r.content)

if __name__ == "__main__":
    url = "https://nodejs.org/dist/v8.11.1/node-v8.11.1-linux-armv7l.tar.xz"
    local = "/tmp"
    sha256 = "7bb97e3b06d186cfff576096f75431eedcc0ecee16c47afe8aabd7a22cc31c47"

    download_file(url, local)
    tf = check_hash256('/tmp/node-v8.11.1-linux-armv7l.tar.xz', sha256)
    print(tf)

