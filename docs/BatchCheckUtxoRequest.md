# BatchCheckUtxoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
**utxos** | [**List[BatchUTXOParam]**](BatchUTXOParam.md) |  | 

## Example

```python
from cobo_waas2.models.batch_check_utxo_request import BatchCheckUtxoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCheckUtxoRequest from a JSON string
batch_check_utxo_request_instance = BatchCheckUtxoRequest.from_json(json)
# print the JSON string representation of the object
print(BatchCheckUtxoRequest.to_json())

# convert the object into a dict
batch_check_utxo_request_dict = batch_check_utxo_request_instance.to_dict()
# create an instance of BatchCheckUtxoRequest from a dict
batch_check_utxo_request_from_dict = BatchCheckUtxoRequest.from_dict(batch_check_utxo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


