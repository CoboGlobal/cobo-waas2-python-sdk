# AllocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The ID of the cryptocurrency you want to allocation. Supported values:  - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDC&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC&#x60;, &#x60;BSC_USDC&#x60; - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**amount** | **str** | The allocation amount.  | 
**source_account** | **str** |  | 
**destination_account** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from cobo_waas2.models.allocation_request import AllocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationRequest from a JSON string
allocation_request_instance = AllocationRequest.from_json(json)
# print the JSON string representation of the object
print(AllocationRequest.to_json())

# convert the object into a dict
allocation_request_dict = allocation_request_instance.to_dict()
# create an instance of AllocationRequest from a dict
allocation_request_from_dict = AllocationRequest.from_dict(allocation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


