# CreatePayoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a payout request. The request ID is provided by you and must be unique. | 
**payout_channel** | [**PayoutChannel**](PayoutChannel.md) |  | 
**payout_params** | [**List[PaymentPayoutParam]**](PaymentPayoutParam.md) |  | 
**bank_account_id** | **str** | The ID of the bank account where the funds will be deposited. Specify this field when &#x60;payout_channel&#x60; is set to &#x60;OffRamp&#x60;.  You can call [List all bank accounts](https://www.cobo.com/payments/en/api-references/payment/list-all-bank-accounts) to retrieve the IDs of registered bank accounts. To add a new bank account, refer to [Destinations](https://www.cobo.com/payments/en/guides/destinations).  | [optional] 
**currency** | **str** | The fiat currency you will receive from the payout. - Required when &#x60;payout_channel&#x60; is set to &#x60;OffRamp&#x60;. - Currently, only &#x60;USD&#x60; is supported.  | [optional] 
**remark** | **str** | The remark for the payout. | [optional] 

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


