# TravelRuleWithdrawRequestTravelRuleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_wallet_type** | [**DestinationWalletType**](DestinationWalletType.md) |  | 
**self_custody_wallet_challenge** | **str** | The message obtained from the &#x60;Retrieve transaction limitations&#x60; operation. This message is used to verify wallet ownership through signing. | 
**self_custody_wallet_address** | **str** | The address of the self-custody wallet. | 
**self_custody_wallet_sign** | **str** | The signature created by signing the challenge message with the wallet&#39;s private key. | 
**vendor_code** | **str** | The vendor code of the exchange or virtual asset service provider (VASP). | 
**vendor_vasp_id** | **str** | The unique identifier of the VASP. | 
**entity_info** | [**TravelRuleWithdrawExchangesOrVASPEntityInfo**](TravelRuleWithdrawExchangesOrVASPEntityInfo.md) |  | 

## Example

```python
from cobo_waas2.models.travel_rule_withdraw_request_travel_rule_info import TravelRuleWithdrawRequestTravelRuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleWithdrawRequestTravelRuleInfo from a JSON string
travel_rule_withdraw_request_travel_rule_info_instance = TravelRuleWithdrawRequestTravelRuleInfo.from_json(json)
# print the JSON string representation of the object
print(TravelRuleWithdrawRequestTravelRuleInfo.to_json())

# convert the object into a dict
travel_rule_withdraw_request_travel_rule_info_dict = travel_rule_withdraw_request_travel_rule_info_instance.to_dict()
# create an instance of TravelRuleWithdrawRequestTravelRuleInfo from a dict
travel_rule_withdraw_request_travel_rule_info_from_dict = TravelRuleWithdrawRequestTravelRuleInfo.from_dict(travel_rule_withdraw_request_travel_rule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


