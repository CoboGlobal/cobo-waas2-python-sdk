# SignatureChallenge

A signature challenge for self-custody wallet verification. The wallet owner must sign the `challenge` string with the wallet associated with `address` and submit the signature via [Submit Travel Rule information for deposits](#operation/submit_deposit_travel_rule_info) or [withdrawals](#operation/submit_withdraw_travel_rule_info). The challenge is time-bounded — each call rotates the challenge and only the most recently-issued value will verify. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The self-custody wallet address that must sign this challenge. This is the counterparty address for the transaction: for deposits it is the sender&#39;s wallet, and for withdrawals it is the recipient&#39;s wallet.  | 
**challenge** | **str** | The human-readable, time-sensitive message to sign. Contains the wallet address, a unique nonce, and a timestamp.  | 
**expires_in** | **int** | Number of seconds before the challenge expires. The signature must be submitted within this window. | 

## Example

```python
from cobo_waas2.models.signature_challenge import SignatureChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureChallenge from a JSON string
signature_challenge_instance = SignatureChallenge.from_json(json)
# print the JSON string representation of the object
print(SignatureChallenge.to_json())

# convert the object into a dict
signature_challenge_dict = signature_challenge_instance.to_dict()
# create an instance of SignatureChallenge from a dict
signature_challenge_from_dict = SignatureChallenge.from_dict(signature_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


