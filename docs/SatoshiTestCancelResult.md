# SatoshiTestCancelResult

Returned by [Cancel Satoshi Test challenge](#operation/cancel_satoshi_test_challenge).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_id** | **str** | The challenge that was cancelled. | 
**status** | **str** | Final status after cancellation. | 

## Example

```python
from cobo_waas2.models.satoshi_test_cancel_result import SatoshiTestCancelResult

# TODO update the JSON string below
json = "{}"
# create an instance of SatoshiTestCancelResult from a JSON string
satoshi_test_cancel_result_instance = SatoshiTestCancelResult.from_json(json)
# print the JSON string representation of the object
print(SatoshiTestCancelResult.to_json())

# convert the object into a dict
satoshi_test_cancel_result_dict = satoshi_test_cancel_result_instance.to_dict()
# create an instance of SatoshiTestCancelResult from a dict
satoshi_test_cancel_result_from_dict = SatoshiTestCancelResult.from_dict(satoshi_test_cancel_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


