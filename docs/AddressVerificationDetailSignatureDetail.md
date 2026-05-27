# AddressVerificationDetailSignatureDetail

Off-chain signature provenance. Present only when `verification_method=SIGNATURE`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The self-custody wallet address that signed the challenge. | 
**challenge** | **str** | The challenge string that was signed. | [optional] 
**signature** | **str** | The wallet signature submitted by the client. | [optional] 
**verified_at** | **int** | Timestamp (milliseconds) when the signature was verified. | [optional] 

## Example

```python
from cobo_waas2.models.address_verification_detail_signature_detail import AddressVerificationDetailSignatureDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AddressVerificationDetailSignatureDetail from a JSON string
address_verification_detail_signature_detail_instance = AddressVerificationDetailSignatureDetail.from_json(json)
# print the JSON string representation of the object
print(AddressVerificationDetailSignatureDetail.to_json())

# convert the object into a dict
address_verification_detail_signature_detail_dict = address_verification_detail_signature_detail_instance.to_dict()
# create an instance of AddressVerificationDetailSignatureDetail from a dict
address_verification_detail_signature_detail_from_dict = AddressVerificationDetailSignatureDetail.from_dict(address_verification_detail_signature_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


