# AddressVerification

Summary of a self-custody address verification record. Returned as items in [List address verifications](#operation/list_address_verifications). Call [Get address verification](#operation/get_address_verification) with `verification_id` to retrieve method-specific provenance (`satoshi_test_detail` / `signature_detail`). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique identifier of this verification record. | 
**address** | **str** | The counterparty (self-custody) wallet address being verified. | 
**chain_id** | **str** | The chain on which this address is verified. | 
**status** | [**AddressVerificationStatus**](AddressVerificationStatus.md) |  | 
**verification_method** | [**AddressVerificationMethod**](AddressVerificationMethod.md) |  | 
**verified_at** | **int** | Timestamp (milliseconds) when verification completed. &#x60;null&#x60; while &#x60;status&#x3D;PENDING&#x60; or &#x60;FAILED&#x60;. | [optional] 

## Example

```python
from cobo_waas2.models.address_verification import AddressVerification

# TODO update the JSON string below
json = "{}"
# create an instance of AddressVerification from a JSON string
address_verification_instance = AddressVerification.from_json(json)
# print the JSON string representation of the object
print(AddressVerification.to_json())

# convert the object into a dict
address_verification_dict = address_verification_instance.to_dict()
# create an instance of AddressVerification from a dict
address_verification_from_dict = AddressVerification.from_dict(address_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


