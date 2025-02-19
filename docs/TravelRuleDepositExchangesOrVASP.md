# TravelRuleDepositExchangesOrVASP

Required information when depositing from an exchange or other virtual asset service providers (VASP).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_wallet_type** | [**DestinationWalletType**](DestinationWalletType.md) |  | 
**vendor_code** | **str** | The vendor code of the VASP. | 
**vendor_vasp_id** | **str** | The unique identifier of the VASP. | 
**vendor_vasp_name** | **str** | The vendor name. Use this field to specify the name of a vendor not listed. | [optional] 
**entity_info** | [**TravelRuleDepositExchangesOrVASPEntityInfo**](TravelRuleDepositExchangesOrVASPEntityInfo.md) |  | 

## Example

```python
from cobo_waas2.models.travel_rule_deposit_exchanges_or_vasp import TravelRuleDepositExchangesOrVASP

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleDepositExchangesOrVASP from a JSON string
travel_rule_deposit_exchanges_or_vasp_instance = TravelRuleDepositExchangesOrVASP.from_json(json)
# print the JSON string representation of the object
print(TravelRuleDepositExchangesOrVASP.to_json())

# convert the object into a dict
travel_rule_deposit_exchanges_or_vasp_dict = travel_rule_deposit_exchanges_or_vasp_instance.to_dict()
# create an instance of TravelRuleDepositExchangesOrVASP from a dict
travel_rule_deposit_exchanges_or_vasp_from_dict = TravelRuleDepositExchangesOrVASP.from_dict(travel_rule_deposit_exchanges_or_vasp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


