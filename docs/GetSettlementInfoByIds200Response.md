# GetSettlementInfoByIds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**psp_token_balances** | [**List[SettlementInfo]**](SettlementInfo.md) |  | [optional] 
**token_balances** | [**List[SettlementInfo]**](SettlementInfo.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.get_settlement_info_by_ids200_response import GetSettlementInfoByIds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSettlementInfoByIds200Response from a JSON string
get_settlement_info_by_ids200_response_instance = GetSettlementInfoByIds200Response.from_json(json)
# print the JSON string representation of the object
print(GetSettlementInfoByIds200Response.to_json())

# convert the object into a dict
get_settlement_info_by_ids200_response_dict = get_settlement_info_by_ids200_response_instance.to_dict()
# create an instance of GetSettlementInfoByIds200Response from a dict
get_settlement_info_by_ids200_response_from_dict = GetSettlementInfoByIds200Response.from_dict(get_settlement_info_by_ids200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


