# CreatePayoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a payout request. The request ID is provided by you and must be unique. | 
**source_account** | **str** | The source account from which the payout will be made. - If the source account is a merchant account, provide the merchant&#39;s ID (e.g., \&quot;M1001\&quot;). - If the source account is the developer account, use the string &#x60;\&quot;developer\&quot;&#x60;.  | 
**payout_channel** | [**PayoutChannel**](PayoutChannel.md) |  | 
**payout_params** | [**List[PaymentPayoutParam]**](PaymentPayoutParam.md) |  | 
**recipient_info** | [**PaymentPayoutRecipientInfo**](PaymentPayoutRecipientInfo.md) |  | 
**remark** | **str** | An optional note or comment about the payout for your internal reference. | [optional] 

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


