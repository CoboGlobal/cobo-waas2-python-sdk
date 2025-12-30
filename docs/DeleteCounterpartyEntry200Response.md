# DeleteCounterpartyEntry200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_counterparty_entry_id** | **str** | The deleted counterparty entry ID. | 

## Example

```python
from cobo_waas2.models.delete_counterparty_entry200_response import DeleteCounterpartyEntry200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCounterpartyEntry200Response from a JSON string
delete_counterparty_entry200_response_instance = DeleteCounterpartyEntry200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteCounterpartyEntry200Response.to_json())

# convert the object into a dict
delete_counterparty_entry200_response_dict = delete_counterparty_entry200_response_instance.to_dict()
# create an instance of DeleteCounterpartyEntry200Response from a dict
delete_counterparty_entry200_response_from_dict = DeleteCounterpartyEntry200Response.from_dict(delete_counterparty_entry200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


