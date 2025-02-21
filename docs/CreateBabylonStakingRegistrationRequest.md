# CreateBabylonStakingRegistrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staking_id** | **str** | The staking id of the phase 1 btc staking position. | [optional] 
**babylon_address** | [**StakingSource**](StakingSource.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_babylon_staking_registration_request import CreateBabylonStakingRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBabylonStakingRegistrationRequest from a JSON string
create_babylon_staking_registration_request_instance = CreateBabylonStakingRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBabylonStakingRegistrationRequest.to_json())

# convert the object into a dict
create_babylon_staking_registration_request_dict = create_babylon_staking_registration_request_instance.to_dict()
# create an instance of CreateBabylonStakingRegistrationRequest from a dict
create_babylon_staking_registration_request_from_dict = CreateBabylonStakingRegistrationRequest.from_dict(create_babylon_staking_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


