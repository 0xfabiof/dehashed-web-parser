# Dehashed-web-parser

A python script tool to leverage the web-interface of Dehashed Free Edition to provide results in an API format - similar to the official Json Format (pay-walled) 

## Requirements

* Python 2
* Curl
* Dehashed.com account
* A valid session_id (you can retrieve it by logging in to Dehashed and retrieving the "mysession" cookie)

## Usage

```
python2 dehashed.py <valid session_id> <query>
```

## Todo:

* Add more than first 10 results parsing
