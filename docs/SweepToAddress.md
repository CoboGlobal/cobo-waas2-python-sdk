# SweepToAddress

The sweep to address information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet address. | 
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | 
**status** | [**SweepToAddressStatus**](SweepToAddressStatus.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.sweep_to_address import SweepToAddress

# TODO update the JSON string below
json = "{}"
# create an instance of SweepToAddress from a JSON string
sweep_to_address_instance = SweepToAddress.from_json(json)
# print the JSON string representation of the object
print(SweepToAddress.to_json())

# convert the object into a dict
sweep_to_address_dict = sweep_to_address_instance.to_dict()
# create an instance of SweepToAddress from a dict
sweep_to_address_from_dict = SweepToAddress.from_dict(sweep_to_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


