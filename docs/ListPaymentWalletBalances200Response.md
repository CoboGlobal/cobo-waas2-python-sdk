# ListPaymentWalletBalances200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PaymentWalletBalance]**](PaymentWalletBalance.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_payment_wallet_balances200_response import ListPaymentWalletBalances200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPaymentWalletBalances200Response from a JSON string
list_payment_wallet_balances200_response_instance = ListPaymentWalletBalances200Response.from_json(json)
# print the JSON string representation of the object
print(ListPaymentWalletBalances200Response.to_json())

# convert the object into a dict
list_payment_wallet_balances200_response_dict = list_payment_wallet_balances200_response_instance.to_dict()
# create an instance of ListPaymentWalletBalances200Response from a dict
list_payment_wallet_balances200_response_from_dict = ListPaymentWalletBalances200Response.from_dict(list_payment_wallet_balances200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


