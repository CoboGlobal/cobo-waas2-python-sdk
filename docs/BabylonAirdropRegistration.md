# BabylonAirdropRegistration

The babylon airdrop registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for tracking the airdrop registrgtiontration | [optional] 
**status** | [**BabylonRegistrationRequestStatus**](BabylonRegistrationRequestStatus.md) |  | [optional] 
**btc_address** | [**StakingSource**](StakingSource.md) |  | [optional] 
**babylon_address** | [**StakingSource**](StakingSource.md) |  | [optional] 
**airdrop_amount** | **str** | Actual airdrop amount being claimed | [optional] 
**error_message** | **str** | Detailed error message if failed | [optional] 
**created_timestamp** | **int** | The timestamp when the registration was created | [optional] 
**updated_timestamp** | **int** | The timestamp when the registration was updated | [optional] 

## Example

```python
from cobo_waas2.models.babylon_airdrop_registration import BabylonAirdropRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of BabylonAirdropRegistration from a JSON string
babylon_airdrop_registration_instance = BabylonAirdropRegistration.from_json(json)
# print the JSON string representation of the object
print(BabylonAirdropRegistration.to_json())

# convert the object into a dict
babylon_airdrop_registration_dict = babylon_airdrop_registration_instance.to_dict()
# create an instance of BabylonAirdropRegistration from a dict
babylon_airdrop_registration_from_dict = BabylonAirdropRegistration.from_dict(babylon_airdrop_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


