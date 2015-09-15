from nebriosmodels import NebriOSModel, NebriOSField, NebriOSReference


class Customer(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    chargebee_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Subscription(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    chargebee_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Invoice(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    chargebee_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Payment(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    chargebee_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)


class Card(NebriOSModel):
    event_type = NebriOSField(required=True)
    date_received = NebriOSField(required=True)
    chargebee_id = NebriOSField(required=True)
    raw_data = NebriOSField(required=True)
