import token
import adal
import requests
import os
import json
import ast

tenantId = 'eb20330a-b375-43c2-a621-3d5443b27184'
clientId = '0b37aa6e-932b-4b23-b507-9fd25247aafb'
clientSecret = 'n*jjU/or[xTuFUeRH-eYtesXp3beu983'
resource = 'https://management.core.windows.net/'
subscriptionId = '48b9dd42-97d6-47c1-8227-eb67af109112'
authentication_endpoint = 'https://login.microsoftonline.com/'



def getAADToken():

    # get an Azure access token using the adal library
    context = adal.AuthenticationContext(authentication_endpoint + tenantId)
    token_response = context.acquire_token_with_client_credentials(resource, clientId, clientSecret)

    access_token = token_response.get('accessToken')
    return access_token

def createRsGrp(access_token):
    headers = {'Content-Type': 'application/json', 'Authorization':  'Bearer ' + access_token}

    params = {'api-version': '2017-05-10'}
    # 2019-04-01
    #Creating Resource Group
    url = 'https://management.azure.com/subscriptions/48b9dd42-97d6-47c1-8227-eb67af109112/resourcegroups/kailashpythonRS'

    data = {'location': 'West US 2'}

    resgrp = requests.put(url, data=json.dumps(data), headers=headers, params=params)

    print(json.dumps(resgrp.json(), indent=4, separators=(',', ': ')))

def createStorageAccount(access_token,headers,params):
    #creating Storage Account
    data = {'location': 'West US 2',
      "properties": {

          "encryption": {
                  "services": {
                           "blob": {
                                   "enabled": 'true'
                           }
                  },
                  "keySource": "Microsoft.Storage"
          }
      },
      "sku": {
          "name": "Standard_RAGRS"
      },
      "kind": "Storage"
            }

    # url='https://management.azure.com/subscriptions/48b9dd42-97d6-47c1-8227-eb67af109112/resourceGroups/kailashpythonRS/providers/Microsoft.Storage/storageAccounts/kailashpythonSTR'
    url = 'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{0}/providers/Microsoft.Storage/storageAccounts/{1}'.format('kailashpythonRS','kailashpythonstr',subscription= subscriptionId)
    print("url",url)
    r = requests.put(url, data=json.dumps(data), headers=headers, params=params)
    print(json.dumps(r.json(), indent=4, separators=(',', ': ')))

def createDatalakeStorage(token):

    # create ADLS account
    url = 'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{0}/providers/Microsoft.DataLakeStore/accounts/kailashadls?api-version=2016-11-01'.format('kailashpythonRS',subscription= subscriptionId)
    data = {'location': 'East US2'}
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + token}

    response = requests.put(url=url, data=json.dumps(data), headers=headers)
    print(response.text)
    print("Successfully created ADLS!")

def createDatalakeAnalytic(token):

    # create ADLA account
    url = 'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{0}/providers/Microsoft.DataLakeAnalytics/accounts/kailashadla?api-version=2016-11-01'.format('kailashpythonRS',subscription= subscriptionId)
    data = {
     "location": "eastus2",
     "properties": {
        "defaultDataLakeStoreAccount": "kailashadls",
            "dataLakeStoreAccounts": [
            {
             "name": "kailashadls"
            }
        ]
     }
    }
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + token}

    response = requests.put(url=url, data=json.dumps(data), headers=headers)
    print(response.text)

def createDataFactory(token):


    # Create Data Factory
    url = 'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{0}/providers/Microsoft.DataFactory/factories/kailashadf?api-version=2018-06-01'.format('kailashpythonRS',subscription= subscriptionId)
    data = {
     "location": "East US2"
    }
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + token}

    response = requests.put(url=url, data=json.dumps(data), headers=headers)
    print(response.text)
    print("Created azure data factory!!!")


def createLinkedServicesadls(token):
    # Create ADLS linked services
    url = 'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{0}/providers/Microsoft.DataFactory/factories/{1}/linkedservices/{2}?api-version=2018-06-01'.format('kailashpythonRS','kailashadf','adlsKailash',subscription= subscriptionId)
    data = {
        "properties": {
            "type": "AzureDataLakeStore",
            "typeProperties": {
                "dataLakeStoreUri": "https://kailashadls.azuredatalakestore.net/webhdfs/v1",
                "servicePrincipalId": "0b37aa6e-932b-4b23-b507-9fd25247aafb",
                "servicePrincipalKey": {
                    "type": "SecureString",
                    "value": "n*jjU/or[xTuFUeRH-eYtesXp3beu983"
                },
                "tenant": "eb20330a-b375-43c2-a621-3d5443b27184"
            }

        }
    }
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.put(url=url, data=json.dumps(data), headers=headers)
    print(response.text)
    print("Created adls linked services successfullty...!!!!!")

def createDatasetadlsInput(token):

    # Create Dataset for input folder in ADLS
    url = 'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{0}/providers/Microsoft.DataFactory/factories/{1}/datasets/ADLSinputDataset?api-version=2018-06-01'.format('kailashpythonRS','kailashadf',subscription= subscriptionId)
    data = {
        "name": "ADLSinputDataset",
        "properties": {
            "type": "AzureDataLakeStoreFile",
            "linkedServiceName": {
                "referenceName": "adlsKailash",
                "type": "LinkedServiceReference"
            },
            "typeProperties": {
                "folderPath": "Input",
                "fileName": "Position_Salaries.csv",
                "format": {
                    "type": "TextFormat",
                    "columnDelimiter": ";",
                    "rowDelimiter": "\n",
                    "firstRowAsHeader": True,
                }
            }
        }
    }
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.put(url=url, data=json.dumps(data), headers=headers)
    print(response.text)
    print("Input dataset created successfully..!")

def createDatasetadlsOutput(token):

    # Create Dataset for Output folder in ADLS
    url = 'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{0}/providers/Microsoft.DataFactory/factories/{1}/datasets/ADLSoutputDataset?api-version=2018-06-01'.format('kailashpythonRS','kailashadf',subscription= subscriptionId)
    data = {
        "name": "ADLSoutputDataset",
        "properties": {
            "type": "AzureDataLakeStoreFile",
            "linkedServiceName": {
                "referenceName": "adlsKailash",
                "type": "LinkedServiceReference"
            },
            "typeProperties": {
                "folderPath": "Output"
            }
        }
    }
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.put(url=url, data=json.dumps(data), headers=headers)
    print(response.text)

def createCopyActivity(token):


    # Create pipeline with copy activity
    url = 'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{0}/providers/Microsoft.DataFactory/factories/{1}/pipelines/kailashpipeline?api-version=2018-06-01'.format('kailashpythonRS','kailashadf',subscription= subscriptionId)
    data = {
        "name": "kailashpipeline",
        "properties": {
            "activities": [
                {"name": "CopyFromADLS_ADLS",
                 "type": "Copy",
                 "inputs": [
                    {
                        "referenceName": "ADLSinputDataset",
                        "type": "DatasetReference"
                    }
                 ],
                 "outputs": [
                    {
                        "referenceName": "ADLSoutputDataset",
                        "type": "DatasetReference"
                    }
                 ],
                 "typeProperties": {
                    "source": {
                        "type": "DelimitedTextSource",
                        "formatSettings": {
                            "type": "DelimitedTextReadSetting",
                        }
                    },
                    "sink": {
                        "type": "DelimitedTextSource"
                    }
                 }
                 }
            ]
        }
    }
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.put(url=url, data=json.dumps(data), headers=headers)
    print(response.text)

def ExecutePipeline(token):
    # Run Pipeline
    url = 'https://management.azure.com/subscriptions/{subscription}/resourceGroups/{0}/providers/Microsoft.DataFactory/factories/{1}/pipelines/{2}/createRun?api-version=2018-06-01'.format('kailashpythonRS','kailashadf','kailashpipeline',subscription= subscriptionId)
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.post(url=url, headers=headers)
    print(response.text)

def main():
    token = getAADToken()
    # token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InU0T2ZORlBId0VCb3NIanRyYXVPYlY4NExuWSIsImtpZCI6InU0T2ZORlBId0VCb3NIanRyYXVPYlY4NExuWSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldC8iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC9lYjIwMzMwYS1iMzc1LTQzYzItYTYyMS0zZDU0NDNiMjcxODQvIiwiaWF0IjoxNTY0NTY2MDYzLCJuYmYiOjE1NjQ1NjYwNjMsImV4cCI6MTU2NDU2OTk2MywiYWlvIjoiNDJGZ1lIZ2lYTlIxN1BPVGNPRVRaUUtYSXJrMkFRQT0iLCJhcHBpZCI6IjBiMzdhYTZlLTkzMmItNGIyMy1iNTA3LTlmZDI1MjQ3YWFmYiIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0L2ViMjAzMzBhLWIzNzUtNDNjMi1hNjIxLTNkNTQ0M2IyNzE4NC8iLCJvaWQiOiIwYjA1MjZmMC0wNDFiLTQ3MzQtOWYwMi1lNDMxMmJkMjY0YTYiLCJzdWIiOiIwYjA1MjZmMC0wNDFiLTQ3MzQtOWYwMi1lNDMxMmJkMjY0YTYiLCJ0aWQiOiJlYjIwMzMwYS1iMzc1LTQzYzItYTYyMS0zZDU0NDNiMjcxODQiLCJ1dGkiOiJiQXhwT0tDSWlVU0RqZnJYUDBRbEFBIiwidmVyIjoiMS4wIn0.CmXuyqygpfZ3W0GfLbKg-7wUZnymDuDzpx-pBzmCEac-VLH4yBiqINW4t5A_QqZDpLRjZCgdlpUaJoxISSBbc05zGzqGhCm-fC2h0GQqslhg7i9yQW1pzN17G_kIOVUhqtczlrdg_IG5M_XhoJrjyY2Bt6aSC-xA8LI0Ds7A_AS-CgYAKTvNPi0hiO9qSqzNAceXCCepiCzYtqUMhsTxc7IttlXlO_I7w8NTgtNUWRhzcBl671ky8zFhVaxrz_zI8edU1vgTXnCFIrucVZAZ7ABBHrg3YD2XykHWDc01t_NIqw5MBxOTjDsOtibUn5hSvUIPMTTVAN_DSeGEJwGNFQ"
    headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + token}

    params = {'api-version': '2019-04-01'}
    # rsGroup = createRsGrp(token)
    # strAct = createStorageAccount(token,headers,params)
    # createDatalakeStorage(token)
    # createDatalakeAnalytic(token)
    # createDataFactory(token)
    # createLinkedServicesadls(token)
    # createDatasetadlsInput(token)
    # createDatasetadlsOutput(token)
    # createCopyActivity(token)
    ExecutePipeline(token)

main()
