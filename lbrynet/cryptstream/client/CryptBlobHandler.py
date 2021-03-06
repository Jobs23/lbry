import binascii
from zope.interface import implements
from lbrynet.cryptstream.CryptBlob import StreamBlobDecryptor
from lbrynet.interfaces import IBlobHandler


class CryptBlobHandler(object):
    implements(IBlobHandler)

    def __init__(self, key, write_func):
        self.key = key
        self.write_func = write_func

    ######## IBlobHandler #########

    def handle_blob(self, blob, blob_info):
        blob_decryptor = StreamBlobDecryptor(
            blob, self.key, binascii.unhexlify(blob_info.iv), blob_info.length)
        d = blob_decryptor.decrypt(self.write_func)
        return d
