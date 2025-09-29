# SwapReceivingTransaction

Receiving transaction information for the swap activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | 
**transaction_hash** | **str** | The transaction hash. | [optional] 
**is_loop** | **bool** | Whether the transaction was executed as a [Cobo Loop](https://manuals.cobo.com/en/portal/custodial-wallets/cobo-loop) transfer. - &#x60;true&#x60;: The transaction was executed as a Cobo Loop transfer. - &#x60;false&#x60;: The transaction was not executed as a Cobo Loop transfer.  | [optional] 

## Example

```python
from cobo_waas2.models.swap_receiving_transaction import SwapReceivingTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of SwapReceivingTransaction from a JSON string
swap_receiving_transaction_instance = SwapReceivingTransaction.from_json(json)
# print the JSON string representation of the object
print(SwapReceivingTransaction.to_json())

# convert the object into a dict
swap_receiving_transaction_dict = swap_receiving_transaction_instance.to_dict()
# create an instance of SwapReceivingTransaction from a dict
swap_receiving_transaction_from_dict = SwapReceivingTransaction.from_dict(swap_receiving_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


