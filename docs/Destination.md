# Destination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_id** | **str** | The destination ID. | [optional] 
**destination_type** | [**DestinationType**](DestinationType.md) |  | 
**destination_name** | **str** | The destination name. | 
**country** | **str** | The country of the destination, in ISO 3166-1 alpha-3 format. | [optional] 
**email** | **str** | The email of the destination. | [optional] 
**contact_address** | **str** | The contact address of the destination. | [optional] 
**merchant_id** | **str** | The ID of the merchant linked to the destination. | [optional] 
**created_timestamp** | **int** | The created time of the destination, represented as a UNIX timestamp in seconds. | 
**updated_timestamp** | **int** | The updated time of the destination, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.destination import Destination

# TODO update the JSON string below
json = "{}"
# create an instance of Destination from a JSON string
destination_instance = Destination.from_json(json)
# print the JSON string representation of the object
print(Destination.to_json())

# convert the object into a dict
destination_dict = destination_instance.to_dict()
# create an instance of Destination from a dict
destination_from_dict = Destination.from_dict(destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


