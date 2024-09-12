# TokenInfo

The token information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | The token ID, which is the unique identifier of a token. You can retrieve the IDs of all the tokens you can use by calling [List enabled tokens](/v2/api-references/wallets/list-enabled-tokens). | 
**chain_id** | **str** | The ID of the chain on which the token operates. | 
**asset_id** | **str** | (This concept applies to Exchange Wallets only) The asset ID. An asset ID is the unique identifier of the asset held within your linked exchange account. | [optional] 
**symbol** | **str** | The token symbol, which is the abbreviated name of a token. | [optional] 
**name** | **str** | The token name, which is the full name of a token. | [optional] 
**decimal** | **int** | The token decimal. | [optional] 
**icon_url** | **str** | The URL of the token icon. | [optional] 
**token_address** | **str** | The token address, if applicable. | [optional] 
**fee_token_id** | **str** | The fee token ID. A fee token is the token with which you pay transaction fees. | [optional] 
**can_deposit** | **bool** | Whether deposits are enabled for this token. | [optional] 
**can_withdraw** | **bool** | Whether withdrawals are enabled for this token. | [optional] 
**dust_threshold** | **str** | The minimum withdrawal amount for Custodial Wallets. If your withdrawal amount is smaller than this threshold, the withdrawal request will receive an error.  Note: [Loop transfers](https://loop.top/) do not have this limitation.  | [optional] 
**custodial_minimum_deposit_threshold** | **str** | The minimum deposit amount for Custodial Wallets. If the amount you deposit to a Custodial Wallet is smaller than this threshold, the deposit will not show up on Cobo Portal or trigger any webhook events.  Note: [Loop transfers](https://loop.top/) do not have this limitation.  | [optional] 

## Example

```python
from cobo_waas2.models.token_info import TokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInfo from a JSON string
token_info_instance = TokenInfo.from_json(json)
# print the JSON string representation of the object
print(TokenInfo.to_json())

# convert the object into a dict
token_info_dict = token_info_instance.to_dict()
# create an instance of TokenInfo from a dict
token_info_from_dict = TokenInfo.from_dict(token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


