# PaymentBalanceChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | The source ID of the balance change. | 
**source_type** | [**PaymentBalanceChangeSourceType**](PaymentBalanceChangeSourceType.md) |  | 
**token_id** | **str** | The token ID of the balance change. | 
**amount** | **str** | The balance change amount, truncated to two decimal places and represented as a numeric string. | 
**amount_raw** | **str** | The balance change amount in the token&#39;s decimal precision, represented as a numeric string. | 
**balance_before** | **str** | The account balance before the balance change, truncated to two decimal places and represented as a numeric string. | 
**balance_before_raw** | **str** | The account balance before the balance change in the token&#39;s decimal precision, represented as a numeric string. | 
**balance_after** | **str** | The account balance after the balance change, truncated to two decimal places and represented as a numeric string. | 
**balance_after_raw** | **str** | The account balance after the balance change in the token&#39;s decimal precision, represented as a numeric string. | 
**flow_direction** | [**PaymentBalanceFlowDirection**](PaymentBalanceFlowDirection.md) |  | 
**created_timestamp** | **int** | The time when the balance change was created, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.payment_balance_change import PaymentBalanceChange

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBalanceChange from a JSON string
payment_balance_change_instance = PaymentBalanceChange.from_json(json)
# print the JSON string representation of the object
print(PaymentBalanceChange.to_json())

# convert the object into a dict
payment_balance_change_dict = payment_balance_change_instance.to_dict()
# create an instance of PaymentBalanceChange from a dict
payment_balance_change_from_dict = PaymentBalanceChange.from_dict(payment_balance_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


