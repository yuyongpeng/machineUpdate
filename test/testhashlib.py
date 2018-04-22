# -*- coding: utf-8 -*-
import hashlib

if __name__ == "__main__":
    f = open('../requirements.txt', 'rb')

    print(hashlib.sha1(u'fffff'.encode('utf8')).hexdigest())

    md5 = hashlib.md5()
    md5.update('how to use md5 in '.encode('utf8'))
    md5.update('python hashlib?'.encode('utf8'))
    print(md5.hexdigest())

    sh = hashlib.sha256()
    sh.update(f.read())
    print(sh.hexdigest())
    print(sh.hesdigest() == '561d2c15fa79c319959cfc821650c829860651d1e5b125b2a425ac9cbd3fe1bb')

    f.close()