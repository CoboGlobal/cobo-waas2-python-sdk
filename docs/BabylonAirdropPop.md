# BabylonAirdropPop

Pop information to be used for airdrop registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baby_address** | **str** | BABY address | 
**btc_address** | **str** | BTC address | 
**btc_public_key** | **str** | BTC public key in hex format | 
**btc_sign_baby** | **str** | BTC sign BABY | 
**baby_sign_btc** | **str** | BABY sign BTC | 
**baby_public_key** | **str** | BABY public key in base64 format | 

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


