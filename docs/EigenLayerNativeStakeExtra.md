# EigenLayerNativeStakeExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**fee_recipient** | **float** | The fee recipient address, if not provided the staker address will be used. | [optional] 

## Example

```python
from cobo_waas2.models.eigen_layer_native_stake_extra import EigenLayerNativeStakeExtra

# TODO update the JSON string below
json = "{}"
# create an instance of EigenLayerNativeStakeExtra from a JSON string
eigen_layer_native_stake_extra_instance = EigenLayerNativeStakeExtra.from_json(json)
# print the JSON string representation of the object
print(EigenLayerNativeStakeExtra.to_json())

# convert the object into a dict
eigen_layer_native_stake_extra_dict = eigen_layer_native_stake_extra_instance.to_dict()
# create an instance of EigenLayerNativeStakeExtra from a dict
eigen_layer_native_stake_extra_from_dict = EigenLayerNativeStakeExtra.from_dict(eigen_layer_native_stake_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


