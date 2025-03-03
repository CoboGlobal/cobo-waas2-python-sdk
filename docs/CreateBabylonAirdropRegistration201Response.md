# CreateBabylonAirdropRegistration201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_id** | **str** | The registration ID, a unique identifier for tracking the airdrop registration request. You can check the registration status with the [Get Babylon airdrop registration details](https://www.cobo.com/developers/v2/api-references/stakings/get_babylon_airdrop_registration_details) operation. | [optional] 

## Example

```python
from cobo_waas2.models.create_babylon_airdrop_registration201_response import CreateBabylonAirdropRegistration201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBabylonAirdropRegistration201Response from a JSON string
create_babylon_airdrop_registration201_response_instance = CreateBabylonAirdropRegistration201Response.from_json(json)
# print the JSON string representation of the object
print(CreateBabylonAirdropRegistration201Response.to_json())

# convert the object into a dict
create_babylon_airdrop_registration201_response_dict = create_babylon_airdrop_registration201_response_instance.to_dict()
# create an instance of CreateBabylonAirdropRegistration201Response from a dict
create_babylon_airdrop_registration201_response_from_dict = CreateBabylonAirdropRegistration201Response.from_dict(create_babylon_airdrop_registration201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


