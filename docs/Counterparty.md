# Counterparty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_id** | **str** | The counterparty ID. | [optional] 
**counterparty_type** | [**CounterpartyType**](CounterpartyType.md) |  | 
**counterparty_name** | **str** | The counterparty name. | 
**country** | **str** | The country of the counterparty, in ISO 3166-1 alpha-3 format. | [optional] 
**email** | **str** | The email of the counterparty. | [optional] 
**contact_address** | **str** | The contact address of the counterparty. | [optional] 
**created_timestamp** | **int** | The created time of the counterparty, represented as a UNIX timestamp in seconds. | 
**updated_timestamp** | **int** | The updated time of the counterparty, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.counterparty import Counterparty

# TODO update the JSON string below
json = "{}"
# create an instance of Counterparty from a JSON string
counterparty_instance = Counterparty.from_json(json)
# print the JSON string representation of the object
print(Counterparty.to_json())

# convert the object into a dict
counterparty_dict = counterparty_instance.to_dict()
# create an instance of Counterparty from a dict
counterparty_from_dict = Counterparty.from_dict(counterparty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


