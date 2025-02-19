# AddressBalance

The token balance for a specific wallet address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet address. | 
**balance** | [**Balance**](Balance.md) |  | 

## Example

```python
from cobo_waas2.models.address_balance import AddressBalance

# TODO update the JSON string below
json = "{}"
# create an instance of AddressBalance from a JSON string
address_balance_instance = AddressBalance.from_json(json)
# print the JSON string representation of the object
print(AddressBalance.to_json())

# convert the object into a dict
address_balance_dict = address_balance_instance.to_dict()
# create an instance of AddressBalance from a dict
address_balance_from_dict = AddressBalance.from_dict(address_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


