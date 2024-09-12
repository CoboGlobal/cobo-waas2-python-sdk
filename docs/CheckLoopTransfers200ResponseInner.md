# CheckLoopTransfers200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet address. | [optional] 
**is_loop** | **bool** | Whether the transaction from the given source to the given destination address can be executed as a Loop transfer.  - &#x60;true&#x60;: The transaction can be executed as a Loop transfer. - &#x60;false&#x60;: The transaction cannot be executed as a Loop transfer.  | [optional] 

## Example

```python
from cobo_waas2.models.check_loop_transfers200_response_inner import CheckLoopTransfers200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CheckLoopTransfers200ResponseInner from a JSON string
check_loop_transfers200_response_inner_instance = CheckLoopTransfers200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(CheckLoopTransfers200ResponseInner.to_json())

# convert the object into a dict
check_loop_transfers200_response_inner_dict = check_loop_transfers200_response_inner_instance.to_dict()
# create an instance of CheckLoopTransfers200ResponseInner from a dict
check_loop_transfers200_response_inner_from_dict = CheckLoopTransfers200ResponseInner.from_dict(check_loop_transfers200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


