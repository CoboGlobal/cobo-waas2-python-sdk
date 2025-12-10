# CommissionFeeDetail

Commission fee detail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission_fee_id** | **str** | Unique ID of the commission fee | [optional] 
**asset_id** | **str** | Asset ID | [optional] 
**fee_tokens** | **List[str]** | List of fee token IDs | [optional] 
**settle_type** | [**SettleType**](SettleType.md) |  | [optional] 
**business_type_id** | **int** | Unique ID of business type | [optional] 
**normalized_amount** | [**CommissionFeeDetailNormalizedAmount**](CommissionFeeDetailNormalizedAmount.md) |  | [optional] 
**strategy_id** | **int** | Strategy ID | [optional] 
**rule_id** | **int** | Rule ID | [optional] 
**strategy_params** | [**StrategyParams**](StrategyParams.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.commission_fee_detail import CommissionFeeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionFeeDetail from a JSON string
commission_fee_detail_instance = CommissionFeeDetail.from_json(json)
# print the JSON string representation of the object
print(CommissionFeeDetail.to_json())

# convert the object into a dict
commission_fee_detail_dict = commission_fee_detail_instance.to_dict()
# create an instance of CommissionFeeDetail from a dict
commission_fee_detail_from_dict = CommissionFeeDetail.from_dict(commission_fee_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


