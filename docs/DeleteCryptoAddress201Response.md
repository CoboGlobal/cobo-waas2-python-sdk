# DeleteCryptoAddress201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_address_id** | **str** | The crypto address ID. | 

## Example

```python
from cobo_waas2.models.delete_crypto_address201_response import DeleteCryptoAddress201Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCryptoAddress201Response from a JSON string
delete_crypto_address201_response_instance = DeleteCryptoAddress201Response.from_json(json)
# print the JSON string representation of the object
print(DeleteCryptoAddress201Response.to_json())

# convert the object into a dict
delete_crypto_address201_response_dict = delete_crypto_address201_response_instance.to_dict()
# create an instance of DeleteCryptoAddress201Response from a dict
delete_crypto_address201_response_from_dict = DeleteCryptoAddress201Response.from_dict(delete_crypto_address201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


