from jinbase import TestBase
from corepro.customer import Customer
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

#print TestBase.Conn.apiKey,
#print TestBase.Conn.apiSecret,
#print TestBase.Conn.domainName
c = Customer()
Customer.list(c, connection=TestBase.Conn)
print c.customerCount

#print cs
#ts = Customer.list(connection=TestBase.Conn)
#cs = Customer.listItems(0, 200, TestBase.Conn, TestBase.loggingObject)
