# ListBabylonEligibleAirdrops200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BabylonEligibleAirdrop]**](BabylonEligibleAirdrop.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_babylon_eligible_airdrops200_response import ListBabylonEligibleAirdrops200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListBabylonEligibleAirdrops200Response from a JSON string
list_babylon_eligible_airdrops200_response_instance = ListBabylonEligibleAirdrops200Response.from_json(json)
# print the JSON string representation of the object
print(ListBabylonEligibleAirdrops200Response.to_json())

# convert the object into a dict
list_babylon_eligible_airdrops200_response_dict = list_babylon_eligible_airdrops200_response_instance.to_dict()
# create an instance of ListBabylonEligibleAirdrops200Response from a dict
list_babylon_eligible_airdrops200_response_from_dict = ListBabylonEligibleAirdrops200Response.from_dict(list_babylon_eligible_airdrops200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


