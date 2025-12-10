# cobo_waas2.ComplianceApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kya_screenings**](ComplianceApi.md#create_kya_screenings) | **POST** /compliance/kya/screenings | Batch create KYA address screening requests
[**get_disposition_status**](ComplianceApi.md#get_disposition_status) | **GET** /compliance/funds/disposition | Query disposition status
[**get_kya_screening**](ComplianceApi.md#get_kya_screening) | **GET** /compliance/kya/screenings/{screening_id} | Retrieve single KYA address screening result
[**get_kyt_screening_status**](ComplianceApi.md#get_kyt_screening_status) | **GET** /compliance/kyt/screenings/status | Retrieve KYT screening status
[**isolate_funds**](ComplianceApi.md#isolate_funds) | **POST** /compliance/funds/disposition/isolate | Create fund isolate disposition
[**list_kya_screenings**](ComplianceApi.md#list_kya_screenings) | **GET** /compliance/kya/screenings | Query KYA address screening results
[**refund_funds**](ComplianceApi.md#refund_funds) | **POST** /compliance/funds/disposition/refund | Create fund refund disposition
[**submit_kyt_manual_review**](ComplianceApi.md#submit_kyt_manual_review) | **POST** /compliance/kyt/screenings/manual_review | Submit KYT manual review result
[**submit_kyt_screening_decisions**](ComplianceApi.md#submit_kyt_screening_decisions) | **POST** /compliance/kyt/screenings/decisions | Submit KYT screening decision
[**unfreeze_funds**](ComplianceApi.md#unfreeze_funds) | **POST** /compliance/funds/disposition/unfreeze | Unfreeze frozen funds


# **create_kya_screenings**
> List[KyaScreeningResult] create_kya_screenings(create_kya_screenings_body=create_kya_screenings_body)

Batch create KYA address screening requests

This operation submits batch address screening requests to detect address compliance and risk levels. Up to 50 addresses can be submitted in a single request.  <Note>This endpoint supports cross-chain address screening with independent idempotency for each address, enabling flexible error handling and partial retries.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_kya_screenings_body import CreateKyaScreeningsBody
from cobo_waas2.models.kya_screening_result import KyaScreeningResult
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.ComplianceApi(api_client)
    create_kya_screenings_body = cobo_waas2.CreateKyaScreeningsBody()

    try:
        # Batch create KYA address screening requests
        api_response = api_instance.create_kya_screenings(create_kya_screenings_body=create_kya_screenings_body)
        print("The response of ComplianceApi->create_kya_screenings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->create_kya_screenings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_kya_screenings_body** | [**CreateKyaScreeningsBody**](CreateKyaScreeningsBody.md)| The request body to batch create KYA address screening requests | [optional] 

### Return type

[**List[KyaScreeningResult]**](KyaScreeningResult.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created address screening requests |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disposition_status**
> DispositionQueryResponse get_disposition_status(transaction_id)

Query disposition status

This operation retrieves the current status of a disposition request for a specific transaction.  You can use this endpoint to check the status of any disposition operation (Refund, Isolate, or Unfreeze)  that has been initiated for a transaction. The response includes the disposition type, current status,  and the disposition transaction ID if applicable.  <Note>Use this endpoint to monitor the progress of disposition operations and verify their completion.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.disposition_query_response import DispositionQueryResponse
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.ComplianceApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Query disposition status
        api_response = api_instance.get_disposition_status(transaction_id)
        print("The response of ComplianceApi->get_disposition_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_disposition_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The unique identifier (UUID) of the transaction to retrieve KYT screening status information for. | 

### Return type

[**DispositionQueryResponse**](DispositionQueryResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved disposition information |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kya_screening**
> KyaScreeningResult get_kya_screening(screening_id)

Retrieve single KYA address screening result

This operation retrieves a specific address screening result by screening_id, including complete risk assessment information.  <Note>This endpoint returns the full screening details including risk level, summary, and detailed risk category exposures.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.kya_screening_result import KyaScreeningResult
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.ComplianceApi(api_client)
    screening_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Retrieve single KYA address screening result
        api_response = api_instance.get_kya_screening(screening_id)
        print("The response of ComplianceApi->get_kya_screening:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_kya_screening: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screening_id** | **str**| The unique identifier (UUID) of the address screening request. | 

### Return type

[**KyaScreeningResult**](KyaScreeningResult.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved address screening result |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kyt_screening_status**
> KytScreeningsTransaction get_kyt_screening_status(transaction_id)

Retrieve KYT screening status

This operation retrieves the current KYT (Know Your Transaction) screening status and compliance information for a specific transaction.  Use this endpoint to monitor the real-time screening status, review decisions, and funds disposition status for transactions that have been processed through the KYT compliance system. The response includes detailed screening results, risk assessment outcomes, and current funds status.  <Note>This endpoint provides comprehensive compliance monitoring capabilities to help maintain AML (Anti-Money Laundering) regulatory compliance and audit trail requirements.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.kyt_screenings_transaction import KytScreeningsTransaction
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.ComplianceApi(api_client)
    transaction_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Retrieve KYT screening status
        api_response = api_instance.get_kyt_screening_status(transaction_id)
        print("The response of ComplianceApi->get_kyt_screening_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_kyt_screening_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The unique identifier (UUID) of the transaction to retrieve KYT screening status information for. | 

### Return type

[**KytScreeningsTransaction**](KytScreeningsTransaction.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved KYT screening information |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **isolate_funds**
> DispositionResponse isolate_funds(isolate_disposition=isolate_disposition)

Create fund isolate disposition

This operation creates an isolate disposition request for a specific transaction.  The isolated funds will be sent to a designated isolation address for compliance purposes.  You need to specify the transaction ID to be isolated and the destination address.  Optional parameters include custom categories for tracking purposes.  <Note>The isolate process will initiate a withdrawal transaction from the compliance-managed address to the specified isolation address.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.disposition_response import DispositionResponse
from cobo_waas2.models.isolate_disposition import IsolateDisposition
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.ComplianceApi(api_client)
    isolate_disposition = cobo_waas2.IsolateDisposition()

    try:
        # Create fund isolate disposition
        api_response = api_instance.isolate_funds(isolate_disposition=isolate_disposition)
        print("The response of ComplianceApi->isolate_funds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->isolate_funds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isolate_disposition** | [**IsolateDisposition**](IsolateDisposition.md)| The request body to create an isolate disposition | [optional] 

### Return type

[**DispositionResponse**](DispositionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created disposition request |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kya_screenings**
> ListKyaScreenings200Response list_kya_screenings(screening_ids=screening_ids, limit=limit, before=before, after=after)

Query KYA address screening results

This operation queries the results of specified screening requests with pagination support. You can filter specific screening requests using screening_ids (up to 50 IDs).  <Note>For large-scale queries exceeding 50 screening results, use pagination parameters (limit, before, after) for multiple queries.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_kya_screenings200_response import ListKyaScreenings200Response
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.ComplianceApi(api_client)
    screening_ids = 'f47ac10b-58cc-4372-a567-0e02b2c3d479,a1b2c3d4-e5f6-4321-8765-fedcba987654'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # Query KYA address screening results
        api_response = api_instance.list_kya_screenings(screening_ids=screening_ids, limit=limit, before=before, after=after)
        print("The response of ComplianceApi->list_kya_screenings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->list_kya_screenings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screening_ids** | **str**| A comma-separated list of screening request IDs to filter specific screening results. Maximum 50 IDs allowed to ensure URL length stays within standard web server limits (typically 8KB).  Each ID must be in standard UUID format (36 characters fixed length).  Example: &#x60;f47ac10b-58cc-4372-a567-0e02b2c3d479,a1b2c3d4-e5f6-4321-8765-fedcba987654&#x60;  | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data before the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C.  If you set &#x60;before&#x60; to the ID of Object C (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object A.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned. - If you set it to &#x60;infinity&#x60;, the last page of data is returned.  | [optional] 
 **after** | **str**| This parameter specifies an object ID as a starting point for pagination, retrieving data after the specified object relative to the current dataset.    Suppose the current data is ordered as Object A, Object B, and Object C. If you set &#x60;after&#x60; to the ID of Object A (&#x60;RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk&#x60;), the response will include Object B and Object C.    **Notes**:   - If you set both &#x60;after&#x60; and &#x60;before&#x60;, an error will occur. - If you leave both &#x60;before&#x60; and &#x60;after&#x60; empty, the first page of data is returned.  | [optional] 

### Return type

[**ListKyaScreenings200Response**](ListKyaScreenings200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved address screening results with pagination |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_funds**
> DispositionResponse refund_funds(refund_disposition=refund_disposition)

Create fund refund disposition

This operation creates a refund disposition request for a specific transaction.  The refunded funds will be sent to the specified destination address.  You need to specify the transaction ID to be refunded and the destination address.  Optional parameters include custom categories for tracking purposes.  <Note>The refund process will initiate a withdrawal transaction from the compliance-managed address to the specified destination.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.disposition_response import DispositionResponse
from cobo_waas2.models.refund_disposition import RefundDisposition
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.ComplianceApi(api_client)
    refund_disposition = cobo_waas2.RefundDisposition()

    try:
        # Create fund refund disposition
        api_response = api_instance.refund_funds(refund_disposition=refund_disposition)
        print("The response of ComplianceApi->refund_funds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->refund_funds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_disposition** | [**RefundDisposition**](RefundDisposition.md)| The request body to create a refund disposition | [optional] 

### Return type

[**DispositionResponse**](DispositionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created disposition request |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_kyt_manual_review**
> SubmitKytResponse submit_kyt_manual_review(submit_kyt_screenings_review_body=submit_kyt_screenings_review_body)

Submit KYT manual review result

This operation submits manual review results for KYT (Know Your Transaction) screening cases that require human intervention and analysis.  Use this endpoint when transactions flagged for manual review have been analyzed by compliance officers and require submission of review outcomes with detailed comments and justifications. This endpoint is specifically designed for submitting comprehensive manual review findings rather than automated screening decisions.  <Note>Submitting manual review results will update the KYT screening status and initiate appropriate compliance workflow actions based on the review outcome.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.submit_kyt_response import SubmitKytResponse
from cobo_waas2.models.submit_kyt_screenings_review_body import SubmitKytScreeningsReviewBody
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.ComplianceApi(api_client)
    submit_kyt_screenings_review_body = cobo_waas2.SubmitKytScreeningsReviewBody()

    try:
        # Submit KYT manual review result
        api_response = api_instance.submit_kyt_manual_review(submit_kyt_screenings_review_body=submit_kyt_screenings_review_body)
        print("The response of ComplianceApi->submit_kyt_manual_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->submit_kyt_manual_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_kyt_screenings_review_body** | [**SubmitKytScreeningsReviewBody**](SubmitKytScreeningsReviewBody.md)| The request body to submit manual review results for KYT screening cases requiring human analysis | [optional] 

### Return type

[**SubmitKytResponse**](SubmitKytResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully submitted external KYT review |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_kyt_screening_decisions**
> SubmitKytResponse submit_kyt_screening_decisions(submit_kyt_screenings_decisions_body=submit_kyt_screenings_decisions_body)

Submit KYT screening decision

This operation submits the final KYT (Know Your Transaction) screening decision for a specific transaction based on external compliance review results.  Use this endpoint to provide screening decisions (Approve, ApproveWithAlert, Reject, or ManualReview) after completing the external KYT screening process. The submitted decision will be recorded for compliance audit purposes and regulatory reporting requirements.  <Note>Submitting a screening decision will update the transaction's KYT status and may automatically trigger downstream compliance workflows or notifications based on the decision type.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.submit_kyt_response import SubmitKytResponse
from cobo_waas2.models.submit_kyt_screenings_decisions_body import SubmitKytScreeningsDecisionsBody
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.ComplianceApi(api_client)
    submit_kyt_screenings_decisions_body = cobo_waas2.SubmitKytScreeningsDecisionsBody()

    try:
        # Submit KYT screening decision
        api_response = api_instance.submit_kyt_screening_decisions(submit_kyt_screenings_decisions_body=submit_kyt_screenings_decisions_body)
        print("The response of ComplianceApi->submit_kyt_screening_decisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->submit_kyt_screening_decisions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_kyt_screenings_decisions_body** | [**SubmitKytScreeningsDecisionsBody**](SubmitKytScreeningsDecisionsBody.md)| The request body to submit a KYT screening decision result based on external compliance review | [optional] 

### Return type

[**SubmitKytResponse**](SubmitKytResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully submitted external KYT result |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfreeze_funds**
> DispositionResponse unfreeze_funds(unfreeze_disposition=unfreeze_disposition)

Unfreeze frozen funds

This operation creates an unfreeze request for a previously frozen transaction.  The unfreeze operation will release the frozen funds back to their original state.  You only need to specify the transaction ID to be unfrozen. Once unfrozen, the funds  will be available for normal operations.  <Note>The unfreeze process will release the compliance hold on the transaction, allowing it to proceed normally.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.disposition_response import DispositionResponse
from cobo_waas2.models.unfreeze_disposition import UnfreezeDisposition
from cobo_waas2.rest import ApiException
from pprint import pprint

# See configuration.py for a list of all supported configurations.
configuration = cobo_waas2.Configuration(
    # Replace `<YOUR_PRIVATE_KEY>` with your private key
    api_private_key="<YOUR_PRIVATE_KEY>",
    # Select the development environment. To use the production environment, change the URL to https://api.cobo.com/v2.
    host="https://api.dev.cobo.com/v2"
)
# Enter a context with an instance of the API client
with cobo_waas2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cobo_waas2.ComplianceApi(api_client)
    unfreeze_disposition = cobo_waas2.UnfreezeDisposition()

    try:
        # Unfreeze frozen funds
        api_response = api_instance.unfreeze_funds(unfreeze_disposition=unfreeze_disposition)
        print("The response of ComplianceApi->unfreeze_funds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->unfreeze_funds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unfreeze_disposition** | [**UnfreezeDisposition**](UnfreezeDisposition.md)| The request body to create an unfreeze disposition | [optional] 

### Return type

[**DispositionResponse**](DispositionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created disposition request |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

