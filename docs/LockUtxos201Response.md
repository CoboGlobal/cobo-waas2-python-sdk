# LockUtxos201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executed** | **bool** | Whether the locking or unlocking operation has been successfully executed. - &#x60;true&#x60;: The operation has been successfully executed. - &#x60;false&#x60;: The operation has not been executed.  | [optional] 

## Example

```python
from cobo_waas2.models.lock_utxos201_response import LockUtxos201Response

# TODO update the JSON string below
json = "{}"
# create an instance of LockUtxos201Response from a JSON string
lock_utxos201_response_instance = LockUtxos201Response.from_json(json)
# print the JSON string representation of the object
print(LockUtxos201Response.to_json())

# convert the object into a dict
lock_utxos201_response_dict = lock_utxos201_response_instance.to_dict()
# create an instance of LockUtxos201Response from a dict
lock_utxos201_response_from_dict = LockUtxos201Response.from_dict(lock_utxos201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


