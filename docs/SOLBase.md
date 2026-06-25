# SOLBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee** | **str** | A fixed fee charged per signature. The default is 5,000 lamports per signature. | [optional] 
**rent_amount** | **str** | The one-time rent required to create and initialize a Solana token Associated Token Account (ATA) — a token sub-address that must be activated before the token can be received or used. This rent is paid by the main (source) address. It is populated only when an ATA must be activated for the transaction; otherwise it is null.  | [optional] 

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


