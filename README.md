# tardis-api-client

## Summary
This is ChronosLabs Python client for interacting with [Tardis data API](https://docs.tardis.dev/downloadable-csv-files). Details of the API itself can be found there. This README only covers usage for our client.

## Usage

**Option 1 - CLI**

Standard CLI program. Sample command: 
`python3 dataset-puller.py -from 2022-09-08 -to 2022-09-09 -sym "BTCUSDT ETHUSDT"`

**Option 2 - UI**

This program has been wrapped by an UI. This means you can specify input parameters via the UI, instead of manually typing them out like above. To launch the UI, simply run `python dataset-puller.py`. Fill in the options in the UI and execute.
<img width="618" alt="Screen Shot 2022-09-13 at 6 31 46 PM" src="https://user-images.githubusercontent.com/113400670/190021372-43e18dad-8fef-4d0e-a5fd-0a2db4bf31e1.png">
