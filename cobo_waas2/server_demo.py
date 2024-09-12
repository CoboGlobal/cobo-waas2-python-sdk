import hashlib
import json
import logging
from typing import Optional

from nacl.exceptions import BadSignatureError
from nacl.signing import SigningKey, VerifyKey

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import PlainTextResponse

from cobo_waas2 import WebhookEvent, Transaction


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# Select the public key based on the environment that you use,
# DEV for the development environment and PROD for the production environment.
pub_keys = {
    "DEV": "a04ea1d5fa8da71f1dcfccf972b9c4eba0a2d8aba1f6da26f49977b08a0d2718",
    "PROD": "8d4a482641adb2a34b726f05827dba9a9653e5857469b8749052bf4458a86729",
}

pubkey = pub_keys["PROD"]


@app.post("/api/webhook")
async def handle_webhook(
    request: Request,
    biz_timestamp: Optional[str] = Header(None),
    biz_resp_signature: Optional[str] = Header(None),
):
    raw_body = await request.body()
    sig_valid = verify_signature(
        pubkey, biz_resp_signature, f"{raw_body.decode('utf8')}|{biz_timestamp}"
    )
    if not sig_valid:
        raise HTTPException(status_code=401, detail="Signature verification failed")
    event = WebhookEvent.from_dict(json.loads(raw_body.decode('utf8')))
    logger.info(event)
    logger.info(event.data)


@app.post("/api/callback", response_class=PlainTextResponse)
async def handle_callback(
    request: Request,
    biz_timestamp: Optional[str] = Header(None),
    biz_resp_signature: Optional[str] = Header(None),
):
    raw_body = await request.body()
    sig_valid = verify_signature(
        pubkey, biz_resp_signature, f"{raw_body.decode('utf8')}|{biz_timestamp}"
    )
    tx = Transaction.from_dict(json.loads(raw_body.decode('utf8')))
    logger.info(tx)
    if not sig_valid:
        raise HTTPException(status_code=401, detail="Signature verification failed")
    # Add your own logic here
    # return "deny"
    return "ok"


def verify_signature(public_key, signature, message):
    vk = VerifyKey(key=bytes.fromhex(public_key))
    sha256_hash = hashlib.sha256(hashlib.sha256(message.encode()).digest()).digest()
    try:
        vk.verify(signature=bytes.fromhex(signature), smessage=sha256_hash)
        return True
    except BadSignatureError:
        return False


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888)