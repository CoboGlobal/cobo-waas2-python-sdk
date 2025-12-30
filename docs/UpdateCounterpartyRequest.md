# UpdateCounterpartyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_counterparty_name** | **str** | The updated counterparty name. | 
**updated_counterparty_type** | [**CounterpartyType**](CounterpartyType.md) |  | 
**updated_country** | **str** | The updated country of the counterparty, in ISO 3166-1 alpha-3 format. | [optional] 
**updated_email** | **str** | The updated email of the counterparty. | [optional] 
**updated_contact_address** | **str** | The updated contact address of the counterparty. | [optional] 

## Example

```python
from cobo_waas2.models.update_counterparty_request import UpdateCounterpartyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCounterpartyRequest from a JSON string
update_counterparty_request_instance = UpdateCounterpartyRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCounterpartyRequest.to_json())

# convert the object into a dict
update_counterparty_request_dict = update_counterparty_request_instance.to_dict()
# create an instance of UpdateCounterpartyRequest from a dict
update_counterparty_request_from_dict = UpdateCounterpartyRequest.from_dict(update_counterparty_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


