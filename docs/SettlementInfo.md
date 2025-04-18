# SettlementInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. For payment gateway balance, this field will be empty. | [optional] 
**token_id** | **str** | The ID of the cryptocurrency token. | [optional] 
**available_amount** | **str** | The amount available for settlement in the specified cryptocurrency token. | 
**available_currency_balance** | **str** | The available currency balance. | [optional] 
**pending_amount** | **str** | The pending amount. | [optional] 
**pending_currency_balance** | **str** | The pending currency balance. | [optional] 

## Example

```python
from cobo_waas2.models.settlement_info import SettlementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementInfo from a JSON string
settlement_info_instance = SettlementInfo.from_json(json)
# print the JSON string representation of the object
print(SettlementInfo.to_json())

# convert the object into a dict
settlement_info_dict = settlement_info_instance.to_dict()
# create an instance of SettlementInfo from a dict
settlement_info_from_dict = SettlementInfo.from_dict(settlement_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


