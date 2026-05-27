# CreateSatoshiTestChallengeRequest

Request body for creating a Satoshi Test challenge. A single endpoint covers both the two-step flow (`PREPARE` then `SUBMIT`) and the one-shot flow (`SUBMIT` directly). Idempotent on `(chain_id, from_address)` per organization. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**SatoshiTestChallengeAction**](SatoshiTestChallengeAction.md) |  | 
**chain_id** | **str** | The chain ID of the counterparty address. See the operation description for supported chains. | 
**from_address** | **str** | The counterparty (self-custody) wallet address that will transfer the micro-deposit. | 
**transaction_id** | **str** | The Cobo transaction ID that this Satoshi Test is verifying for. | 
**transaction_type** | [**TravelRuleTransactionType**](TravelRuleTransactionType.md) |  | 
**challenge_id** | **str** | The &#x60;challenge_id&#x60; returned by a previous &#x60;PREPARE&#x60; call. - When &#x60;action&#x3D;SUBMIT&#x60;: if provided, activates that specific challenge by id (recommended when you cached the id client-side after &#x60;PREPARE&#x60;). If omitted, the server activates the latest matching challenge identified by &#x60;(chain_id, from_address)&#x60;. - When &#x60;action&#x3D;PREPARE&#x60;: **must be omitted**. A new challenge is always generated; passing a &#x60;challenge_id&#x60; here will cause the request to be rejected.  | [optional] 

## Example

```python
from cobo_waas2.models.create_satoshi_test_challenge_request import CreateSatoshiTestChallengeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSatoshiTestChallengeRequest from a JSON string
create_satoshi_test_challenge_request_instance = CreateSatoshiTestChallengeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSatoshiTestChallengeRequest.to_json())

# convert the object into a dict
create_satoshi_test_challenge_request_dict = create_satoshi_test_challenge_request_instance.to_dict()
# create an instance of CreateSatoshiTestChallengeRequest from a dict
create_satoshi_test_challenge_request_from_dict = CreateSatoshiTestChallengeRequest.from_dict(create_satoshi_test_challenge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


