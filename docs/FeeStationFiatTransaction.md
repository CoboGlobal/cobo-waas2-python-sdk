# FeeStationFiatTransaction

The information about a fiat transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The transaction ID. | 
**main_transaction_id** | **str** | The UUID of the parent (main) transaction that this record is associated with. Set only when the current record is a gas/fee transaction initiated by FeeStation; omit for main transactions. | [optional] 
**transaction_type** | [**FeeStationFiatTransactionType**](FeeStationFiatTransactionType.md) |  | 
**amount** | **str** | The transaction amount. | 
**fiat_currency** | **str** | The fiat currency of the transaction. Possible values include:   - &#x60;USD&#x60;: US Dollar.  | 
**status** | **str** | The status of the fiat transaction. Possible values include:   - &#x60;Created&#x60;: The transaction has been created.   - &#x60;Succeeded&#x60;: The transaction has been completed successfully.  | 
**cobo_category** | **List[str]** | The Cobo category of the transaction. | [optional] 
**created_timestamp** | **int** | The time when the transaction was created, in Unix timestamp format, measured in milliseconds. | [optional] 
**modified_timestamp** | **int** | The time when the transaction was last modified, in Unix timestamp format, measured in milliseconds. | [optional] 

## Example

```python
from cobo_waas2.models.fee_station_fiat_transaction import FeeStationFiatTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of FeeStationFiatTransaction from a JSON string
fee_station_fiat_transaction_instance = FeeStationFiatTransaction.from_json(json)
# print the JSON string representation of the object
print(FeeStationFiatTransaction.to_json())

# convert the object into a dict
fee_station_fiat_transaction_dict = fee_station_fiat_transaction_instance.to_dict()
# create an instance of FeeStationFiatTransaction from a dict
fee_station_fiat_transaction_from_dict = FeeStationFiatTransaction.from_dict(fee_station_fiat_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


