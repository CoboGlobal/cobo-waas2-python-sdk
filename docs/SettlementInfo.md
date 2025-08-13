# SettlementInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. For developer balance, this field will be empty. | [optional] 
**token_id** | **str** | The ID of the cryptocurrency. | [optional] 
**available_amount** | **str** | This field is no longer in use and can be ignored. | 
**available_currency_balance** | **str** | This field is no longer in use and can be ignored. | [optional] 
**pending_amount** | **str** | This field is no longer in use and can be ignored. | [optional] 
**pending_currency_balance** | **str** | This field is no longer in use and can be ignored. | [optional] 
**settled_amount** | **str** | The amount already settled, in the specified cryptocurrency. | [optional] 
**available_balance** | **str** | The balance available for settlement or refund, in the specified cryptocurrency. | [optional] 
**total_balance** | **str** |  The total unsettled balance in the specified cryptocurrency, including: - Available balance that can be settled immediately - Amounts below the sweep threshold that require forced sweep before settlement  | [optional] 
**acquiring_type** | [**AcquiringType**](AcquiringType.md) |  | [optional] 
**created_timestamp** | **int** | The creation time of the settlement, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The last update time of the settlement, represented as a UNIX timestamp in seconds. | [optional] 

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


