# PaymentOrderDeposit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The incoming Payment transaction ID. | 
**tx_hash** | **str** | The blockchain transaction hash. | 
**amount** | [**PaymentAssetAmount**](PaymentAssetAmount.md) |  | 
**source_address** | **str** | The source address of the incoming transaction. | 
**status** | [**PaymentPayInStatus**](PaymentPayInStatus.md) |  | 
**screening_mode** | [**PaymentScreeningMode**](PaymentScreeningMode.md) |  | 
**is_late** | **bool** | Whether the incoming transaction completed after the order reached a terminal status. | 
**message** | **str** | The action prompt for an &#x60;ActionRequired&#x60; status. | 
**failed_reason** | [**PaymentFailedReason**](PaymentFailedReason.md) |  | 

## Example

```python
from cobo_waas2.models.payment_order_deposit import PaymentOrderDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentOrderDeposit from a JSON string
payment_order_deposit_instance = PaymentOrderDeposit.from_json(json)
# print the JSON string representation of the object
print(PaymentOrderDeposit.to_json())

# convert the object into a dict
payment_order_deposit_dict = payment_order_deposit_instance.to_dict()
# create an instance of PaymentOrderDeposit from a dict
payment_order_deposit_from_dict = PaymentOrderDeposit.from_dict(payment_order_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


