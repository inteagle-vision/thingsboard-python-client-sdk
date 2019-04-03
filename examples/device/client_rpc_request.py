import psutil
import time
import logging
from tb_device_mqtt import TBClient
logging.basicConfig(level=logging.DEBUG)


def callback(request_id, resp_body):
    print("request id: {request_id}, response body: {resp_body}".format(request_id=request_id,
                                                                        resp_body=resp_body))


//TODO: replace
client = TBClient("demo.thingsboard.io", "HvbKddqKsxVqowKoSR2J")

client.connect()
# call "getTime" on server and receive result, then process it with callback
client.send_rpc_call("getTime", {}, callback)
while True:
    time.sleep(1)
