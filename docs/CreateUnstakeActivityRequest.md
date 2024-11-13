# CreateUnstakeActivityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a request. The request ID is provided by you and must be unique within your organization. | [optional] 
**staking_id** | **str** | The ID of the corresponding staking position. | 
**amount** | **str** | The amount to unstake. For the Babylon protocol, this property is ignored. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 
**extra** | [**CreateUnstakeActivityExtra**](CreateUnstakeActivityExtra.md) |  | [optional] 
**app_initiator** | **str** | The initiator of the staking activity. If you do not specify this property, the WaaS service will automatically designate the API key as the initiator. | [optional] 

## Example

```python
from cobo_waas2.models.create_unstake_activity_request import CreateUnstakeActivityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUnstakeActivityRequest from a JSON string
create_unstake_activity_request_instance = CreateUnstakeActivityRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUnstakeActivityRequest.to_json())

# convert the object into a dict
create_unstake_activity_request_dict = create_unstake_activity_request_instance.to_dict()
# create an instance of CreateUnstakeActivityRequest from a dict
create_unstake_activity_request_from_dict = CreateUnstakeActivityRequest.from_dict(create_unstake_activity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


