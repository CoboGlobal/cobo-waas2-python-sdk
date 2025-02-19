# Vasp

The information of a virtual asset service provider (VASP).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The VASP name. | 
**vendor_code** | **str** | The vendor code of the VASP. | 
**vendor_vasp_id** | **str** | The VASP ID. | 

## Example

```python
from cobo_waas2.models.vasp import Vasp

# TODO update the JSON string below
json = "{}"
# create an instance of Vasp from a JSON string
vasp_instance = Vasp.from_json(json)
# print the JSON string representation of the object
print(Vasp.to_json())

# convert the object into a dict
vasp_dict = vasp_instance.to_dict()
# create an instance of Vasp from a dict
vasp_from_dict = Vasp.from_dict(vasp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


