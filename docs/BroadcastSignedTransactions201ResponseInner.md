# BroadcastSignedTransactions201ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a transaction request. | 
**transaction_id** | **str** | The transaction ID of this broadcast transaction. | 

## Example

```python
from cobo_waas2.models.broadcast_signed_transactions201_response_inner import BroadcastSignedTransactions201ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of BroadcastSignedTransactions201ResponseInner from a JSON string
broadcast_signed_transactions201_response_inner_instance = BroadcastSignedTransactions201ResponseInner.from_json(json)
# print the JSON string representation of the object
print(BroadcastSignedTransactions201ResponseInner.to_json())

# convert the object into a dict
broadcast_signed_transactions201_response_inner_dict = broadcast_signed_transactions201_response_inner_instance.to_dict()
# create an instance of BroadcastSignedTransactions201ResponseInner from a dict
broadcast_signed_transactions201_response_inner_from_dict = BroadcastSignedTransactions201ResponseInner.from_dict(broadcast_signed_transactions201_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


