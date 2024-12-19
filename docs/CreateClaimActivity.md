# CreateClaimActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a request. The request ID is provided by you and must be unique within your organization. | [optional] 
**staking_id** | **str** | The ID of the staking position. You can retrieve a list of staking positions by calling [List staking positions](/v2/api-references/stakings/list-staking-positions). | 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.create_claim_activity import CreateClaimActivity

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClaimActivity from a JSON string
create_claim_activity_instance = CreateClaimActivity.from_json(json)
# print the JSON string representation of the object
print(CreateClaimActivity.to_json())

# convert the object into a dict
create_claim_activity_dict = create_claim_activity_instance.to_dict()
# create an instance of CreateClaimActivity from a dict
create_claim_activity_from_dict = CreateClaimActivity.from_dict(create_claim_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


