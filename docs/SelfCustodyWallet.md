# SelfCustodyWallet

Required information when depositing from or withdrawing to a self-custody wallet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_wallet_type** | [**DestinationWalletType**](DestinationWalletType.md) |  | 
**self_custody_wallet_challenge** | **str** | The message obtained from the &#x60;Retrieve transaction limitations&#x60; operation. This message is used to verify wallet ownership through signing. | 
**self_custody_wallet_address** | **str** | The address of the self-custody wallet. | 
**self_custody_wallet_sign** | **str** | The signature created by signing the challenge message with the wallet&#39;s private key. | 

## Example

```python
from cobo_waas2.models.self_custody_wallet import SelfCustodyWallet

# TODO update the JSON string below
json = "{}"
# create an instance of SelfCustodyWallet from a JSON string
self_custody_wallet_instance = SelfCustodyWallet.from_json(json)
# print the JSON string representation of the object
print(SelfCustodyWallet.to_json())

# convert the object into a dict
self_custody_wallet_dict = self_custody_wallet_instance.to_dict()
# create an instance of SelfCustodyWallet from a dict
self_custody_wallet_from_dict = SelfCustodyWallet.from_dict(self_custody_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


