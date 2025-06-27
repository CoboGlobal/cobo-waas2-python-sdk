# TokenizationAllowlistActivationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**activation** | **bool** | Whether to activate the allowlist feature for the token. | 
**app_initiator** | **str** | The initiator of the tokenization activity. If you do not specify this property, the WaaS service will automatically designate the API key as the initiator. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 

## Example

```python
from cobo_waas2.models.tokenization_allowlist_activation_request import TokenizationAllowlistActivationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationAllowlistActivationRequest from a JSON string
tokenization_allowlist_activation_request_instance = TokenizationAllowlistActivationRequest.from_json(json)
# print the JSON string representation of the object
print(TokenizationAllowlistActivationRequest.to_json())

# convert the object into a dict
tokenization_allowlist_activation_request_dict = tokenization_allowlist_activation_request_instance.to_dict()
# create an instance of TokenizationAllowlistActivationRequest from a dict
tokenization_allowlist_activation_request_from_dict = TokenizationAllowlistActivationRequest.from_dict(tokenization_allowlist_activation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


