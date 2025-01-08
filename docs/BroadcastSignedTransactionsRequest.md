# BroadcastSignedTransactionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_ids** | **List[str]** | The transaction IDs of the signed transactions to be broadcast. You can retrieve the transactions corresponding to a staking activity by calling [Get staking activity details](https://www.cobo.com/developers/v2/api-references/stakings/get-staking-activity-details). | [optional] 

## Example

```python
from cobo_waas2.models.broadcast_signed_transactions_request import BroadcastSignedTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastSignedTransactionsRequest from a JSON string
broadcast_signed_transactions_request_instance = BroadcastSignedTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print(BroadcastSignedTransactionsRequest.to_json())

# convert the object into a dict
broadcast_signed_transactions_request_dict = broadcast_signed_transactions_request_instance.to_dict()
# create an instance of BroadcastSignedTransactionsRequest from a dict
broadcast_signed_transactions_request_from_dict = BroadcastSignedTransactionsRequest.from_dict(broadcast_signed_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


