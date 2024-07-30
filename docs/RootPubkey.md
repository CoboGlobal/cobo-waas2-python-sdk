# RootPubkey

The data for MPC Root Extended Public Key information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubkey** | **str** | The vault&#39;s [root extended public key](https://manuals.cobo.com/en/portal/mpc-wallets/ocw/tss-node-deployment#tss-node-on-cobo-portal-and-mpc-root-extended-public-key). | [optional] 
**curve** | [**CurveType**](CurveType.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.root_pubkey import RootPubkey

# TODO update the JSON string below
json = "{}"
# create an instance of RootPubkey from a JSON string
root_pubkey_instance = RootPubkey.from_json(json)
# print the JSON string representation of the object
print(RootPubkey.to_json())

# convert the object into a dict
root_pubkey_dict = root_pubkey_instance.to_dict()
# create an instance of RootPubkey from a dict
root_pubkey_from_dict = RootPubkey.from_dict(root_pubkey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


