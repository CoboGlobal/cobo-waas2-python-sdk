# EstimateContractCallFeeParams

The information about a transaction that interacts with a smart contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a transaction request. | [optional] 
**request_type** | [**EstimateFeeRequestType**](EstimateFeeRequestType.md) |  | 
**chain_id** | **str** | The chain ID of the chain on which the smart contract is issued. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | 
**source** | [**ContractCallSource**](ContractCallSource.md) |  | 
**destination** | [**ContractCallDestination**](ContractCallDestination.md) |  | [optional] 
**fee_type** | [**FeeType**](FeeType.md) |  | [optional] 
**replaced_transaction_id** | **str** | The ID of the transaction that this transaction replaced. | [optional] 

## Example

```python
from cobo_waas2.models.estimate_contract_call_fee_params import EstimateContractCallFeeParams

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateContractCallFeeParams from a JSON string
estimate_contract_call_fee_params_instance = EstimateContractCallFeeParams.from_json(json)
# print the JSON string representation of the object
print(EstimateContractCallFeeParams.to_json())

# convert the object into a dict
estimate_contract_call_fee_params_dict = estimate_contract_call_fee_params_instance.to_dict()
# create an instance of EstimateContractCallFeeParams from a dict
estimate_contract_call_fee_params_from_dict = EstimateContractCallFeeParams.from_dict(estimate_contract_call_fee_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


