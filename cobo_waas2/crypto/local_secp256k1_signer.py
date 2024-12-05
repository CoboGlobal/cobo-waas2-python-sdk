import hashlib
from ecdsa import SigningKey, SECP256k1
from ecdsa.util import sigencode_der_canonize, sigdecode_der
import binascii

from cobo_waas2.crypto.signer import Signer
from ecdsa import BadSignatureError


class LocalSecp256k1Signer(Signer):
    def __init__(self, priv_key: str):
        self.private_key = SigningKey.from_string(binascii.unhexlify(priv_key), curve=SECP256k1)
        self.public_key = self.private_key.verifying_key

    def sign(self, message_hash: bytes) -> str:
        der_signature = self.private_key.sign_digest(
            message_hash, sigencode=sigencode_der_canonize
        )
        return binascii.hexlify(der_signature).decode()

    def get_public_key(self) -> str:
        public_key_bytes = self.public_key.to_string("compressed")
        return binascii.hexlify(public_key_bytes).decode()

    @classmethod
    def generate_key_pair(cls) -> (str, str):
        private_key = SigningKey.generate(curve=SECP256k1)
        public_key = private_key.verifying_key
        return (binascii.hexlify(private_key.to_string()).decode(),
                binascii.hexlify(public_key.to_string("compressed")).decode()
                )

    def verify(self, signature: str, message_hash: bytes) -> bool:
        signature_bytes = binascii.unhexlify(signature)
        try:
            self.public_key.verify(signature_bytes, message_hash, sigdecode=sigdecode_der)
            print("Signature is valid.")
            return True
        except BadSignatureError:
            print("Signature verification failed.")
            return False
