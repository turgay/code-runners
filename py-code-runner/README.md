Code runner web app. Runs given python code through REST api.

Sample code run curl call:

curl -i -H "Content-Type: application/json" -X POST -d '{"code":"import datetime\nprint datetime.datetime.now() "}' http://localhost:7000/pycoder/api/v1.0/run
