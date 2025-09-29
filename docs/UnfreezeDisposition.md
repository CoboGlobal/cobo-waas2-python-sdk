# UnfreezeDisposition

The information about a fund unfreeze disposition request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The UUID of the transaction to be unfrozen. This identifies the frozen transaction that needs to be released. | 

## Example

```python
from cobo_waas2.models.unfreeze_disposition import UnfreezeDisposition

# TODO update the JSON string below
json = "{}"
# create an instance of UnfreezeDisposition from a JSON string
unfreeze_disposition_instance = UnfreezeDisposition.from_json(json)
# print the JSON string representation of the object
print(UnfreezeDisposition.to_json())

# convert the object into a dict
unfreeze_disposition_dict = unfreeze_disposition_instance.to_dict()
# create an instance of UnfreezeDisposition from a dict
unfreeze_disposition_from_dict = UnfreezeDisposition.from_dict(unfreeze_disposition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


