# PreCheck

Some validation settings for creating a transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_checks** | [**List[SkipCheckType]**](SkipCheckType.md) | Selection to skip verification. | [optional] 

## Example

```python
from cobo_waas2.models.pre_check import PreCheck

# TODO update the JSON string below
json = "{}"
# create an instance of PreCheck from a JSON string
pre_check_instance = PreCheck.from_json(json)
# print the JSON string representation of the object
print(PreCheck.to_json())

# convert the object into a dict
pre_check_dict = pre_check_instance.to_dict()
# create an instance of PreCheck from a dict
pre_check_from_dict = PreCheck.from_dict(pre_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


