# AddressVerificationDetailSatoshiTestDetail

The latest Satoshi Test challenge associated with this verification. Present only when `verification_method=SATOSHI_TEST`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge_id** | **str** | The unique identifier of the Satoshi Test challenge. | 
**from_address** | **str** | The counterparty (self-custody) wallet address that must transfer the micro-deposit. | 
**to_address** | **str** | The Cobo-generated verification address that will receive the micro-deposit. | 
**amount** | **str** | The exact amount (in the token&#39;s smallest unit) that must be transferred. The amount is unique per challenge and is used together with &#x60;to_address&#x60; to identify a matching on-chain transfer.  | 
**token_id** | **str** | The ID of the token used for the micro-deposit (typically the chain&#39;s native asset). | 
**chain_id** | **str** | The chain on which the micro-deposit is expected. | 
**status** | [**SatoshiTestChallengeStatus**](SatoshiTestChallengeStatus.md) |  | 
**remaining_seconds** | **int** | Remaining time (in seconds) before the challenge expires. &#x60;0&#x60; when the challenge is not yet submitted or has already completed/expired.  | 
**matched_txid** | **str** | The on-chain transaction hash of the matching transfer, once matched. | [optional] 
**started_at** | **int** | Timestamp (milliseconds) when the challenge was submitted and the countdown started. | [optional] 
**expires_at** | **int** | Timestamp (milliseconds) when the challenge will expire if not matched. | [optional] 

## Example

```python
from cobo_waas2.models.address_verification_detail_satoshi_test_detail import AddressVerificationDetailSatoshiTestDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AddressVerificationDetailSatoshiTestDetail from a JSON string
address_verification_detail_satoshi_test_detail_instance = AddressVerificationDetailSatoshiTestDetail.from_json(json)
# print the JSON string representation of the object
print(AddressVerificationDetailSatoshiTestDetail.to_json())

# convert the object into a dict
address_verification_detail_satoshi_test_detail_dict = address_verification_detail_satoshi_test_detail_instance.to_dict()
# create an instance of AddressVerificationDetailSatoshiTestDetail from a dict
address_verification_detail_satoshi_test_detail_from_dict = AddressVerificationDetailSatoshiTestDetail.from_dict(address_verification_detail_satoshi_test_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


