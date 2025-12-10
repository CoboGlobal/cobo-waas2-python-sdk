# DeleteCounterparty200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_id** | **str** | The counterparty ID. | 

## Example

```python
from cobo_waas2.models.delete_counterparty200_response import DeleteCounterparty200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCounterparty200Response from a JSON string
delete_counterparty200_response_instance = DeleteCounterparty200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteCounterparty200Response.to_json())

# convert the object into a dict
delete_counterparty200_response_dict = delete_counterparty200_response_instance.to_dict()
# create an instance of DeleteCounterparty200Response from a dict
delete_counterparty200_response_from_dict = DeleteCounterparty200Response.from_dict(delete_counterparty200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


