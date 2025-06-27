# TokenizationHoldingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The unique identifier of the wallet holding the token. | 
**wallet_name** | **str** | The name of the wallet. | [optional] 
**address** | **str** | The address holding the token. | 
**balance** | **str** | The token balance held by this address. | 
**address_label** | **str** | The label of the address. | [optional] 

## Example

```python
from cobo_waas2.models.tokenization_holding_info import TokenizationHoldingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TokenizationHoldingInfo from a JSON string
tokenization_holding_info_instance = TokenizationHoldingInfo.from_json(json)
# print the JSON string representation of the object
print(TokenizationHoldingInfo.to_json())

# convert the object into a dict
tokenization_holding_info_dict = tokenization_holding_info_instance.to_dict()
# create an instance of TokenizationHoldingInfo from a dict
tokenization_holding_info_from_dict = TokenizationHoldingInfo.from_dict(tokenization_holding_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


