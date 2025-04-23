# ListTokenBalancesForFeeStation200ResponseDataInner

The balance information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-tokens). | 
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
**balance** | [**Balance**](Balance.md) |  | 

## Example

```python
from cobo_waas2.models.list_token_balances_for_fee_station200_response_data_inner import ListTokenBalancesForFeeStation200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTokenBalancesForFeeStation200ResponseDataInner from a JSON string
list_token_balances_for_fee_station200_response_data_inner_instance = ListTokenBalancesForFeeStation200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ListTokenBalancesForFeeStation200ResponseDataInner.to_json())

# convert the object into a dict
list_token_balances_for_fee_station200_response_data_inner_dict = list_token_balances_for_fee_station200_response_data_inner_instance.to_dict()
# create an instance of ListTokenBalancesForFeeStation200ResponseDataInner from a dict
list_token_balances_for_fee_station200_response_data_inner_from_dict = ListTokenBalancesForFeeStation200ResponseDataInner.from_dict(list_token_balances_for_fee_station200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


