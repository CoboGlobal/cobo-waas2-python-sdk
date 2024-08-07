# CreateAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](/v2/api-references/wallets/list-enabled-chains). | 
**count** | **int** | The number of addresses to create. | [default to 1]
**encoding** | [**AddressEncoding**](AddressEncoding.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_address_request import CreateAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddressRequest from a JSON string
create_address_request_instance = CreateAddressRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAddressRequest.to_json())

# convert the object into a dict
create_address_request_dict = create_address_request_instance.to_dict()
# create an instance of CreateAddressRequest from a dict
create_address_request_from_dict = CreateAddressRequest.from_dict(create_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


