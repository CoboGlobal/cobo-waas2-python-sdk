# EigenLayerLstStakeExtra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_type** | [**StakingPoolType**](StakingPoolType.md) |  | 
**operator** | **str** | The operator address. | [optional] 

## Example

```python
from cobo_waas2.models.eigen_layer_lst_stake_extra import EigenLayerLstStakeExtra

# TODO update the JSON string below
json = "{}"
# create an instance of EigenLayerLstStakeExtra from a JSON string
eigen_layer_lst_stake_extra_instance = EigenLayerLstStakeExtra.from_json(json)
# print the JSON string representation of the object
print(EigenLayerLstStakeExtra.to_json())

# convert the object into a dict
eigen_layer_lst_stake_extra_dict = eigen_layer_lst_stake_extra_instance.to_dict()
# create an instance of EigenLayerLstStakeExtra from a dict
eigen_layer_lst_stake_extra_from_dict = EigenLayerLstStakeExtra.from_dict(eigen_layer_lst_stake_extra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


