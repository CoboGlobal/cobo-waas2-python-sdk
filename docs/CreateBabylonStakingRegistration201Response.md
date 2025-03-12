# CreateBabylonStakingRegistration201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_id** | **str** | The registration ID, a unique identifier for tracking the Babylon Phase-2 registration request. You can use it with the [Get Babylon Phase-2 registration details operation](https://www.cobo.com/developers/v2/api-references/stakings/get-babylon-phase-2-registration-details) to check the registration status. | [optional] 

## Example

```python
from cobo_waas2.models.create_babylon_staking_registration201_response import CreateBabylonStakingRegistration201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBabylonStakingRegistration201Response from a JSON string
create_babylon_staking_registration201_response_instance = CreateBabylonStakingRegistration201Response.from_json(json)
# print the JSON string representation of the object
print(CreateBabylonStakingRegistration201Response.to_json())

# convert the object into a dict
create_babylon_staking_registration201_response_dict = create_babylon_staking_registration201_response_instance.to_dict()
# create an instance of CreateBabylonStakingRegistration201Response from a dict
create_babylon_staking_registration201_response_from_dict = CreateBabylonStakingRegistration201Response.from_dict(create_babylon_staking_registration201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


