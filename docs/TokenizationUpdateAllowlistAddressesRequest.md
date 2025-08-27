# TokenizationUpdateAllowlistAddressesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TokenizationUpdateAddressAction**](TokenizationUpdateAddressAction.md) |  | 
**source** | [**TokenizationTokenOperationSource**](TokenizationTokenOperationSource.md) |  | 
**addresses** | [**List[TokenizationUpdateAllowlistAddressesParamsAddressesInner]**](TokenizationUpdateAllowlistAddressesParamsAddressesInner.md) | A list of addresses to manage. For &#39;add&#39; operations, notes can be provided. For &#39;remove&#39; operations, notes are ignored. | 
**app_initiator** | **str** | The initiator of the tokenization activity. If you do not specify this property, the WaaS service will automatically designate the API key as the initiator. | [optional] 
**fee** | [**TransactionRequestFee**](TransactionRequestFee.md) |  | 
**request_id** | **str** | The request ID that is used to track a transaction request. The request ID is provided by you and must be unique within your organization. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_update_allowlist_addresses_request import TokenizationUpdateAllowlistAddressesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationUpdateAllowlistAddressesRequest from a JSON string
tokenization_update_allowlist_addresses_request_instance = TokenizationUpdateAllowlistAddressesRequest.from_json(json)
# print the JSON string representation of the object
print(TokenizationUpdateAllowlistAddressesRequest.to_json())

# convert the object into a dict
tokenization_update_allowlist_addresses_request_dict = tokenization_update_allowlist_addresses_request_instance.to_dict()
# create an instance of TokenizationUpdateAllowlistAddressesRequest from a dict
tokenization_update_allowlist_addresses_request_from_dict = TokenizationUpdateAllowlistAddressesRequest.from_dict(tokenization_update_allowlist_addresses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


