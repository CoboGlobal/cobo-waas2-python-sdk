# SOLBase

The transaction base fee based on the SOL fee model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee** | **str** | The fundamental fee required for each transaction. It is charged to prevent spam transactions and network congestion, ensuring that only meaningful transactions consume network resources. | [optional] 
**rent_amount** | **str** | The fee charged as rent for maintaining the state of accounts on the blockchain. This rent ensures accounts are stored on-chain over the long term and that there&#39;s sufficient balance to sustain the account state. | [optional] 

## Example

```python
from cobo_waas2.models.sol_base import SOLBase

# TODO update the JSON string below
json = "{}"
# create an instance of SOLBase from a JSON string
sol_base_instance = SOLBase.from_json(json)
# print the JSON string representation of the object
print(SOLBase.to_json())

# convert the object into a dict
sol_base_dict = sol_base_instance.to_dict()
# create an instance of SOLBase from a dict
sol_base_from_dict = SOLBase.from_dict(sol_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


