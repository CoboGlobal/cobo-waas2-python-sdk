# ActivityInitiator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_initiator** | **str** | The initiator of the staking activity. If you do not specify this property, the WaaS service will automatically designate the API key as the initiator. | [optional] 

## Example

```python
from cobo_waas2.models.activity_initiator import ActivityInitiator

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityInitiator from a JSON string
activity_initiator_instance = ActivityInitiator.from_json(json)
# print the JSON string representation of the object
print(ActivityInitiator.to_json())

# convert the object into a dict
activity_initiator_dict = activity_initiator_instance.to_dict()
# create an instance of ActivityInitiator from a dict
activity_initiator_from_dict = ActivityInitiator.from_dict(activity_initiator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


