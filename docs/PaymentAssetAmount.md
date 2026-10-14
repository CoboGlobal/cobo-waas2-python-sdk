# PaymentAssetAmount

A cryptocurrency asset amount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The amount of the asset, represented as a decimal string. | 
**token_id** | **str** | The token ID of the asset. | 
**chain_id** | **str** | The chain ID of the asset. | 

## Example

```python
from cobo_waas2.models.payment_asset_amount import PaymentAssetAmount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAssetAmount from a JSON string
payment_asset_amount_instance = PaymentAssetAmount.from_json(json)
# print the JSON string representation of the object
print(PaymentAssetAmount.to_json())

# convert the object into a dict
payment_asset_amount_dict = payment_asset_amount_instance.to_dict()
# create an instance of PaymentAssetAmount from a dict
payment_asset_amount_from_dict = PaymentAssetAmount.from_dict(payment_asset_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


