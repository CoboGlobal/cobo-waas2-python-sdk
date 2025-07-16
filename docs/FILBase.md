# FILBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_base** | **str** | The minimum fee required for a transaction to be included in a block. The base fee is dynamically adjusted based on network congestion to maintain target block utilization. It is burned rather than paid to miners, reducing the total Filecoin supply over time. | [optional] 

## Example

```python
from cobo_waas2.models.fil_base import FILBase

# TODO update the JSON string below
json = "{}"
# create an instance of FILBase from a JSON string
fil_base_instance = FILBase.from_json(json)
# print the JSON string representation of the object
print(FILBase.to_json())

# convert the object into a dict
fil_base_dict = fil_base_instance.to_dict()
# create an instance of FILBase from a dict
fil_base_from_dict = FILBase.from_dict(fil_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


