# UpdateDestinationByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_name** | **str** | The destination name. | 
**destination_type** | [**DestinationType**](DestinationType.md) |  | 
**merchant_id** | **str** | The ID of the merchant linked to the destination. | [optional] 
**country** | **str** | The country of the destination, in ISO 3166-1 alpha-3 format. | [optional] 
**email** | **str** | The email of the destination. | [optional] 
**contact_address** | **str** | The contact address of the destination. | [optional] 

## Example

```python
from cobo_waas2.models.update_destination_by_id_request import UpdateDestinationByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDestinationByIdRequest from a JSON string
update_destination_by_id_request_instance = UpdateDestinationByIdRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDestinationByIdRequest.to_json())

# convert the object into a dict
update_destination_by_id_request_dict = update_destination_by_id_request_instance.to_dict()
# create an instance of UpdateDestinationByIdRequest from a dict
update_destination_by_id_request_from_dict = UpdateDestinationByIdRequest.from_dict(update_destination_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


