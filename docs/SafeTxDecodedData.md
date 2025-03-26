# SafeTxDecodedData

The information about the decoded data of the transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Name of the decoded method | [optional] 
**parameters** | [**List[SafeTxDecodedDataParameters]**](SafeTxDecodedDataParameters.md) | List of method parameters | [optional] 

## Example

```python
from cobo_waas2.models.safe_tx_decoded_data import SafeTxDecodedData

# TODO update the JSON string below
json = "{}"
# create an instance of SafeTxDecodedData from a JSON string
safe_tx_decoded_data_instance = SafeTxDecodedData.from_json(json)
# print the JSON string representation of the object
print(SafeTxDecodedData.to_json())

# convert the object into a dict
safe_tx_decoded_data_dict = safe_tx_decoded_data_instance.to_dict()
# create an instance of SafeTxDecodedData from a dict
safe_tx_decoded_data_from_dict = SafeTxDecodedData.from_dict(safe_tx_decoded_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


