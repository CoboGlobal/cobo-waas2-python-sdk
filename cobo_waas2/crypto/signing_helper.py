import hashlib
import time
from urllib.parse import urlencode
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from cobo_waas2.crypto.signer import Signer


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
        signer: Signer,
        method: str,
        path: str,
        timestamp: str,
        params: dict = None,
        body: bytes = None,
    ) -> (bytes, bytes):
        digest = cls._build_unsigned_digest(
            method, path, timestamp, params=params, body=body
        )
        signature = signer.sign(digest)
        return signature, signer.get_public_key()

    @classmethod
    def generate_headers(
        cls,
        signer: Signer,
        body: bytes,
        method: str,
        params: dict,
        path,
    ):
        timestamp = str(int(time.time() * 1000))
        signature, api_key = cls.sign(
            signer,
            method,
            path,
            timestamp,
            params=params,
            body=body,
        )
        headers = {
            "Biz-Api-Key": api_key,
            "Biz-Api-Nonce": timestamp,
            "Biz-Api-Signature": signature,
        }
        return headers

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