# TokenizationUnarchiveTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_initiator** | **str** | The initiator of the tokenization activity. If you do not specify this property, the WaaS service will automatically designate the API key as the initiator. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_unarchive_token_request import TokenizationUnarchiveTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationUnarchiveTokenRequest from a JSON string
tokenization_unarchive_token_request_instance = TokenizationUnarchiveTokenRequest.from_json(json)
# print the JSON string representation of the object
print(TokenizationUnarchiveTokenRequest.to_json())

# convert the object into a dict
tokenization_unarchive_token_request_dict = tokenization_unarchive_token_request_instance.to_dict()
# create an instance of TokenizationUnarchiveTokenRequest from a dict
tokenization_unarchive_token_request_from_dict = TokenizationUnarchiveTokenRequest.from_dict(tokenization_unarchive_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


