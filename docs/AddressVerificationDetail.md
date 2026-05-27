# AddressVerificationDetail

Full detail of a single address verification record, including method-specific provenance.  - `verification_method=SIGNATURE` → `signature_detail` is populated, `satoshi_test_detail` is `null`. - `verification_method=SATOSHI_TEST` → `satoshi_test_detail` carries the latest challenge state (`status`, `remaining_seconds`, `matched_txid`); `signature_detail` is `null`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique identifier of this verification record. | 
**address** | **str** | The counterparty (self-custody) wallet address being verified. | 
**chain_id** | **str** | The chain on which this address is verified. | 
**status** | [**AddressVerificationStatus**](AddressVerificationStatus.md) |  | 
**verification_method** | [**AddressVerificationMethod**](AddressVerificationMethod.md) |  | 
**verified_at** | **int** | Timestamp (milliseconds) when verification completed. &#x60;null&#x60; while &#x60;status&#x3D;PENDING&#x60; or &#x60;FAILED&#x60;. | [optional] 
**satoshi_test_detail** | [**AddressVerificationDetailSatoshiTestDetail**](AddressVerificationDetailSatoshiTestDetail.md) |  | [optional] 
**signature_detail** | [**AddressVerificationDetailSignatureDetail**](AddressVerificationDetailSignatureDetail.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.address_verification_detail import AddressVerificationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AddressVerificationDetail from a JSON string
address_verification_detail_instance = AddressVerificationDetail.from_json(json)
# print the JSON string representation of the object
print(AddressVerificationDetail.to_json())

# convert the object into a dict
address_verification_detail_dict = address_verification_detail_instance.to_dict()
# create an instance of AddressVerificationDetail from a dict
address_verification_detail_from_dict = AddressVerificationDetail.from_dict(address_verification_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


