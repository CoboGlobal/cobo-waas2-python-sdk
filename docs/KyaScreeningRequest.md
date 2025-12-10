# KyaScreeningRequest

Individual address screening request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The request ID that is used to track a request. The request ID is provided by you and must be unique within your organization. This ID is used for idempotency to prevent duplicate submissions and for troubleshooting purposes. | 
**address** | **str** | The blockchain address to be screened. For chains requiring memo (XRP, EOS, XLM, IOST, BNB_BNB, ATOM, LUNA, TON), append the memo to the address using \&quot;|\&quot; separator (e.g., \&quot;address|memo\&quot;).  | 
**chain_id** | **str** | The chain identifier (e.g., ETH, BTC, TRON). | 
**note** | **str** | Optional note for this address screening. | [optional] 

## Example

```python
from cobo_waas2.models.kya_screening_request import KyaScreeningRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KyaScreeningRequest from a JSON string
kya_screening_request_instance = KyaScreeningRequest.from_json(json)
# print the JSON string representation of the object
print(KyaScreeningRequest.to_json())

# convert the object into a dict
kya_screening_request_dict = kya_screening_request_instance.to_dict()
# create an instance of KyaScreeningRequest from a dict
kya_screening_request_from_dict = KyaScreeningRequest.from_dict(kya_screening_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


