# LockUtxosRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**utxos** | [**List[LockUtxosRequestUtxosInner]**](LockUtxosRequestUtxosInner.md) |  | 

## Example

```python
from cobo_waas2.models.lock_utxos_request import LockUtxosRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LockUtxosRequest from a JSON string
lock_utxos_request_instance = LockUtxosRequest.from_json(json)
# print the JSON string representation of the object
print(LockUtxosRequest.to_json())

# convert the object into a dict
lock_utxos_request_dict = lock_utxos_request_instance.to_dict()
# create an instance of LockUtxosRequest from a dict
lock_utxos_request_from_dict = LockUtxosRequest.from_dict(lock_utxos_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


