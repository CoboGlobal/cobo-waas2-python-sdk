# CreateSettlementRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a settlement request. The request ID is provided by you and must be unique. | 
**acquiring_type** | [**AcquiringType**](AcquiringType.md) |  | [optional] 
**payout_channel** | [**PayoutChannel**](PayoutChannel.md) |  | [optional] 
**settlement_type** | [**SettlementType**](SettlementType.md) |  | [optional] 
**settlements** | [**List[CreateSettlement]**](CreateSettlement.md) |  | 
**bank_account_id** | **str** | ｜ Only used in OffRamp payout channel. The ID of the bank account where the settled funds will be deposited. | [optional] 
**currency** | **str** | The fiat currency for the settlement request. | [optional] 
**remark** | **str** | The remark for the settlement request. | [optional] 

## Example

```python
from cobo_waas2.models.create_settlement_request_request import CreateSettlementRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSettlementRequestRequest from a JSON string
create_settlement_request_request_instance = CreateSettlementRequestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSettlementRequestRequest.to_json())

# convert the object into a dict
create_settlement_request_request_dict = create_settlement_request_request_instance.to_dict()
# create an instance of CreateSettlementRequestRequest from a dict
create_settlement_request_request_from_dict = CreateSettlementRequestRequest.from_dict(create_settlement_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


