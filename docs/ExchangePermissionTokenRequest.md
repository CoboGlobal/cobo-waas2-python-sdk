# ExchangePermissionTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_type** | **str** | The OAuth permission type. Set the value as &#x60;payment_orders_payin&#x60;. | 

## Example

```python
from cobo_waas2.models.exchange_permission_token_request import ExchangePermissionTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangePermissionTokenRequest from a JSON string
exchange_permission_token_request_instance = ExchangePermissionTokenRequest.from_json(json)
# print the JSON string representation of the object
print(ExchangePermissionTokenRequest.to_json())

# convert the object into a dict
exchange_permission_token_request_dict = exchange_permission_token_request_instance.to_dict()
# create an instance of ExchangePermissionTokenRequest from a dict
exchange_permission_token_request_from_dict = ExchangePermissionTokenRequest.from_dict(exchange_permission_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


