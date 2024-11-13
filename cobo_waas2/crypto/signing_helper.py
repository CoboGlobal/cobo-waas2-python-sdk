import hashlib
import time
from urllib.parse import urlencode

from nacl.signing import SigningKey, VerifyKey
from nacl.exceptions import BadSignatureError


class SignHelper(object):
    @classmethod
    def _build_unsigned_digest(
        cls,
        method: str,
        path: str,
        timestamp: str,
        params: dict = None,
        body: bytes = None,
    ) -> bytes:
        method = method.lower()

        body_str = str(body, "utf-8", "strict") if body else ""
        params = params or {}
        str_to_sign = "|".join(
            (method.upper(), path, timestamp, urlencode(params), body_str)
        )

        digest = hashlib.sha256(hashlib.sha256(str_to_sign.encode()).digest()).digest()
        return digest

    @classmethod
    def sign(
        cls,
        api_secret: str,
        method: str,
        path: str,
        timestamp: str,
        params: dict = None,
        body: bytes = None,
    ) -> (bytes, bytes):
        digest = cls._build_unsigned_digest(
            method, path, timestamp, params=params, body=body
        )
        sk = SigningKey(bytes.fromhex(api_secret))
        signature = sk.sign(digest).signature
        vk = bytes(sk.verify_key)
        return signature, vk

    @classmethod
    def generate_headers(
        cls,
        api_secret: str,
        body: bytes,
        method: str,
        params: dict,
        path,
    ):
        timestamp = str(int(time.time() * 1000))
        signature, api_key = cls.sign(
            api_secret,
            method,
            path,
            timestamp,
            params=params,
            body=body,
        )
        headers = {
            "Biz-Api-Key": api_key.hex(),
            "Biz-Api-Nonce": timestamp,
            "Biz-Api-Signature": signature.hex(),
        }
        return headers

    @classmethod
    def generate_api_key(cls) -> dict:
        sk = SigningKey.generate()
        return {
            "api_key": bytes(sk.verify_key).hex(),
            "api_secret": bytes(sk).hex(),
        }

    @classmethod
    def verify(
        cls,
        pub_key: str,
        signature: str,
        content: str
    ) -> bool:
        try:
            content_hash = hashlib.sha256(
                hashlib.sha256(content.encode()).digest()
            ).digest()

            # Convert the public key (api_key) and signature from hex to bytes
            verify_key = VerifyKey(bytes.fromhex(pub_key))
            signature_bytes = bytes.fromhex(signature)

            # Verify the signature
            verify_key.verify(signature=signature_bytes, smessage=content_hash)
            return True

        except BadSignatureError as e:
            return False