# QueryGuardPubkey200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubkey** | **str** | guard&#39;s pubkey. | [optional] 
**status** | [**GuardPubkeyStatus**](GuardPubkeyStatus.md) |  | [optional] 
**addresses** | [**List[QueryGuardPubkey200ResponseAddressesInner]**](QueryGuardPubkey200ResponseAddressesInner.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.query_guard_pubkey200_response import QueryGuardPubkey200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryGuardPubkey200Response from a JSON string
query_guard_pubkey200_response_instance = QueryGuardPubkey200Response.from_json(json)
# print the JSON string representation of the object
print(QueryGuardPubkey200Response.to_json())

# convert the object into a dict
query_guard_pubkey200_response_dict = query_guard_pubkey200_response_instance.to_dict()
# create an instance of QueryGuardPubkey200Response from a dict
query_guard_pubkey200_response_from_dict = QueryGuardPubkey200Response.from_dict(query_guard_pubkey200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


