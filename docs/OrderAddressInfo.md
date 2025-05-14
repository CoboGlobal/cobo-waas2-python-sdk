# OrderAddressInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The ID of the linked wallet. | 
**amount** | **str** | The amount of cryptocurrency received by the order&#39;s receiving address. | 
**created_timestamp** | **int** | The created time of the address, represented as a UNIX timestamp in seconds. | 
**updated_timestamp** | **int** | The updated time of the address, represented as a UNIX timestamp in seconds. | 

## Example

```python
from cobo_waas2.models.order_address_info import OrderAddressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderAddressInfo from a JSON string
order_address_info_instance = OrderAddressInfo.from_json(json)
# print the JSON string representation of the object
print(OrderAddressInfo.to_json())

# convert the object into a dict
order_address_info_dict = order_address_info_instance.to_dict()
# create an instance of OrderAddressInfo from a dict
order_address_info_from_dict = OrderAddressInfo.from_dict(order_address_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


