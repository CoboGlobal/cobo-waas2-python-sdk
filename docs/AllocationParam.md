# AllocationParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The ID of the cryptocurrency you want to allocation. Supported values:  - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDC&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC&#x60;, &#x60;BSC_USDC&#x60; - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**amount** | **str** | The allocation amount.  | 
**source_account** | **str** | The source account from which the allocation will be deducted. - If the source account is a merchant account, provide the merchant&#39;s ID (e.g., \&quot;M1001\&quot;). - If the source account is the developer account, use the string &#x60;\&quot;developer\&quot;&#x60;.  | 
**destination_account** | **str** | The destination account to which the allocation will be credited. - If the destination account is a merchant account, provide the merchant&#39;s ID (e.g., \&quot;M1001\&quot;). - If the destination account is the developer account, use the string &#x60;\&quot;developer\&quot;&#x60;.  | 
**description** | **str** | The description of the allocation. | 

## Example

```python
from cobo_waas2.models.allocation_param import AllocationParam

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationParam from a JSON string
allocation_param_instance = AllocationParam.from_json(json)
# print the JSON string representation of the object
print(AllocationParam.to_json())

# convert the object into a dict
allocation_param_dict = allocation_param_instance.to_dict()
# create an instance of AllocationParam from a dict
allocation_param_from_dict = AllocationParam.from_dict(allocation_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


