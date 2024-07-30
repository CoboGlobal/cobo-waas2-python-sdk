import hashlib
import time
from urllib.parse import urlencode

import ed25519
from ed25519.keys import create_keypair


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
        sk = ed25519.SigningKey(sk_s=bytes.fromhex(api_secret))
        signature = sk.sign(digest)
        vk = sk.get_verifying_key().to_bytes()
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
        sk, vk = create_keypair()
        return {
            "api_key": vk.to_bytes().hex(),
            "api_secret": sk.to_seed().hex(),
        }
