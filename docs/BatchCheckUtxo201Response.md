# BatchCheckUtxo201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UTXO]**](UTXO.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.batch_check_utxo201_response import BatchCheckUtxo201Response

# TODO update the JSON string below
json = "{}"
# create an instance of BatchCheckUtxo201Response from a JSON string
batch_check_utxo201_response_instance = BatchCheckUtxo201Response.from_json(json)
# print the JSON string representation of the object
print(BatchCheckUtxo201Response.to_json())

# convert the object into a dict
batch_check_utxo201_response_dict = batch_check_utxo201_response_instance.to_dict()
# create an instance of BatchCheckUtxo201Response from a dict
batch_check_utxo201_response_from_dict = BatchCheckUtxo201Response.from_dict(batch_check_utxo201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


