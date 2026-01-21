# PaymentBulkSendItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulk_send_item_id** | **str** | The payout item ID. | 
**token_id** | **str** | The token ID of the payout item. | 
**receiving_address** | **str** | The receiving address of the payout item. | 
**amount** | **str** | The amount of the payout item. | 
**description** | **str** | The note of the payout item. | [optional] 
**status** | [**PaymentBulkSendItemStatus**](PaymentBulkSendItemStatus.md) |  | 
**validation_status** | [**PaymentBulkSendItemValidationStatus**](PaymentBulkSendItemValidationStatus.md) |  | 

## Example

```python
from cobo_waas2.models.payment_bulk_send_item import PaymentBulkSendItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBulkSendItem from a JSON string
payment_bulk_send_item_instance = PaymentBulkSendItem.from_json(json)
# print the JSON string representation of the object
print(PaymentBulkSendItem.to_json())

# convert the object into a dict
payment_bulk_send_item_dict = payment_bulk_send_item_instance.to_dict()
# create an instance of PaymentBulkSendItem from a dict
payment_bulk_send_item_from_dict = PaymentBulkSendItem.from_dict(payment_bulk_send_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


