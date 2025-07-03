# FILBase

The transaction gas base based on the FIL fee model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_base** | **str** | This is the minimum fee required to include a transaction in a block. It is determined by the network&#39;s congestion level, which adjusts to maintain a target block utilization rate. The base fee is burned, reducing the total supply of Filecoin over time. | [optional] 

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


