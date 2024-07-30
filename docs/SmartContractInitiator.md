# SmartContractInitiator

The information about the initiator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The initiator&#39;s wallet ID. | 
**address** | **str** | The initiator&#39;s wallet address.  | 

## Example

```python
from cobo_waas2.models.smart_contract_initiator import SmartContractInitiator

# TODO update the JSON string below
json = "{}"
# create an instance of SmartContractInitiator from a JSON string
smart_contract_initiator_instance = SmartContractInitiator.from_json(json)
# print the JSON string representation of the object
print(SmartContractInitiator.to_json())

# convert the object into a dict
smart_contract_initiator_dict = smart_contract_initiator_instance.to_dict()
# create an instance of SmartContractInitiator from a dict
smart_contract_initiator_from_dict = SmartContractInitiator.from_dict(smart_contract_initiator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


