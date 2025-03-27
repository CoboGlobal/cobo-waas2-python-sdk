# SafeTxExtraData

The information used to construct and sign Safe{Wallet} transactions using the EIP-712 standard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The recipient address of the transaction. | 
**value** | **str** | The human-readable transaction value, for example, &#x60;1 ETH&#x60;. | 
**data** | **str** | The transaction call data. | 
**domain_hash** | **str** | The EIP-712 domain separator hash. | 
**message_hash** | **str** | The hash of the structured message to be signed. | 
**safe_address** | **str** | The address of the Safe contract. | 
**safe_tx_hash** | **str** | The hash of the transaction. | 
**safe_nonce** | **int** | The nonce of the transaction. | 
**operation** | **str** | The operation type for the transaction. | 
**gas_token_addr** | **str** | The address of the token used to pay gas. | [optional] 
**safe_tx_gas** | **int** | The gas limit used for the transaction. | [optional] 
**base_gas** | **int** | The base gas for the transaction. | [optional] 
**gas_price** | **str** | The gas price used in the transaction. | [optional] 
**refund_receiver** | **str** | The address used to receive the gas refund. | [optional] 
**to_contract_name** | **str** | The name of the recipient contract (if available). | [optional] 
**decoded_data** | [**SafeTxDecodedData**](SafeTxDecodedData.md) |  | [optional] 
**signature** | **str** | The signature of the transaction (if signed by Cobo Signer). | [optional] 
**wei** | **str** | The transaction amount in Wei. | [optional] 

## Example

```python
from cobo_waas2.models.safe_tx_extra_data import SafeTxExtraData

# TODO update the JSON string below
json = "{}"
# create an instance of SafeTxExtraData from a JSON string
safe_tx_extra_data_instance = SafeTxExtraData.from_json(json)
# print the JSON string representation of the object
print(SafeTxExtraData.to_json())

# convert the object into a dict
safe_tx_extra_data_dict = safe_tx_extra_data_instance.to_dict()
# create an instance of SafeTxExtraData from a dict
safe_tx_extra_data_from_dict = SafeTxExtraData.from_dict(safe_tx_extra_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


