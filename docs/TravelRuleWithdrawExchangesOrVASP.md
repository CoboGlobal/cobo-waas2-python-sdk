# TravelRuleWithdrawExchangesOrVASP

Required fields for `EXCHANGES_OR_VASP`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_wallet_type** | [**DestinationWalletType**](DestinationWalletType.md) |  | 
**vendor_code** | **str** | The vendor code for exchanges or VASPs. | 
**vendor_vasp_id** | **str** | The unique identifier of the VASP. | 
**entity_info** | [**TravelRuleWithdrawExchangesOrVASPEntityInfo**](TravelRuleWithdrawExchangesOrVASPEntityInfo.md) |  | 

## Example

```python
from cobo_waas2.models.travel_rule_withdraw_exchanges_or_vasp import TravelRuleWithdrawExchangesOrVASP

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleWithdrawExchangesOrVASP from a JSON string
travel_rule_withdraw_exchanges_or_vasp_instance = TravelRuleWithdrawExchangesOrVASP.from_json(json)
# print the JSON string representation of the object
print(TravelRuleWithdrawExchangesOrVASP.to_json())

# convert the object into a dict
travel_rule_withdraw_exchanges_or_vasp_dict = travel_rule_withdraw_exchanges_or_vasp_instance.to_dict()
# create an instance of TravelRuleWithdrawExchangesOrVASP from a dict
travel_rule_withdraw_exchanges_or_vasp_from_dict = TravelRuleWithdrawExchangesOrVASP.from_dict(travel_rule_withdraw_exchanges_or_vasp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


