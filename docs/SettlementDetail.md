# SettlementDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The fiat currency for the settlement. | [optional] 
**token_id** | **str** | The ID of the cryptocurrency settled. | [optional] 
**chain_id** | **str** | The ID of the blockchain network on which the settlement occurred. | [optional] 
**merchant_id** | **str** | The ID of the merchant associated with this settlement. | [optional] 
**amount** | **str** | The settlement amount. - If &#x60;payout_channel&#x60; is set to &#x60;Crypto&#x60;, this represents the settlement amount in the specified cryptocurrency. - If &#x60;payout_channel&#x60; is set to &#x60;OffRamp&#x60;, this represents the settlement amount in the specified fiat currency.  | [optional] 
**settled_amount** | **str** | The settled amount of this settlement detail.  - If &#x60;payout_channel&#x60; is set to &#x60;Crypto&#x60;, this represents the actual settled amount in the specified cryptocurrency.  - If &#x60;payout_channel&#x60; is set to &#x60;OffRamp&#x60;, this represents the actual settled amount in the specified fiat currency.  | [optional] 
**status** | [**SettleStatus**](SettleStatus.md) |  | [optional] 
**bank_account** | [**BankAccount**](BankAccount.md) |  | [optional] 
**transactions** | [**List[PaymentTransaction]**](PaymentTransaction.md) | An array of transactions associated with this settlement request. Each transaction represents a separate blockchain operation related to the settlement process. | [optional] 
**created_timestamp** | **int** | The creation time of the settlement, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The last update time of the settlement, represented as a UNIX timestamp in seconds. | [optional] 
**crypto_address_id** | **str** | The ID of the crypto address used for crypto withdrawal. | [optional] 
**payout_channel** | [**PayoutChannel**](PayoutChannel.md) |  | [optional] 
**acquiring_type** | [**AcquiringType**](AcquiringType.md) |  | [optional] 

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


