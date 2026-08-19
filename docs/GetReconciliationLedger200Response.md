# GetReconciliationLedger200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReconLedgerEntry]**](ReconLedgerEntry.md) | The list of reconciliation ledger entries. A single transaction may produce multiple entries (for example, an internal transfer), which share the same &#x60;transaction_id&#x60;. | 

## Example

```python
from cobo_waas2.models.get_reconciliation_ledger200_response import GetReconciliationLedger200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReconciliationLedger200Response from a JSON string
get_reconciliation_ledger200_response_instance = GetReconciliationLedger200Response.from_json(json)
# print the JSON string representation of the object
print(GetReconciliationLedger200Response.to_json())

# convert the object into a dict
get_reconciliation_ledger200_response_dict = get_reconciliation_ledger200_response_instance.to_dict()
# create an instance of GetReconciliationLedger200Response from a dict
get_reconciliation_ledger200_response_from_dict = GetReconciliationLedger200Response.from_dict(get_reconciliation_ledger200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


