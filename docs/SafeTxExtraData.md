# SafeTxExtraData

The information about the extra data of the Safe{Wallet} tx message transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The recipient address of the transaction | 
**value** | **str** | Readable transaction value (e.g., 1 ETH) | 
**data** | **str** | The transaction data | 
**domain_hash** | **str** | EIP712 structured data domain hash | 
**message_hash** | **str** | Hash of the structured message | 
**safe_address** | **str** | Address of the Safe contract | 
**safe_tx_hash** | **str** | Hash of the Safe transaction | 
**safe_nonce** | **int** | Safe transaction nonce | 
**operation** | **str** | Type of operation performed in the transaction | 
**gas_token_addr** | **str** | Address of the gas token | [optional] 
**safe_tx_gas** | **int** | Gas used for the Safe transaction | [optional] 
**base_gas** | **int** | Base gas for the transaction | [optional] 
**gas_price** | **str** | Gas price used in the transaction | [optional] 
**refund_receiver** | **str** | Address to receive the gas refund | [optional] 
**to_contract_name** | **str** | Name of the recipient contract (if available) | [optional] 
**decoded_data** | [**SafeTxDecodedData**](SafeTxDecodedData.md) |  | [optional] 
**signature** | **str** | Signature of the transaction (if signed by Cobo Signer) | [optional] 
**wei** | **str** | Transaction amount in Wei | [optional] 

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


