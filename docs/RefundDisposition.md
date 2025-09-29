# RefundDisposition

The information about a fund refund disposition request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The UUID of the transaction to be refunded. This identifies the original transaction that requires refund processing. | 
**destination_address** | **str** | The blockchain address where the refunded funds will be sent. | 
**disposition_amount** | **str** | The amount to be refunded from the original transaction, specified as a numeric string. This value cannot exceed the total amount of the original transaction.  | 
**category_names** | **List[str]** | Custom categories to identify and track this refund transaction. Used for transaction classification and reporting. | [optional] 
**description** | **str** | Additional notes or description for this refund disposition. | [optional] 

## Example

```python
from cobo_waas2.models.refund_disposition import RefundDisposition

# TODO update the JSON string below
json = "{}"
# create an instance of RefundDisposition from a JSON string
refund_disposition_instance = RefundDisposition.from_json(json)
# print the JSON string representation of the object
print(RefundDisposition.to_json())

# convert the object into a dict
refund_disposition_dict = refund_disposition_instance.to_dict()
# create an instance of RefundDisposition from a dict
refund_disposition_from_dict = RefundDisposition.from_dict(refund_disposition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


