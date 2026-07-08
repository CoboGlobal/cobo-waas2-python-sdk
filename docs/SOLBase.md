# SOLBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee** | **str** | A fixed fee charged per signature. The default is 5,000 lamports per signature. | [optional] 
**rent_amount** | **str** | The one-time rent required to activate a Solana token Associated Token Account (ATA) before the token can be received or used. **This field is reserved for future use and is currently not populated.** | [optional] 

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


