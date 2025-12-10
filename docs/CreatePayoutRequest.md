# CreatePayoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a settlement request. The request ID is provided by you and must be unique. | 
**payout_channel** | [**PayoutChannel**](PayoutChannel.md) |  | 
**source_type** | [**PaymentSourceType**](PaymentSourceType.md) |  | 
**payout_params** | [**List[PaymentPayoutParam]**](PaymentPayoutParam.md) |  | 
**bank_account_id** | **str** | ｜ Only used in OffRamp payout channel. The ID of the bank account where the settled funds will be deposited. | [optional] 
**currency** | **str** | The fiat currency for the create payouts. | [optional] 
**remark** | **str** | The remark for the create payouts. | [optional] 

## Example

```python
from cobo_waas2.models.create_payout_request import CreatePayoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayoutRequest from a JSON string
create_payout_request_instance = CreatePayoutRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePayoutRequest.to_json())

# convert the object into a dict
create_payout_request_dict = create_payout_request_instance.to_dict()
# create an instance of CreatePayoutRequest from a dict
create_payout_request_from_dict = CreatePayoutRequest.from_dict(create_payout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


