# PaymentAssetOrFiatAmount

An amount represented either as a cryptocurrency asset or a fiat currency.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_type** | **str** | The amount representation type. | 
**amount** | **str** | The amount, represented as a decimal string. | 
**token_id** | **str** | The token ID of the asset. This field is present when &#x60;amount_type&#x60; is &#x60;Crypto&#x60;. | [optional] 
**chain_id** | **str** | The chain ID of the asset. This field is present when &#x60;amount_type&#x60; is &#x60;Crypto&#x60;. | [optional] 
**currency** | **str** | The fiat currency code. This field is present when &#x60;amount_type&#x60; is &#x60;Fiat&#x60;. | [optional] 

## Example

```python
from cobo_waas2.models.payment_asset_or_fiat_amount import PaymentAssetOrFiatAmount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAssetOrFiatAmount from a JSON string
payment_asset_or_fiat_amount_instance = PaymentAssetOrFiatAmount.from_json(json)
# print the JSON string representation of the object
print(PaymentAssetOrFiatAmount.to_json())

# convert the object into a dict
payment_asset_or_fiat_amount_dict = payment_asset_or_fiat_amount_instance.to_dict()
# create an instance of PaymentAssetOrFiatAmount from a dict
payment_asset_or_fiat_amount_from_dict = PaymentAssetOrFiatAmount.from_dict(payment_asset_or_fiat_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


