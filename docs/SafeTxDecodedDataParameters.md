# SafeTxDecodedDataParameters

The information about the decoded parameters of the transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the parameter. | [optional] 
**type** | **str** | The data type of the parameter. | [optional] 
**value** | **str** | The value of the parameter. | [optional] 
**value_decoded** | [**List[SafeTxSubTransaction]**](SafeTxSubTransaction.md) | The decoded value of the parameter (if applicable). | [optional] 

## Example

```python
from cobo_waas2.models.safe_tx_decoded_data_parameters import SafeTxDecodedDataParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SafeTxDecodedDataParameters from a JSON string
safe_tx_decoded_data_parameters_instance = SafeTxDecodedDataParameters.from_json(json)
# print the JSON string representation of the object
print(SafeTxDecodedDataParameters.to_json())

# convert the object into a dict
safe_tx_decoded_data_parameters_dict = safe_tx_decoded_data_parameters_instance.to_dict()
# create an instance of SafeTxDecodedDataParameters from a dict
safe_tx_decoded_data_parameters_from_dict = SafeTxDecodedDataParameters.from_dict(safe_tx_decoded_data_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


