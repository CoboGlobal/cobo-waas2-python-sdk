# CreateUnstakeActivityExtra

Additional protocol-specific information required for the unstaking operation. The required fields vary depending on the staking protocol.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**validator_pubkeys** | **List[str]** | A list of public keys identifying the validators to unstake from the Ethereum Beacon Chain. | 

## Example

```python
from cobo_waas2.models.create_unstake_activity_extra import CreateUnstakeActivityExtra

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUnstakeActivityExtra from a JSON string
create_unstake_activity_extra_instance = CreateUnstakeActivityExtra.from_json(json)
# print the JSON string representation of the object
print(CreateUnstakeActivityExtra.to_json())

# convert the object into a dict
create_unstake_activity_extra_dict = create_unstake_activity_extra_instance.to_dict()
# create an instance of CreateUnstakeActivityExtra from a dict
create_unstake_activity_extra_from_dict = CreateUnstakeActivityExtra.from_dict(create_unstake_activity_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


