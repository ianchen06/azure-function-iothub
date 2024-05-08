# Azure IoT to PostgreSQL

This Azure Function will be triggered when there is a new event in IoTHub. Then, it will write the data into PostgreSQL via the `psycopg2` library.

## Getting Started

1. Install Azure Function extension in VSCode
1. CMD+p and search for "Create Function App in Azure," following the instructions
1. CMD+p and search for "Deploy to Function App," following the instructions
1. After the deployment, check the function by going to the Azure web portal
1. Add `IOTHUB_CONNECTION_STRING` and `DATABASE_URL` environment variable in Function App settings 
1. Send a test event and it should be written to your PostgreSQL database  

## Environment Variables

| Environment Variable | Example Value |
| ------------- | ------------- |
| IOTHUB_CONNECTION_STRING  | Endpoint=sb://somethingnamespace.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=cmysharedaccGu72NY=;EntityPath=iothub-ehub-techin510-111111-111111  |
| DATABASE_URL  | postgresql://<postgres-username>:<somepassword>@aws-0-us-west-1.pooler.supabase.com:5432/postgres  |
