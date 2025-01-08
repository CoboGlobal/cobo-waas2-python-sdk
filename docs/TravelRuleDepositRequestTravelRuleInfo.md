# TravelRuleDepositRequestTravelRuleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_wallet_type** | [**DestinationWalletType**](DestinationWalletType.md) |  | 
**vendor_code** | **str** | The vendor code for exchanges or VASPs. | 
**vendor_vasp_id** | **str** | The unique identifier of the VASP. | 
**vendor_vasp_name** | **str** | The vendor name to be provided when selecting \&quot;Others\&quot; as the VASP case. This field allows customers to specify the name of a vendor not listed. | [optional] 
**entity_info** | [**TravelRuleDepositExchangesOrVASPEntityInfo**](TravelRuleDepositExchangesOrVASPEntityInfo.md) |  | 
**self_custody_wallet_challenge** | **str** | The challenge obtained from a previous operation. | 
**self_custody_wallet_address** | **str** | The address of the self-custodial wallet. | 
**self_custody_wallet_sign** | **str** | The signed message from the self-custodial wallet. | 

## Example

```python
from cobo_waas2.models.travel_rule_deposit_request_travel_rule_info import TravelRuleDepositRequestTravelRuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleDepositRequestTravelRuleInfo from a JSON string
travel_rule_deposit_request_travel_rule_info_instance = TravelRuleDepositRequestTravelRuleInfo.from_json(json)
# print the JSON string representation of the object
print(TravelRuleDepositRequestTravelRuleInfo.to_json())

# convert the object into a dict
travel_rule_deposit_request_travel_rule_info_dict = travel_rule_deposit_request_travel_rule_info_instance.to_dict()
# create an instance of TravelRuleDepositRequestTravelRuleInfo from a dict
travel_rule_deposit_request_travel_rule_info_from_dict = TravelRuleDepositRequestTravelRuleInfo.from_dict(travel_rule_deposit_request_travel_rule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


