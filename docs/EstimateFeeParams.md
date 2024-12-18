# EstimateFeeParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. It is recommended to use the same request ID as the transaction for which you want to estimate the transaction fee. | [optional] 
**request_type** | [**EstimateFeeRequestType**](EstimateFeeRequestType.md) |  | 
**source** | [**ContractCallSource**](ContractCallSource.md) |  | 
**token_id** | **str** | The token ID of the transferred token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](/v2/api-references/wallets/list-enabled-tokens). | 
**destination** | [**ContractCallDestination**](ContractCallDestination.md) |  | 
**fee_type** | [**FeeType**](FeeType.md) |  | [optional] 
**chain_id** | **str** | The chain ID of the chain on which the smart contract is deployed. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](/v2/api-references/wallets/list-enabled-chains). | 

## Example

```python
from cobo_waas2.models.estimate_fee_params import EstimateFeeParams

# TODO update the JSON string below
json = "{}"
# create an instance of EstimateFeeParams from a JSON string
estimate_fee_params_instance = EstimateFeeParams.from_json(json)
# print the JSON string representation of the object
print(EstimateFeeParams.to_json())

# convert the object into a dict
estimate_fee_params_dict = estimate_fee_params_instance.to_dict()
# create an instance of EstimateFeeParams from a dict
estimate_fee_params_from_dict = EstimateFeeParams.from_dict(estimate_fee_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


