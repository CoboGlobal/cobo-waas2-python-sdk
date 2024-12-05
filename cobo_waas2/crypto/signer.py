from abc import ABC


class Signer(ABC):

    def sign(self, message_hash: bytes) -> str:
        """
        signed a hashed message
        """
        raise NotImplemented

    def get_public_key(self) -> str:
        raise NotImplemented
