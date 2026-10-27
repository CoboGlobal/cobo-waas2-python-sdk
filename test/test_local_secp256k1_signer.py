import hashlib
import unittest

from cobo_waas2.crypto.local_secp256k1_signer import LocalSecp256k1Signer


class TestLocalSecp256k1Signer(unittest.TestCase):
    def setUp(self) -> None:
        priv_key, _ = LocalSecp256k1Signer.generate_key_pair()
        self.signer = LocalSecp256k1Signer(priv_key)
        self.message_hash = hashlib.sha256(b"cobo waas2").digest()

    def test_verify_accepts_own_signature(self) -> None:
        signature = self.signer.sign(self.message_hash)
        self.assertTrue(self.signer.verify(signature, self.message_hash))

    def test_verify_rejects_other_digest(self) -> None:
        signature = self.signer.sign(self.message_hash)
        other_hash = hashlib.sha256(b"tampered").digest()
        self.assertFalse(self.signer.verify(signature, other_hash))

    def test_verify_rejects_signature_from_other_key(self) -> None:
        other_priv_key, _ = LocalSecp256k1Signer.generate_key_pair()
        signature = LocalSecp256k1Signer(other_priv_key).sign(self.message_hash)
        self.assertFalse(self.signer.verify(signature, self.message_hash))


if __name__ == "__main__":
    unittest.main()
