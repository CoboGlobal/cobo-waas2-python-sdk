# cobo_waas2.AddressBooksApi

All URIs are relative to *https://api.dev.cobo.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address_books**](AddressBooksApi.md#create_address_books) | **POST** /address_books | Create Address Book entries
[**delete_address_book_by_id**](AddressBooksApi.md#delete_address_book_by_id) | **POST** /address_books/{entry_id}/delete | Delete Address Book entry
[**get_address_book_by_id**](AddressBooksApi.md#get_address_book_by_id) | **GET** /address_books/{entry_id} | Get Address Book entry
[**list_address_books**](AddressBooksApi.md#list_address_books) | **GET** /address_books | List Address Book entries
[**update_address_book_by_id**](AddressBooksApi.md#update_address_book_by_id) | **PUT** /address_books/{entry_id} | Update Address Book entry


# **create_address_books**
> CreateAddressBooks201Response create_address_books(create_address_books_param=create_address_books_param)

Create Address Book entries

This operation adds new entries (records) to your Address Book. <Note>This operation is available upon request. Please contact our [customer support](mailto:help@cobo.com) to enable it.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.create_address_books201_response import CreateAddressBooks201Response
from cobo_waas2.models.create_address_books_param import CreateAddressBooksParam
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
    api_instance = cobo_waas2.AddressBooksApi(api_client)
    create_address_books_param = cobo_waas2.CreateAddressBooksParam()

    try:
        # Create Address Book entries
        api_response = api_instance.create_address_books(create_address_books_param=create_address_books_param)
        print("The response of AddressBooksApi->create_address_books:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBooksApi->create_address_books: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_address_books_param** | [**CreateAddressBooksParam**](CreateAddressBooksParam.md)| The request body of the create Address Books operation. | [optional] 

### Return type

[**CreateAddressBooks201Response**](CreateAddressBooks201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The information about created Address Books. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_address_book_by_id**
> DeleteAddressBookById201Response delete_address_book_by_id(entry_id)

Delete Address Book entry

This operation deletes a specified Address Book entry (record). <Note>This operation is available upon request. Please contact our [customer support](mailto:help@cobo.com) to enable it.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.delete_address_book_by_id201_response import DeleteAddressBookById201Response
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
    api_instance = cobo_waas2.AddressBooksApi(api_client)
    entry_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Delete Address Book entry
        api_response = api_instance.delete_address_book_by_id(entry_id)
        print("The response of AddressBooksApi->delete_address_book_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBooksApi->delete_address_book_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**| The Address Book entry ID. | 

### Return type

[**DeleteAddressBookById201Response**](DeleteAddressBookById201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request was successful. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_book_by_id**
> AddressBook get_address_book_by_id(entry_id)

Get Address Book entry

This operation retrieves the detailed information about a specified Address Book entry (record). 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.address_book import AddressBook
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
    api_instance = cobo_waas2.AddressBooksApi(api_client)
    entry_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'

    try:
        # Get Address Book entry
        api_response = api_instance.get_address_book_by_id(entry_id)
        print("The response of AddressBooksApi->get_address_book_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBooksApi->get_address_book_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**| The Address Book entry ID. | 

### Return type

[**AddressBook**](AddressBook.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about an Address Book. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_address_books**
> ListAddressBooks200Response list_address_books(chain_id=chain_id, address=address, label=label, limit=limit, before=before, after=after)

List Address Book entries

This operation retrieves all entries (records) from your Address Book. You can filter the entries by chain ID, address, and label. 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.list_address_books200_response import ListAddressBooks200Response
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
    api_instance = cobo_waas2.AddressBooksApi(api_client)
    chain_id = 'ETH'
    address = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
    label = 'test'
    limit = 10
    before = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGmk1'
    after = 'RqeEoTkgKG5rpzqYzg2Hd3szmPoj2cE7w5jWwShz3C1vyGSAk'

    try:
        # List Address Book entries
        api_response = api_instance.list_address_books(chain_id=chain_id, address=address, label=label, limit=limit, before=before, after=after)
        print("The response of AddressBooksApi->list_address_books:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBooksApi->list_address_books: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| The chain ID, which is the unique identifier of a blockchain. You can retrieve the IDs of all the chains you can use by calling [List enabled chains](https://www.cobo.com/developers/v2/api-references/wallets/list-enabled-chains). | [optional] 
 **address** | **str**|  | [optional] 
 **label** | **str**| A user-defined label for the address. | [optional] 
 **limit** | **int**| The maximum number of objects to return. For most operations, the value range is [1, 50]. | [optional] [default to 10]
 **before** | **str**| A cursor indicating the position before the current page. This value is generated by Cobo and returned in the response. If you are paginating forward from the beginning, you do not need to provide it on the first request. When paginating backward (to the previous page), you should pass the before value returned from the last response.  | [optional] 
 **after** | **str**| A cursor indicating the position after the current page. This value is generated by Cobo and returned in the response. You do not need to provide it on the first request. When paginating forward (to the next page), you should pass the after value returned from the last response.  | [optional] 

### Return type

[**ListAddressBooks200Response**](ListAddressBooks200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about an Address Book. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address_book_by_id**
> AddressBook update_address_book_by_id(entry_id, update_address_book_param=update_address_book_param)

Update Address Book entry

This operation updates the information of a specified Address Book entry (record). <Note>This operation is available upon request. Please contact our [customer support](mailto:help@cobo.com) to enable it.</Note> 

### Example

* OAuth Authentication (OAuth2):
* Api Key Authentication (CoboAuth):

```python
import cobo_waas2
from cobo_waas2.models.address_book import AddressBook
from cobo_waas2.models.update_address_book_param import UpdateAddressBookParam
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
    api_instance = cobo_waas2.AddressBooksApi(api_client)
    entry_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
    update_address_book_param = cobo_waas2.UpdateAddressBookParam()

    try:
        # Update Address Book entry
        api_response = api_instance.update_address_book_by_id(entry_id, update_address_book_param=update_address_book_param)
        print("The response of AddressBooksApi->update_address_book_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressBooksApi->update_address_book_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**| The Address Book entry ID. | 
 **update_address_book_param** | [**UpdateAddressBookParam**](UpdateAddressBookParam.md)| The request body of the update Address Book operation. | [optional] 

### Return type

[**AddressBook**](AddressBook.md)

### Authorization

[OAuth2](../README.md#OAuth2), [CoboAuth](../README.md#CoboAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated Address Book. |  -  |
**4XX** | Bad request. Your request contains malformed syntax or invalid parameters. |  -  |
**5XX** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

