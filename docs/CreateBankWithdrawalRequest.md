# CreateBankWithdrawalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a bank withdrawal request. The request ID is provided by you and must be unique. | 
**source_bank_account_id** | **str** | The source bank account ID. The destination bank account must be tagged as &#x60;VA&#x60;. Cobo uses the mapped VA account to initiate the withdrawal.  | 
**target_bank_account_id** | **str** | The target bank account ID that receives the bank withdrawal. | 
**currency** | **str** | The fiat currency of the bank withdrawal. | 
**amount** | **str** | The bank withdrawal amount. | 
**remark** | **str** | The remark for the bank withdrawal. | [optional] 

## Example

```python
from cobo_waas2.models.create_bank_withdrawal_request import CreateBankWithdrawalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBankWithdrawalRequest from a JSON string
create_bank_withdrawal_request_instance = CreateBankWithdrawalRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBankWithdrawalRequest.to_json())

# convert the object into a dict
create_bank_withdrawal_request_dict = create_bank_withdrawal_request_instance.to_dict()
# create an instance of CreateBankWithdrawalRequest from a dict
create_bank_withdrawal_request_from_dict = CreateBankWithdrawalRequest.from_dict(create_bank_withdrawal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


