# CancelSatoshiTestChallengeRequest

Request body for cancelling a Satoshi Test challenge that is in `PREPARE` or `PENDING` status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_id** | **str** | The challenge ID to cancel. | 

## Example

```python
from cobo_waas2.models.cancel_satoshi_test_challenge_request import CancelSatoshiTestChallengeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelSatoshiTestChallengeRequest from a JSON string
cancel_satoshi_test_challenge_request_instance = CancelSatoshiTestChallengeRequest.from_json(json)
# print the JSON string representation of the object
print(CancelSatoshiTestChallengeRequest.to_json())

# convert the object into a dict
cancel_satoshi_test_challenge_request_dict = cancel_satoshi_test_challenge_request_instance.to_dict()
# create an instance of CancelSatoshiTestChallengeRequest from a dict
cancel_satoshi_test_challenge_request_from_dict = CancelSatoshiTestChallengeRequest.from_dict(cancel_satoshi_test_challenge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


