# ListFeeStationFiatTransactions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FeeStationFiatTransaction]**](FeeStationFiatTransaction.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from cobo_waas2.models.list_fee_station_fiat_transactions200_response import ListFeeStationFiatTransactions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListFeeStationFiatTransactions200Response from a JSON string
list_fee_station_fiat_transactions200_response_instance = ListFeeStationFiatTransactions200Response.from_json(json)
# print the JSON string representation of the object
print(ListFeeStationFiatTransactions200Response.to_json())

# convert the object into a dict
list_fee_station_fiat_transactions200_response_dict = list_fee_station_fiat_transactions200_response_instance.to_dict()
# create an instance of ListFeeStationFiatTransactions200Response from a dict
list_fee_station_fiat_transactions200_response_from_dict = ListFeeStationFiatTransactions200Response.from_dict(list_fee_station_fiat_transactions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


