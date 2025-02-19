# CreatePrimeBrokerAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[QueryGuardPubkey200ResponseAddressesInner]**](QueryGuardPubkey200ResponseAddressesInner.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_prime_broker_address_request import CreatePrimeBrokerAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePrimeBrokerAddressRequest from a JSON string
create_prime_broker_address_request_instance = CreatePrimeBrokerAddressRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePrimeBrokerAddressRequest.to_json())

# convert the object into a dict
create_prime_broker_address_request_dict = create_prime_broker_address_request_instance.to_dict()
# create an instance of CreatePrimeBrokerAddressRequest from a dict
create_prime_broker_address_request_from_dict = CreatePrimeBrokerAddressRequest.from_dict(create_prime_broker_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


