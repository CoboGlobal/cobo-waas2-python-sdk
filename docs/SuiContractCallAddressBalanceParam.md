# SuiContractCallAddressBalanceParam

Parameters related to SUI address balance operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_type** | [**SuiContractCallContractType**](SuiContractCallContractType.md) |  | 
**token_id** | **str** | The token ID, which is the unique identifier of a token. | 
**operation_type** | [**SuiContractCallAddressBalanceOperationType**](SuiContractCallAddressBalanceOperationType.md) |  | 
**txid** | **str** | The transaction hash of the deposit to return. Required when &#x60;operation_type&#x60; is &#x60;AddressBalanceRefund&#x60;, and must be omitted otherwise. The destination address is resolved from this deposit and cannot be specified.  | [optional] 

## Example

```python
from cobo_waas2.models.sui_contract_call_address_balance_param import SuiContractCallAddressBalanceParam

# TODO update the JSON string below
json = "{}"
# create an instance of SuiContractCallAddressBalanceParam from a JSON string
sui_contract_call_address_balance_param_instance = SuiContractCallAddressBalanceParam.from_json(json)
# print the JSON string representation of the object
print(SuiContractCallAddressBalanceParam.to_json())

# convert the object into a dict
sui_contract_call_address_balance_param_dict = sui_contract_call_address_balance_param_instance.to_dict()
# create an instance of SuiContractCallAddressBalanceParam from a dict
sui_contract_call_address_balance_param_from_dict = SuiContractCallAddressBalanceParam.from_dict(sui_contract_call_address_balance_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


