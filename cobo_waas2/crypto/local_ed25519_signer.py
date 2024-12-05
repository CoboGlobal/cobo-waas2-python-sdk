from nacl.signing import SigningKey

from cobo_waas2.crypto.signer import Signer


class LocalEd25519Signer(Signer):
    def __init__(self, priv_key: str):
        self.sk = SigningKey(bytes.fromhex(priv_key))
        self.vk = bytes(self.sk.verify_key)

    def sign(self, message_hash: bytes) -> str:
        signature = self.sk.sign(message_hash).signature
        return signature.hex()

    def get_public_key(self) -> str:
        return self.vk.hex()

    @classmethod
    def generate_key_pair(cls) -> (str, str):
        sk = SigningKey.generate()
        return sk.encode().hex(), sk.verify_key.encode().hex()