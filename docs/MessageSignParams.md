# MessageSignParams

The information about a transaction that signs a message. You can provide the message either as raw data or as structured data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | 
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](/v2/api-references/wallets/list-enabled-chains). | 
**source** | [**MessageSignSource**](MessageSignSource.md) |  | 
**destination** | [**MessageSignDestination**](MessageSignDestination.md) |  | 
**description** | **str** | The description of the message sign transaction. | [optional] 
**category_names** | **List[str]** | The custom category for you to identify your transactions. | [optional] 

## Example

```python
from cobo_waas2.models.message_sign_params import MessageSignParams

# TODO update the JSON string below
json = "{}"
# create an instance of MessageSignParams from a JSON string
message_sign_params_instance = MessageSignParams.from_json(json)
# print the JSON string representation of the object
print(MessageSignParams.to_json())

# convert the object into a dict
message_sign_params_dict = message_sign_params_instance.to_dict()
# create an instance of MessageSignParams from a dict
message_sign_params_from_dict = MessageSignParams.from_dict(message_sign_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


