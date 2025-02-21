# CreateBabylonAirdropRegistrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**btc_address** | [**StakingSource**](StakingSource.md) |  | [optional] 
**babylon_address** | [**StakingSource**](StakingSource.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_babylon_airdrop_registration_request import CreateBabylonAirdropRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBabylonAirdropRegistrationRequest from a JSON string
create_babylon_airdrop_registration_request_instance = CreateBabylonAirdropRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBabylonAirdropRegistrationRequest.to_json())

# convert the object into a dict
create_babylon_airdrop_registration_request_dict = create_babylon_airdrop_registration_request_instance.to_dict()
# create an instance of CreateBabylonAirdropRegistrationRequest from a dict
create_babylon_airdrop_registration_request_from_dict = CreateBabylonAirdropRegistrationRequest.from_dict(create_babylon_airdrop_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


