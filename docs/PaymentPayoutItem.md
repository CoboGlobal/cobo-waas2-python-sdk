# PaymentPayoutItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID of the payout item. | 
**amount** | **str** | The amount of the payout item.  | 
**bridging_fee** | [**BridgingFee**](BridgingFee.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.payment_payout_item import PaymentPayoutItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPayoutItem from a JSON string
payment_payout_item_instance = PaymentPayoutItem.from_json(json)
# print the JSON string representation of the object
print(PaymentPayoutItem.to_json())

# convert the object into a dict
payment_payout_item_dict = payment_payout_item_instance.to_dict()
# create an instance of PaymentPayoutItem from a dict
payment_payout_item_from_dict = PaymentPayoutItem.from_dict(payment_payout_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


