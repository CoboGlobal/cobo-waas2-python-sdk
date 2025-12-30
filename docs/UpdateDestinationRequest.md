# UpdateDestinationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_destination_name** | **str** | The updated destination name. | 
**updated_destination_type** | [**DestinationType**](DestinationType.md) |  | 
**updated_merchant_id** | **str** | The updated ID of the merchant linked to the destination. | [optional] 
**updated_country** | **str** | The updated country of the destination, in ISO 3166-1 alpha-3 format. | [optional] 
**updated_email** | **str** | The updated email of the destination. | [optional] 
**updated_contact_address** | **str** | The updated contact address of the destination. | [optional] 

## Example

```python
from cobo_waas2.models.update_destination_request import UpdateDestinationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDestinationRequest from a JSON string
update_destination_request_instance = UpdateDestinationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDestinationRequest.to_json())

# convert the object into a dict
update_destination_request_dict = update_destination_request_instance.to_dict()
# create an instance of UpdateDestinationRequest from a dict
update_destination_request_from_dict = UpdateDestinationRequest.from_dict(update_destination_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


