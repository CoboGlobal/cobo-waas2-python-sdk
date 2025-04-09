# SettlementDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency for the settlement. | [optional] 
**token_id** | **str** | The ID of the cryptocurrency token settled. | [optional] 
**chain_id** | **str** | The ID of the blockchain network on which the settlement occurred. | [optional] 
**amount** | **str** | The settled amount. - If &#x60;token_id&#x60; is specified, this represents the settlement amount in the specified cryptocurrency token. - If &#x60;token_id&#x60; is not specified, this represents the settlement amount in the specified currency.  | [optional] 
**status** | [**SettleStatus**](SettleStatus.md) |  | [optional] 
**bank_account** | [**BankAccount**](BankAccount.md) |  | [optional] 
**transactions** | [**List[PaymentTransaction]**](PaymentTransaction.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.settlement_detail import SettlementDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementDetail from a JSON string
settlement_detail_instance = SettlementDetail.from_json(json)
# print the JSON string representation of the object
print(SettlementDetail.to_json())

# convert the object into a dict
settlement_detail_dict = settlement_detail_instance.to_dict()
# create an instance of SettlementDetail from a dict
settlement_detail_from_dict = SettlementDetail.from_dict(settlement_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


