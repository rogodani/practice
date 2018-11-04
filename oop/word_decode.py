'''
Decode a string
rule:
E -> G
K -> M
O -> Q
'''

import string


class Decode:
    def __init__(self, text):
        self.text = text

    def decode_text(self):
        intab = string.ascii_lowercase
        outtab = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
        trantab = str.maketrans(intab, outtab)
        return self.text.translate(trantab)


text = "g fmnc wms bgblr rpylqjyrc gr zw fylb." \
       "rfyrq ufyr amknsrcpq ypc dmp." \
       "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle." \
       "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(Decode(text).decode_text())
print(Decode('http://www.pythonchallenge.com/pc/def/map.html').decode_text())
