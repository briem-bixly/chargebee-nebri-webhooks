from nebrios_authentication_lib import basic_auth_required
from chargebeewebhookmodels import Customer, Subscription, Invoice, Payment, Card
import json


@basic_auth_required(realm='chargebee')
def all_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['event_type'].split('_')[0]
    if event_type == 'customer':
        try:
            event = Customer.get(chargebee_id=event_data['id'])
            return {}
        except Process.DoesNotExist:
            event = Customer()
    elif event_type == 'subscription':
        try:
            event = Subscription.get(chargebee_id=event_data['id'])
            return {}
        except Process.DoesNotExist:
            event = Subscription()
    elif event_type == 'invoice':
        try:
            event = Invoice.get(chargebee_id=event_data['id'])
            return {}
        except Process.DoesNotExist:
            event = Invoice()
    elif event_type == 'payment':
        try:
            event = Payment.get(chargebee_id=event_data['id'])
            return {}
        except Process.DoesNotExist:
            event = Payment()
    elif event_type == 'card':
        try:
            event = Card.get(chargebee_id=event_data['id'])
            return {}
        except Process.DoesNotExist:
            event = Card()
    else:
        return HttpResponseBadRequest

    event.event_type = event_data['event_type'].split('_', 1)[1]
    event.chargebee_id = event_data['id']
    event.date_received = datetime.now()
    event.raw_data = event_data
    event.save()


@basic_auth_required(realm='chargebee')
def customer_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['event_type'].split('_')[0]
    if event_type != 'customer':
        return HttpResponseBadRequest
    try:
        event = Customer.get(chargebee_id=event_data['id'])
        return {}
    except Process.DoesNotExist:
        event = Customer(
            event_type=event_data['event_type'].split('_', 1)[1],
            chargebee_id=event_data['id'],
            date_received=datetime.now(),
            raw_data=event_data
        )
        event.save()


@basic_auth_required(realm='chargebee')
def subscription_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['event_type'].split('_')[0]
    if event_type != 'subscription':
        return HttpResponseBadRequest
    try:
        event = Subscription.get(chargebee_id=event_data['id'])
        return {}
    except Process.DoesNotExist:
        event = Subscription(
            event_type=event_data['event_type'].split('_', 1)[1],
            chargebee_id=event_data['id'],
            date_received=datetime.now(),
            raw_data=event_data
        )
        event.save()


@basic_auth_required(realm='chargebee')
def invoice_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['event_type'].split('_')[0]
    if event_type != 'invoice':
        return HttpResponseBadRequest
    try:
        event = Invoice.get(chargebee_id=event_data['id'])
        return {}
    except Process.DoesNotExist:
        event = Invoice(
            event_type=event_data['event_type'].split('_', 1)[1],
            chargebee_id=event_data['id'],
            date_received=datetime.now(),
            raw_data=event_data
        )
        event.save()


@basic_auth_required(realm='chargebee')
def payment_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['event_type'].split('_')[0]
    if event_type != 'payment':
        return HttpResponseBadRequest
    try:
        event = Payment.get(chargebee_id=event_data['id'])
        return {}
    except Process.DoesNotExist:
        event = Payment(
            event_type=event_data['event_type'].split('_', 1)[1],
            chargebee_id=event_data['id'],
            date_received=datetime.now(),
            raw_data=event_data
        )
        event.save()


@basic_auth_required(realm='chargebee')
def card_events(request):
    try:
        event_data = json.loads(request.BODY)
    except:
        event_data = request.BODY
    event_type = event_data['event_type'].split('_')[0]
    if event_type != 'card':
        return HttpResponseBadRequest
    try:
        event = Card.get(chargebee_id=event_data['id'])
        return {}
    except Process.DoesNotExist:
        event = Card(
            event_type=event_data['event_type'].split('_', 1)[1],
            chargebee_id=event_data['id'],
            date_received=datetime.now(),
            raw_data=event_data
        )
        event.save()
