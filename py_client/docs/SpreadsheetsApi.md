# \SpreadsheetsApi

All URIs are relative to *https://api.wk-dev.wdesk.org/v1beta1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SpreadsheetsPost**](SpreadsheetsApi.md#SpreadsheetsPost) | **Post** /spreadsheets | Create a new spreadsheet.
[**SpreadsheetsSpreadsheetIdDelete**](SpreadsheetsApi.md#SpreadsheetsSpreadsheetIdDelete) | **Delete** /spreadsheets/{SpreadsheetId} | Delete a Spreadsheet
[**SpreadsheetsSpreadsheetIdGet**](SpreadsheetsApi.md#SpreadsheetsSpreadsheetIdGet) | **Get** /spreadsheets/{SpreadsheetId} | Retrieve a Spreadsheet
[**SpreadsheetsSpreadsheetIdPut**](SpreadsheetsApi.md#SpreadsheetsSpreadsheetIdPut) | **Put** /spreadsheets/{SpreadsheetId} | Update a Spreadsheet
[**SpreadsheetsSpreadsheetIdSheetsGet**](SpreadsheetsApi.md#SpreadsheetsSpreadsheetIdSheetsGet) | **Get** /spreadsheets/{SpreadsheetId}/sheets | Get a list of sheets
[**SpreadsheetsSpreadsheetIdSheetsPost**](SpreadsheetsApi.md#SpreadsheetsSpreadsheetIdSheetsPost) | **Post** /spreadsheets/{SpreadsheetId}/sheets | Creates a new Sheet
[**SpreadsheetsSpreadsheetIdSheetsSheetIdDataGet**](SpreadsheetsApi.md#SpreadsheetsSpreadsheetIdSheetsSheetIdDataGet) | **Get** /spreadsheets/{SpreadsheetId}/sheets/{SheetId}/data | Retrieves data in a Region
[**SpreadsheetsSpreadsheetIdSheetsSheetIdDataPut**](SpreadsheetsApi.md#SpreadsheetsSpreadsheetIdSheetsSheetIdDataPut) | **Put** /spreadsheets/{SpreadsheetId}/sheets/{SheetId}/data | Writes data in a Region
[**SpreadsheetsSpreadsheetIdSheetsSheetIdDelete**](SpreadsheetsApi.md#SpreadsheetsSpreadsheetIdSheetsSheetIdDelete) | **Delete** /spreadsheets/{SpreadsheetId}/sheets/{SheetId} | Deletes a Sheet.
[**SpreadsheetsSpreadsheetIdSheetsSheetIdGet**](SpreadsheetsApi.md#SpreadsheetsSpreadsheetIdSheetsSheetIdGet) | **Get** /spreadsheets/{SpreadsheetId}/sheets/{SheetId} | Retrieve a Sheet
[**SpreadsheetsSpreadsheetIdSheetsSheetIdPut**](SpreadsheetsApi.md#SpreadsheetsSpreadsheetIdSheetsSheetIdPut) | **Put** /spreadsheets/{SpreadsheetId}/sheets/{SheetId} | Updates a Sheet


# **SpreadsheetsPost**
> SpreadsheetResponse SpreadsheetsPost($spreadsheetBodyParameter, $xApiKey)

Create a new spreadsheet.


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheetBodyParameter** | [**SpreadsheetBody**](SpreadsheetBody.md)| Properties for creating a new spreadsheet | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 

### Return type

[**SpreadsheetResponse**](SpreadsheetResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SpreadsheetsSpreadsheetIdDelete**
> EmptyResponse SpreadsheetsSpreadsheetIdDelete($spreadsheetId, $xApiKey)

Delete a Spreadsheet

Deletes an existing spreadsheet. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheetId** | **string**| A unique identifier for a spreadsheet | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SpreadsheetsSpreadsheetIdGet**
> SpreadsheetResponse SpreadsheetsSpreadsheetIdGet($spreadsheetId, $xApiKey, $revision)

Retrieve a Spreadsheet

Gets an existing spreadsheet given a spreadsheet id.


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheetId** | **string**| A unique identifier for a spreadsheet | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 
 **revision** | **int32**| The Spreadsheet revision from which to select data. If no revision is  provided, the latest revision will be selected.  | [optional] 

### Return type

[**SpreadsheetResponse**](SpreadsheetResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SpreadsheetsSpreadsheetIdPut**
> EmptyResponse SpreadsheetsSpreadsheetIdPut($spreadsheetId, $spreadsheetBodyParameter, $xApiKey)

Update a Spreadsheet

Updates a Spreadsheet using the given Spreadsheet properties. If any  property is null or not included in the request the property will not  be modified. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheetId** | **string**| A unique identifier for a spreadsheet | 
 **spreadsheetBodyParameter** | [**SpreadsheetBody**](SpreadsheetBody.md)| Properties for creating a new spreadsheet | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SpreadsheetsSpreadsheetIdSheetsGet**
> SheetsResponse SpreadsheetsSpreadsheetIdSheetsGet($spreadsheetId, $xApiKey, $revision)

Get a list of sheets

Retrieves all Sheets in the outline


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheetId** | **string**| A unique identifier for a spreadsheet | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 
 **revision** | **int32**| The Spreadsheet revision from which to select data. If no revision is  provided, the latest revision will be selected.  | [optional] 

### Return type

[**SheetsResponse**](SheetsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SpreadsheetsSpreadsheetIdSheetsPost**
> SheetResponse SpreadsheetsSpreadsheetIdSheetsPost($spreadsheetId, $sheetBodyParameter, $xApiKey)

Creates a new Sheet

Creates a new sheet within the current spreadsheet.


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheetId** | **string**| A unique identifier for a spreadsheet | 
 **sheetBodyParameter** | [**SheetBody**](SheetBody.md)| Properties for creating a new sheet | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 

### Return type

[**SheetResponse**](SheetResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SpreadsheetsSpreadsheetIdSheetsSheetIdDataGet**
> RangeDataResponse SpreadsheetsSpreadsheetIdSheetsSheetIdDataGet($spreadsheetId, $sheetId, $xApiKey, $revision, $region, $page, $perPage)

Retrieves data in a Region

Retrieves all data in a region, paging if necessary.   When paging, the revision parameter must be set and the per_page parameter indicates the  maximum number of cells to include in a single response. The server enforces a maximum  per_page of 50,000. An unbounded region may only be used to obtain the first page of  results. Use the paged_region or next_url from the first page to retrieve  subsequent pages. All cells in the requested region will appear exactly once during the  paging process, however ordering is not guaranteed. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheetId** | **string**| A unique identifier for a spreadsheet | 
 **sheetId** | **string**| A unique identifier for a sheet within a spreadsheet | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 
 **revision** | **int32**| The Spreadsheet revision from which to select data. If no revision is  provided, the latest revision will be selected.  | [optional] 
 **region** | **string**| A1 style representation of a Cell or Range. The Range may be unbounded in  any/all directions.  For example: * The (entirely bounded) Range \&quot;A2:D8\&quot; will select all data in the Range between A2 and D8 (inclusive) * The (unbounded in rows) Range \&quot;A:A\&quot; will select all data in column A * The (unbounded in stop coordinates) Range \&quot;B3:\&quot; will select all data below and to the right of B3 (inclusive)  If no region is provided, all data in the sheet will be selected.  | [optional] 
 **page** | **int32**| The page of results to return.  | [optional] 
 **perPage** | **int32**| The number of items to return per page. Leave blank for no limit, returning all results.  | [optional] 

### Return type

[**RangeDataResponse**](RangeDataResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SpreadsheetsSpreadsheetIdSheetsSheetIdDataPut**
> EmptyResponse SpreadsheetsSpreadsheetIdSheetsSheetIdDataPut($spreadsheetId, $sheetId, $rangeDataBodyParameter, $xApiKey, $region)

Writes data in a Region

Overwrites all data in a region with new data. If the provided RangeData is smaller than the specified Region, all cells in the Region and not covered by the RangeData will be cleared. The provided RangeData must not be larger than the specified Region. An empty RangeData is valid and may be used to clear a Region.' 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheetId** | **string**| A unique identifier for a spreadsheet | 
 **sheetId** | **string**| A unique identifier for a sheet within a spreadsheet | 
 **rangeDataBodyParameter** | [**RangeDataBody**](RangeDataBody.md)| Multidimensional array of cell values in row-major order. The &#x60;null&#x60; JSON value may be used to avoid modifying a cell. | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 
 **region** | **string**| A1 style representation of a Cell or Range. The Range may be unbounded in  any/all directions.  For example: * The (entirely bounded) Range \&quot;A2:D8\&quot; will select all data in the Range between A2 and D8 (inclusive) * The (unbounded in rows) Range \&quot;A:A\&quot; will select all data in column A * The (unbounded in stop coordinates) Range \&quot;B3:\&quot; will select all data below and to the right of B3 (inclusive)  If no region is provided, all data in the sheet will be selected.  | [optional] 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SpreadsheetsSpreadsheetIdSheetsSheetIdDelete**
> EmptyResponse SpreadsheetsSpreadsheetIdSheetsSheetIdDelete($spreadsheetId, $sheetId, $xApiKey)

Deletes a Sheet.

Deletes the identified sheet.


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheetId** | **string**| A unique identifier for a spreadsheet | 
 **sheetId** | **string**| A unique identifier for a sheet within a spreadsheet | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SpreadsheetsSpreadsheetIdSheetsSheetIdGet**
> SheetResponse SpreadsheetsSpreadsheetIdSheetsSheetIdGet($spreadsheetId, $sheetId, $xApiKey, $revision)

Retrieve a Sheet

Retrieves a sheet from the identified spreadsheet


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheetId** | **string**| A unique identifier for a spreadsheet | 
 **sheetId** | **string**| A unique identifier for a sheet within a spreadsheet | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 
 **revision** | **int32**| The Spreadsheet revision from which to select data. If no revision is  provided, the latest revision will be selected.  | [optional] 

### Return type

[**SheetResponse**](SheetResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SpreadsheetsSpreadsheetIdSheetsSheetIdPut**
> EmptyResponse SpreadsheetsSpreadsheetIdSheetsSheetIdPut($spreadsheetId, $sheetId, $sheetBodyParameter, $xApiKey)

Updates a Sheet

Updates a Sheet using the given Sheet properties. If any property is  set to the null JSON value or not included in the request the property  will not be modified. 


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheetId** | **string**| A unique identifier for a spreadsheet | 
 **sheetId** | **string**| A unique identifier for a sheet within a spreadsheet | 
 **sheetBodyParameter** | [**SheetBody**](SheetBody.md)| Properties for creating a new sheet | 
 **xApiKey** | **string**| API callers are identified by API keys. Throttling and request quota limits are set for each individual API key.   | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

