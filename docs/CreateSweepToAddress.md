# CreateSweepToAddress

The information of create sweep to address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The wallet ID. | 
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | 

## Example

```python
from cobo_waas2.models.create_sweep_to_address import CreateSweepToAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSweepToAddress from a JSON string
create_sweep_to_address_instance = CreateSweepToAddress.from_json(json)
# print the JSON string representation of the object
print(CreateSweepToAddress.to_json())

# convert the object into a dict
create_sweep_to_address_dict = create_sweep_to_address_instance.to_dict()
# create an instance of CreateSweepToAddress from a dict
create_sweep_to_address_from_dict = CreateSweepToAddress.from_dict(create_sweep_to_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


