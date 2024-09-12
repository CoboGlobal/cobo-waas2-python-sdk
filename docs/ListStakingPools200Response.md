# ListStakingPools200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PoolSummary]**](PoolSummary.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_staking_pools200_response import ListStakingPools200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListStakingPools200Response from a JSON string
list_staking_pools200_response_instance = ListStakingPools200Response.from_json(json)
# print the JSON string representation of the object
print(ListStakingPools200Response.to_json())

# convert the object into a dict
list_staking_pools200_response_dict = list_staking_pools200_response_instance.to_dict()
# create an instance of ListStakingPools200Response from a dict
list_staking_pools200_response_from_dict = ListStakingPools200Response.from_dict(list_staking_pools200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


