import os
import codecs
from digest import Digest
from rbc_sha import RbcSha


if '__main__' == __name__:
    print('hello world')
    print(codecs.encode(RbcSha.sha256(''), 'hex'))
