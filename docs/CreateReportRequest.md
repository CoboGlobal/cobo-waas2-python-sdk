# CreateReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **int** | The start time of the report. Unix timestamp measured in seconds. | 
**end_time** | **int** | The end time of the report. Unix timestamp measured in seconds. | 
**report_export_format** | [**ReportExportFormat**](ReportExportFormat.md) |  | 
**report_types** | [**List[ReportType]**](ReportType.md) |  | 
**token_ids** | **List[str]** | Optional filter to include only items related to specified token IDs in the report. | [optional] 

## Example

```python
from cobo_waas2.models.create_report_request import CreateReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReportRequest from a JSON string
create_report_request_instance = CreateReportRequest.from_json(json)
# print the JSON string representation of the object
print(CreateReportRequest.to_json())

# convert the object into a dict
create_report_request_dict = create_report_request_instance.to_dict()
# create an instance of CreateReportRequest from a dict
create_report_request_from_dict = CreateReportRequest.from_dict(create_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


