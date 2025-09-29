# TokenizationTokenDetailInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The unique token identifier. | 
**chain_id** | **str** | The chain ID of the tokenization contract. | 
**token_address** | **str** | The address of the token contract. | [optional] 
**token_name** | **str** | The name of the token. | [optional] 
**token_symbol** | **str** | The unique token symbol. | 
**token_standard** | [**TokenizationTokenStandard**](TokenizationTokenStandard.md) |  | 
**decimals** | **int** | The number of decimals of the token. | 
**token_access_activated** | **bool** | Whether the allowlist feature is activated for the token. | [optional] 
**status** | [**TokenizationStatus**](TokenizationStatus.md) |  | 
**total_supply** | **str** | The total supply of the token. | [optional] 
**holdings** | **str** | The amount of tokens held by the organization. | [optional] 
**permissions** | [**List[TokenizationAddressPermission]**](TokenizationAddressPermission.md) | List of execution addresses and their permissions. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_token_detail_info import TokenizationTokenDetailInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationTokenDetailInfo from a JSON string
tokenization_token_detail_info_instance = TokenizationTokenDetailInfo.from_json(json)
# print the JSON string representation of the object
print(TokenizationTokenDetailInfo.to_json())

# convert the object into a dict
tokenization_token_detail_info_dict = tokenization_token_detail_info_instance.to_dict()
# create an instance of TokenizationTokenDetailInfo from a dict
tokenization_token_detail_info_from_dict = TokenizationTokenDetailInfo.from_dict(tokenization_token_detail_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


