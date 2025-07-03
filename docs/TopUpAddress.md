# TopUpAddress

The details of a top-up address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The dedicated top-up address assigned to a specific payer under a merchant on a specified chain. | 
**payer_id** | **str** | A unique identifier assigned by Cobo to track and identify individual payers. | 
**custom_payer_id** | **str** | A unique identifier assigned by the developer to track and identify individual payers in their system. | 
**merchant_id** | **str** | The merchant ID. | 
**token_id** | **str** | The token ID, which is a unique identifier that specifies both the blockchain network and cryptocurrency token in the format &#x60;{CHAIN}_{TOKEN}&#x60;. | 
**chain** | **str** | The chain ID. | [optional] 
**developer_fee_rate** | **str** | The developer fee rate applied to top-up transactions made to this address. Expressed as a decimal string where \&quot;0.1\&quot; represents 10%. | [optional] 
**min_amount** | **str** | The minimum top-up amount allowed for this address. Top-ups below this threshold will not be credited to merchant funds, but to developer funds instead. | 
**created_timestamp** | **int** | The creation time of the top-up address, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The last update time of the top-up address, represented as a UNIX timestamp in seconds. | [optional] 

## Example

```python
from cobo_waas2.models.top_up_address import TopUpAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TopUpAddress from a JSON string
top_up_address_instance = TopUpAddress.from_json(json)
# print the JSON string representation of the object
print(TopUpAddress.to_json())

# convert the object into a dict
top_up_address_dict = top_up_address_instance.to_dict()
# create an instance of TopUpAddress from a dict
top_up_address_from_dict = TopUpAddress.from_dict(top_up_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


