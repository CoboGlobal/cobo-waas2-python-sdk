# SignatureDetail

Details of an off-chain signature that verified a self-custody address. Returned only when `verification_method=SIGNATURE`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The self-custody wallet address that signed the challenge. | 
**challenge** | **str** | The challenge string that was signed. | [optional] 
**signature** | **str** | The wallet signature submitted by the client. | [optional] 
**verified_at** | **int** | Timestamp (milliseconds) when the signature was verified. | [optional] 

## Example

```python
from cobo_waas2.models.signature_detail import SignatureDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureDetail from a JSON string
signature_detail_instance = SignatureDetail.from_json(json)
# print the JSON string representation of the object
print(SignatureDetail.to_json())

# convert the object into a dict
signature_detail_dict = signature_detail_instance.to_dict()
# create an instance of SignatureDetail from a dict
signature_detail_from_dict = SignatureDetail.from_dict(signature_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


