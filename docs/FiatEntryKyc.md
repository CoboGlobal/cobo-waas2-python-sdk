# FiatEntryKyc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fiat_entry_kyc_id** | **str** | The fiat entry KYC ID. | 
**status** | [**FiatEntryKycStatus**](FiatEntryKycStatus.md) |  | 

## Example

```python
from cobo_waas2.models.fiat_entry_kyc import FiatEntryKyc

# TODO update the JSON string below
json = "{}"
# create an instance of FiatEntryKyc from a JSON string
fiat_entry_kyc_instance = FiatEntryKyc.from_json(json)
# print the JSON string representation of the object
print(FiatEntryKyc.to_json())

# convert the object into a dict
fiat_entry_kyc_dict = fiat_entry_kyc_instance.to_dict()
# create an instance of FiatEntryKyc from a dict
fiat_entry_kyc_from_dict = FiatEntryKyc.from_dict(fiat_entry_kyc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


