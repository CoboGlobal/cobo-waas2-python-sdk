# Merchant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_id** | **str** | The merchant ID. | 
**name** | **str** | The merchant name. | 
**wallet_id** | **str** | This field has been deprecated. | 
**developer_fee_rate** | **str** | The merchant-level fee fraction applied specifically to Top-up-mode deposits. The value can range from &#x60;0&#x60; through &#x60;1&#x60; and can contain up to four decimal places. For example, &#x60;0.015&#x60; represents 1.5%. An absent or cleared value is treated as zero, so no developer fee is charged on Top-up deposits.  An update applies only to subsequent Top-up deposits and is not retroactive to deposits that have already been processed. The developer share is rounded down to the token&#39;s precision.  This rate does not combine with a Payment Order&#39;s &#x60;fee_amount&#x60;. Order-mode and Top-up-mode deposits use separate, mutually exclusive settlement paths, so there is no calculation order or precedence between the two fees.  For configuration and settlement details, see [Merchant management](https://www.cobo.com/payments/en/guides/merchants), [Payment collection in order mode](https://www.cobo.com/payments/en/guides/create-orders), and [Accounts and fund allocation](https://www.cobo.com/payments/en/guides/amounts-and-balances).  | [optional] 
**wallet_setup** | [**WalletSetup**](WalletSetup.md) |  | [optional] 
**created_timestamp** | **int** | The creation time of the merchant, represented as a UNIX timestamp in seconds. | [optional] 
**updated_timestamp** | **int** | The last update time of the merchant, represented as a UNIX timestamp in seconds. | [optional] 

## Example

```python
from cobo_waas2.models.merchant import Merchant

# TODO update the JSON string below
json = "{}"
# create an instance of Merchant from a JSON string
merchant_instance = Merchant.from_json(json)
# print the JSON string representation of the object
print(Merchant.to_json())

# convert the object into a dict
merchant_dict = merchant_instance.to_dict()
# create an instance of Merchant from a dict
merchant_from_dict = Merchant.from_dict(merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


