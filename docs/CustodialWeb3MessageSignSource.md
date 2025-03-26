# CustodialWeb3MessageSignSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**MessageSignSourceType**](MessageSignSourceType.md) |  | 
**wallet_id** | **str** | The wallet ID. | 
**address** | **str** | The wallet address. | 

## Example

```python
from cobo_waas2.models.custodial_web3_message_sign_source import CustodialWeb3MessageSignSource

# TODO update the JSON string below
json = "{}"
# create an instance of CustodialWeb3MessageSignSource from a JSON string
custodial_web3_message_sign_source_instance = CustodialWeb3MessageSignSource.from_json(json)
# print the JSON string representation of the object
print(CustodialWeb3MessageSignSource.to_json())

# convert the object into a dict
custodial_web3_message_sign_source_dict = custodial_web3_message_sign_source_instance.to_dict()
# create an instance of CustodialWeb3MessageSignSource from a dict
custodial_web3_message_sign_source_from_dict = CustodialWeb3MessageSignSource.from_dict(custodial_web3_message_sign_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


