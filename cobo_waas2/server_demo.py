import hashlib
import json
import logging
from typing import Optional

import ed25519
from fastapi import FastAPI, Header, HTTPException, Request

from cobo_waas2 import WebhookEvent, Transaction


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# 替换成对应环境的pub key
pub_keys = {
    "DEV": "a04ea1d5fa8da71f1dcfccf972b9c4eba0a2d8aba1f6da26f49977b08a0d2718",
    "PROD": "8d4a482641adb2a34b726f05827dba9a9653e5857469b8749052bf4458a86729",
}

pubkey = pub_keys["DEV"]


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


@app.post("/api/callback")
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
    vk = ed25519.VerifyingKey(bytes.fromhex(public_key))
    sha256_hash = hashlib.sha256(hashlib.sha256(message.encode()).digest()).digest()
    try:
        vk.verify(bytes.fromhex(signature), sha256_hash)
        return True
    except ed25519.BadSignatureError:
        return False


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888)