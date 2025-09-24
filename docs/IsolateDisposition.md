# IsolateDisposition

The information about a fund isolate disposition request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The UUID of the transaction to be isolated. This identifies the original transaction that requires isolation processing. | 
**destination_address** | **str** | The blockchain address where the isolated funds will be sent. | 
**disposition_amount** | **str** | The amount to be isolated from the original transaction, specified as a numeric string. This value cannot exceed the total amount of the original transaction.  | 
**category_names** | **List[str]** | Custom categories to identify and track this isolate transaction. Used for transaction classification and reporting. | [optional] 
**description** | **str** | Additional notes or description for this isolate disposition. | [optional] 

## Example

```python
from cobo_waas2.models.isolate_disposition import IsolateDisposition

# TODO update the JSON string below
json = "{}"
# create an instance of IsolateDisposition from a JSON string
isolate_disposition_instance = IsolateDisposition.from_json(json)
# print the JSON string representation of the object
print(IsolateDisposition.to_json())

# convert the object into a dict
isolate_disposition_dict = isolate_disposition_instance.to_dict()
# create an instance of IsolateDisposition from a dict
isolate_disposition_from_dict = IsolateDisposition.from_dict(isolate_disposition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


