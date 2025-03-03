# BabylonAirdropPop

Proof of Participation (PoP) details used for airdrop registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baby_address** | **str** | The Babylon (BABY) address used to receive BABY rewards. | 
**btc_address** | **str** | The Bitcoin (BTC) address used for staking. | 
**btc_public_key** | **str** | The public key corresponding to the &#x60;btc_address&#x60;, represented in hex format. | 
**btc_sign_baby** | **str** | A BTC signature that signs the &#x60;baby_address&#x60;. | 
**baby_sign_btc** | **str** | A BABY signature that signs the &#x60;btc_address&#x60;. | 
**baby_public_key** | **str** | The public key corresponding to the &#x60;baby_address&#x60;, represented in base64 format. | 

## Example

```python
from cobo_waas2.models.babylon_airdrop_pop import BabylonAirdropPop

# TODO update the JSON string below
json = "{}"
# create an instance of BabylonAirdropPop from a JSON string
babylon_airdrop_pop_instance = BabylonAirdropPop.from_json(json)
# print the JSON string representation of the object
print(BabylonAirdropPop.to_json())

# convert the object into a dict
babylon_airdrop_pop_dict = babylon_airdrop_pop_instance.to_dict()
# create an instance of BabylonAirdropPop from a dict
babylon_airdrop_pop_from_dict = BabylonAirdropPop.from_dict(babylon_airdrop_pop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


