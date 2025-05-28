# BatchUTXOParam

The UTXO information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_hash** | **str** | The transaction hash. | 
**vout_ns** | **List[int]** |  | [optional] 

## Example

```python
from cobo_waas2.models.batch_utxo_param import BatchUTXOParam

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUTXOParam from a JSON string
batch_utxo_param_instance = BatchUTXOParam.from_json(json)
# print the JSON string representation of the object
print(BatchUTXOParam.to_json())

# convert the object into a dict
batch_utxo_param_dict = batch_utxo_param_instance.to_dict()
# create an instance of BatchUTXOParam from a dict
batch_utxo_param_from_dict = BatchUTXOParam.from_dict(batch_utxo_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


