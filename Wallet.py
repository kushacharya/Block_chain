import uuid
# from Crypto.PublicKey import RSA
#
# # key = RSA.generate(2048)
# # private_key = key.exportKey()
# # public_key = key.publickey().export_key()
#
#
#
def createWallet():
    return str(uuid.uuid4())

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import base64

class Wallet:
    def __init__(self):
        key = RSA.generate(2048)
        self.private_key = key.exportKey().decode()
        self.public_key = key.publickey().exportKey().decode()

    def sign_transaction(self, sender, receiver, amount):
        private_key = RSA.importKey(self.private_key)
        signer = PKCS1_v1_5.new(private_key)
        message = f"{sender} {receiver} {amount}".encode()
        digest = SHA256.new()
        return base64.b64encode(signer.sign(digest)).decode()

    def verify_transaction(public_key,signature,sender,receiver,amount):
        public_key = RSA.importKey(public_key)
        verifier = PKCS1_v1_5.new(public_key)
        message = f"{sender} {receiver} {amount}".encode()
        digest = SHA256.new(message)
        return verifier.verify(digest, signature)
