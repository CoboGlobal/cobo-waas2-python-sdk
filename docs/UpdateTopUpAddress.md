# UpdateTopUpAddress

The request body to update top up address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. | [optional] 
**token_id** | **str** | The token ID, which identifies the cryptocurrency. Supported values:    - USDC: &#x60;ETH_USDC&#x60;, &#x60;ARBITRUM_USDC&#x60;, &#x60;SOL_USDC&#x60;, &#x60;BASE_USDC&#x60;, &#x60;MATIC_USDC&#x60;, &#x60;BSC_USDC&#x60;   - USDT: &#x60;TRON_USDT&#x60;, &#x60;ETH_USDT&#x60;, &#x60;ARBITRUM_USDT&#x60;, &#x60;SOL_USDT&#x60;, &#x60;BASE_USDT&#x60;, &#x60;MATIC_USDT&#x60;, &#x60;BSC_USDT&#x60;  | 
**custom_payer_id** | **str** | Unique customer identifier on the merchant side, used to allocate a dedicated top-up address  | 

## Example

```python
from cobo_waas2.models.update_top_up_address import UpdateTopUpAddress

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTopUpAddress from a JSON string
update_top_up_address_instance = UpdateTopUpAddress.from_json(json)
# print the JSON string representation of the object
print(UpdateTopUpAddress.to_json())

# convert the object into a dict
update_top_up_address_dict = update_top_up_address_instance.to_dict()
# create an instance of UpdateTopUpAddress from a dict
update_top_up_address_from_dict = UpdateTopUpAddress.from_dict(update_top_up_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


