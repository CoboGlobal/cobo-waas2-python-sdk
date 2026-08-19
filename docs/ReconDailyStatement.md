# ReconDailyStatement

The daily reconciliation statement for a wallet and token on a business date.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biz_date** | **date** | The business date (UTC), in YYYY-MM-DD format. | 
**token_id** | **str** | The token ID, which is the unique identifier of a token. | 
**chain_id** | **str** | The chain ID, which is the unique identifier of a blockchain. | 
**wallet_id** | **str** | The wallet ID. | 
**opening_balance** | **str** | The opening balance at the start of the business date, expressed in the token&#39;s main unit. | 
**total_deposit** | **str** | The total deposit amount during the business date, expressed in the token&#39;s main unit. | 
**deposit_count** | **int** | The number of deposits during the business date. | 
**total_withdrawal** | **str** | The total withdrawal amount during the business date, expressed in the token&#39;s main unit. | 
**withdrawal_count** | **int** | The number of withdrawals during the business date. | 
**closing_balance** | **str** | The closing balance at the end of the business date, expressed in the token&#39;s main unit. | 
**status** | [**ReconStatementStatus**](ReconStatementStatus.md) |  | 

## Example

```python
from cobo_waas2.models.recon_daily_statement import ReconDailyStatement

# TODO update the JSON string below
json = "{}"
# create an instance of ReconDailyStatement from a JSON string
recon_daily_statement_instance = ReconDailyStatement.from_json(json)
# print the JSON string representation of the object
print(ReconDailyStatement.to_json())

# convert the object into a dict
recon_daily_statement_dict = recon_daily_statement_instance.to_dict()
# create an instance of ReconDailyStatement from a dict
recon_daily_statement_from_dict = ReconDailyStatement.from_dict(recon_daily_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


