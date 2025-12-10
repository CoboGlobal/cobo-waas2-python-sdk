# UpdateCounterpartyByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_name** | **str** | The counterparty name. | 
**counterparty_type** | [**CounterpartyType**](CounterpartyType.md) |  | 
**country** | **str** | The country of the counterparty, in ISO 3166-1 alpha-3 format. | [optional] 
**email** | **str** | The email of the counterparty. | [optional] 
**contact_address** | **str** | The contact address of the counterparty. | [optional] 

## Example

```python
from cobo_waas2.models.update_counterparty_by_id_request import UpdateCounterpartyByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCounterpartyByIdRequest from a JSON string
update_counterparty_by_id_request_instance = UpdateCounterpartyByIdRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCounterpartyByIdRequest.to_json())

# convert the object into a dict
update_counterparty_by_id_request_dict = update_counterparty_by_id_request_instance.to_dict()
# create an instance of UpdateCounterpartyByIdRequest from a dict
update_counterparty_by_id_request_from_dict = UpdateCounterpartyByIdRequest.from_dict(update_counterparty_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


