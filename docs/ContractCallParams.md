# ContractCallParams

The information about a transaction that interacts with a smart contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | A client-defined unique request identifier (idempotency key) used to prevent duplicate contract call requests. It must be unique within the same organization. Requests with the same request ID will be rejected with an error. | 
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | 
**source** | [**ContractCallSource**](ContractCallSource.md) |  | 
**destination** | [**ContractCallDestination**](ContractCallDestination.md) |  | 
**description** | **str** | The description of the contract call transaction. Maximum length is 2048 characters for MPC Wallets and Custodial Wallets (Web3 Wallets), and 1000 characters for Custodial Wallets (Asset Wallets). | [optional] 
**category_names** | **List[str]** | The custom category for you to identify your transactions. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | [optional] 
**transaction_process_type** | [**TransactionProcessType**](TransactionProcessType.md) |  | [optional] 
**auto_fuel** | [**AutoFuelType**](AutoFuelType.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.contract_call_params import ContractCallParams

# TODO update the JSON string below
json = "{}"
# create an instance of ContractCallParams from a JSON string
contract_call_params_instance = ContractCallParams.from_json(json)
# print the JSON string representation of the object
print(ContractCallParams.to_json())

# convert the object into a dict
contract_call_params_dict = contract_call_params_instance.to_dict()
# create an instance of ContractCallParams from a dict
contract_call_params_from_dict = ContractCallParams.from_dict(contract_call_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


