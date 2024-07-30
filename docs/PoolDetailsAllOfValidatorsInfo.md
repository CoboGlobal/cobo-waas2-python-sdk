# PoolDetailsAllOfValidatorsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon_url** | **str** | The URL of the validator&#39;s icon. | 
**name** | **str** | The name of validator. | 
**priority** | **int** | The priority of validator. | [optional] 
**public_key** | **str** | The public key of validator. | 
**commission_rate** | **float** | The commission of validator. | 
**supported_pos_chains** | **List[str]** | The list of supported pos chains. | 
**address** | **str** | The address of validator. | 

## Example

```python
from cobo_waas2.models.pool_details_all_of_validators_info import PoolDetailsAllOfValidatorsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PoolDetailsAllOfValidatorsInfo from a JSON string
pool_details_all_of_validators_info_instance = PoolDetailsAllOfValidatorsInfo.from_json(json)
# print the JSON string representation of the object
print(PoolDetailsAllOfValidatorsInfo.to_json())

# convert the object into a dict
pool_details_all_of_validators_info_dict = pool_details_all_of_validators_info_instance.to_dict()
# create an instance of PoolDetailsAllOfValidatorsInfo from a dict
pool_details_all_of_validators_info_from_dict = PoolDetailsAllOfValidatorsInfo.from_dict(pool_details_all_of_validators_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


