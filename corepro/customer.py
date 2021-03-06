__author__ = 'socialmoneydev'

from utils.requestor import Requestor
from models.jsonBase import JsonBase
from account import Account
from externalaccount import ExternalAccount
from models.customeraddress import CustomerAddress
from models.customerphone import CustomerPhone
from models.customeridonly import CustomerIdOnly
from models.customerverifyrequest import CustomerVerifyRequest

class Customer(JsonBase):

    def __init__(self):
        self.requestId = None
        self.customerCount = None
        self.customerId = None
        self.firstName = None
        self.middleName = None
        self.lastName = None
        self.birthDate = None
        self.gender = None
        self.culture = None
        self.tag = None
        self.status = None
        self.createdDate = None
        self.taxId = None
        self.driversLicenseNumber = None
        self.driversLicenseState = None
        self.driversLicenseExpirationDate = None
        self.passportNumber = None
        self.passportCountry = None
        self.emailAddress = None
        self.isActive = None
        self.isLocked = None
        self.lockedDate = None
        self.lockedReason = None
        self.deceasedDate = None
        self.isSubjectToBackupWithholding = None
        self.isOptedInToBankCommunication = None
        self.isDocumentsAccepted = None
        self.phones = []
        self.addresses = []
        self.accounts = []
        self.externalAccounts = []

    def fromJson(self, json, classDefs):
        classDefs = classDefs or dict()
        classDefs['phones'] = CustomerPhone
        classDefs['addresses'] = CustomerAddress
        classDefs['accounts'] = Account
        classDefs['externalAccounts'] = ExternalAccount
        return super(Customer, self).fromJson(json, classDefs)

    @staticmethod
    def getItem(customerId, connection = None, loggingObject = None):
        c = Customer()
        c.customerId = customerId
        return c.get(connection, loggingObject)

    def get(self, connection = None, loggingObject = None):
        return Requestor().get("/customer/get/{0}".format(self.customerId), Customer, connection, loggingObject)

    @staticmethod
    def getItemByTag(tag, connection = None, loggingObject = None):
        c = Customer()
        c.tag = tag
        return c.getByTag(connection, loggingObject)

    def getByTag(self, connection = None, loggingObject = None):
        return Requestor().get("/customer/getbytag/{0}".format(Requestor.escape(self.tag)), Customer, connection, loggingObject)

    @staticmethod
    def listItems(pageNumber = 0, pageSize = 200, connection = None, loggingObject = None):
        return Customer().list(pageNumber, pageSize, connection, loggingObject)

    def list(self, pageNumber = 0, pageSize = 200, connection = None, loggingObject = None):
        return Requestor().get("/customer/list", Customer, connection, loggingObject)

    def create(self, connection = None, loggingObject = None):
        cid = Requestor().post("/customer/create", CustomerIdOnly, self, connection, loggingObject)
        return cid.customerId

    def initiate(self, connection = None, loggingObject = None):
        return Requestor().post("/customer/initiate", CustomerIdOnly, self, connection, loggingObject)

    def verify(self, verificationId, answers, connection = None, loggingObject = None):
        cvr = CustomerVerifyRequest()
        cvr.verificationId = verificationId
        cvr.answers = answers
        return cvr.verify(connection, loggingObject)

    def update(self, connection = None, loggingObject = None):
        cid = Requestor().post("/customer/update", CustomerIdOnly, self, connection, loggingObject)
        return cid.customerId

    def deactivate(self, connection = None, loggingObject = None):
        cid = Requestor().post("/customer/deactivate", CustomerIdOnly, self, connection, loggingObject)
        return cid.customerId

    def search(self, pageNumber = 0, pageSize = 200, connection = None, loggingObject = None):
        return Requestor().post("/customer/search/?pageNumber={0}&pageSize={1}".format(pageNumber, pageSize), Customer, self, connection, loggingObject)