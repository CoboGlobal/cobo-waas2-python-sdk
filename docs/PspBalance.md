# PspBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. | 
**developer_fee_amount** | **str** | The total amount of the token that has been received as developer fee. | [optional] 
**settled_amount** | **str** | The total amount of the token that has been settled from the developer&#39;s balance. | [optional] 
**refunded_amount** | **str** | The total amount of the token that has been refunded from the developer&#39;s balance. | [optional] 
**total_balance** | **str** | The total balance of the token for the developer. | [optional] 
**available_balance** | **str** | The balance available for settlement or refund, in the specified cryptocurrency. | [optional] 

## Example

```python
from cobo_waas2.models.psp_balance import PspBalance

# TODO update the JSON string below
json = "{}"
# create an instance of PspBalance from a JSON string
psp_balance_instance = PspBalance.from_json(json)
# print the JSON string representation of the object
print(PspBalance.to_json())

# convert the object into a dict
psp_balance_dict = psp_balance_instance.to_dict()
# create an instance of PspBalance from a dict
psp_balance_from_dict = PspBalance.from_dict(psp_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


