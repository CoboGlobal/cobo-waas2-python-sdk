# CreatePrimeBrokerAddress201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubkey** | **str** | guard&#39;s pubkey. | 
**addresses** | [**List[QueryGuardPubkey200ResponseAddressesInner]**](QueryGuardPubkey200ResponseAddressesInner.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_prime_broker_address201_response import CreatePrimeBrokerAddress201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePrimeBrokerAddress201Response from a JSON string
create_prime_broker_address201_response_instance = CreatePrimeBrokerAddress201Response.from_json(json)
# print the JSON string representation of the object
print(CreatePrimeBrokerAddress201Response.to_json())

# convert the object into a dict
create_prime_broker_address201_response_dict = create_prime_broker_address201_response_instance.to_dict()
# create an instance of CreatePrimeBrokerAddress201Response from a dict
create_prime_broker_address201_response_from_dict = CreatePrimeBrokerAddress201Response.from_dict(create_prime_broker_address201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


