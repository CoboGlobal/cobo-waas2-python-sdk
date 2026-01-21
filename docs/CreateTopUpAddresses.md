# CreateTopUpAddresses

The request body to batch create top-up addresses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. If not provided, the default merchant created during organization initialization will be used. | [optional] 
**token_id** | **str** | The token ID, which identifies the cryptocurrency.  | 
**custom_payer_ids** | **List[str]** | A list of unique custom payer IDs required to create top-up addresses. The maximum number of items is 50.  | 

## Example

```python
from cobo_waas2.models.create_top_up_addresses import CreateTopUpAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTopUpAddresses from a JSON string
create_top_up_addresses_instance = CreateTopUpAddresses.from_json(json)
# print the JSON string representation of the object
print(CreateTopUpAddresses.to_json())

# convert the object into a dict
create_top_up_addresses_dict = create_top_up_addresses_instance.to_dict()
# create an instance of CreateTopUpAddresses from a dict
create_top_up_addresses_from_dict = CreateTopUpAddresses.from_dict(create_top_up_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


