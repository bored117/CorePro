from jinbase import TestBase
from corepro.customer import Customer
import httplib
import requests
from corepro.models.envelope import Envelope
from corepro.models.envelope import Envelope
from corepro.coreproapiexception import CoreProApiException

#r = requests.get('https://sandbox-api.corepro.io/customer/list', auth=('payoff','A99EAE16-C4F9-405D-81C0-39317B980EA0'))
#print r.status_code
#print r.headers
#print r.encoding
#print r.text
#print r.json()

SDK_USER_AGENT = "CorePro Python SDK v {0}".format("1.0.0")
httpConn = httplib.HTTPSConnection(TestBase.Conn.domainName, 433)
print TestBase.Conn.headerValue
print TestBase.Conn.domainName
headers = {'User-Agent':SDK_USER_AGENT,
           'Content_type':'application/json; charset=utf-8',
           'Accept':'application/json; charset=utf-8',
           'Authorization': TestBase.Conn.headerValue,
           'Host': TestBase.Conn.domainName}
print headers
httpConn.request("GET","https://sandbox-api.corepro.io.customer/list", None, headers)
resp = httpConn.getresponse()
print resp


#print TestBase.Conn.apiKey,
#print TestBase.Conn.apiSecret,
#print TestBase.Conn.domainName
#c = Customer()
#Customer.list(c, connection=TestBase.Conn)
#print c.customerCount

#print cs
#ts = Customer.list(connection=TestBase.Conn)
#cs = Customer.listItems(0, 200, TestBase.Conn, TestBase.loggingObject)
