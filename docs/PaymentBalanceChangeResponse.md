# PaymentBalanceChangeResponse

The response containing balance changes and pagination information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PaymentBalanceChange]**](PaymentBalanceChange.md) | The list of balance changes. | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.payment_balance_change_response import PaymentBalanceChangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBalanceChangeResponse from a JSON string
payment_balance_change_response_instance = PaymentBalanceChangeResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentBalanceChangeResponse.to_json())

# convert the object into a dict
payment_balance_change_response_dict = payment_balance_change_response_instance.to_dict()
# create an instance of PaymentBalanceChangeResponse from a dict
payment_balance_change_response_from_dict = PaymentBalanceChangeResponse.from_dict(payment_balance_change_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


