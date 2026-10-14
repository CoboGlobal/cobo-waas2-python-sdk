# SOLBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_fee** | **str** | A fixed fee, in lamports, charged per signature. The default is 5,000 per signature. | [optional] 
**rent_amount** | **str** | The one-time rent, in lamports, required to create the destination&#39;s Associated Token Account (ATA) for this token when it does not exist yet.  In fee estimate responses, this field returns the current on-chain rent if the destination address has no ATA for the token, and is empty otherwise. You can call [Estimate transaction fee](https://www.cobo.com/developers/v2/api-references/transactions/estimate-transaction-fee) before submitting a transaction to check whether it will incur ATA rent. The result reflects the destination at estimation time; if the ATA is closed before the transaction is built, the transaction still creates it and incurs the rent.  In transaction records, this field keeps the value estimated when the transaction was created and is not updated from on-chain data. &#x60;estimated_fee_used&#x60; includes this rent, while &#x60;fee_used&#x60; does not.  | [optional] 

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


