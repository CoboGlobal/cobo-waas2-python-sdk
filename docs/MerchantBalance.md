# MerchantBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. | 
**token_id** | **str** | The ID of the cryptocurrency. | 
**acquiring_type** | [**AcquiringType**](AcquiringType.md) |  | 
**total_received_amount** | **str** | The merchant total received amount. | [optional] 
**settled_amount** | **str** | The merchant settled amount. | [optional] 
**payout_amount** | **str** | The merchant payout amount. | [optional] 
**refunded_amount** | **str** | The merchant total refunded amount. | [optional] 
**total_balance** | **str** | The merchant total balance. | [optional] 
**available_balance** | **str** | The merchant available balance. | [optional] 
**locked_balance** | **str** | The merchant locked balance. | [optional] 

## Example

```python
from cobo_waas2.models.merchant_balance import MerchantBalance

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantBalance from a JSON string
merchant_balance_instance = MerchantBalance.from_json(json)
# print the JSON string representation of the object
print(MerchantBalance.to_json())

# convert the object into a dict
merchant_balance_dict = merchant_balance_instance.to_dict()
# create an instance of MerchantBalance from a dict
merchant_balance_from_dict = MerchantBalance.from_dict(merchant_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


