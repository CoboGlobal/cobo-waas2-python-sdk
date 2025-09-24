# TokenizationActivityInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | The ID of the activity. | 
**token_id** | **str** | The token ID. | 
**type** | [**TokenizationOperationType**](TokenizationOperationType.md) |  | 
**status** | [**TokenizationActivityStatus**](TokenizationActivityStatus.md) |  | 
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**initiator** | **str** | The initiator of the activity. | 
**initiator_type** | [**TransactionInitiatorType**](TransactionInitiatorType.md) |  | 
**transaction_ids** | **List[str]** | The IDs of the corresponding transactions of the activity. | 
**created_timestamp** | **int** | The creation timestamp of the activity in milliseconds since the Unix epoch. | 
**updated_timestamp** | **int** | The last update timestamp of the activity in milliseconds since the Unix epoch. | 

## Example

```python
from cobo_waas2.models.tokenization_activity_info import TokenizationActivityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationActivityInfo from a JSON string
tokenization_activity_info_instance = TokenizationActivityInfo.from_json(json)
# print the JSON string representation of the object
print(TokenizationActivityInfo.to_json())

# convert the object into a dict
tokenization_activity_info_dict = tokenization_activity_info_instance.to_dict()
# create an instance of TokenizationActivityInfo from a dict
tokenization_activity_info_from_dict = TokenizationActivityInfo.from_dict(tokenization_activity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


