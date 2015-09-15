# ChargeBee Nebri Webhooks

This app is intended for use in a NebriOS instance. Visit https://nebrios.com to sign up for free!

<h2>Requirements</h2>
This app requires the use of https://github.com/briem-bixly/nebrios-authentication.

<h2>Usage</h2>
Webhooks can be set up in ChargeBee on the Settings -> Webhook Settings page. The URL you enter depends on what event type you would like to listen to. However, it should look something like https://<strong>instance_name</strong>.nebrios.com/api/v1/chargebee_webhooks/<strong>chosen_endpoint</strong>. All endpoints require Basic Authentication.

<h2>Endpoints</h2>
- all_events: can be used for any event type
- customer_events: for use with customer events
- invoice_events: for use with invoice events
- card_events: for use with card events
- subscription_events: for use with subscription events
- transfer_events: for use with transfer events

<strong>NOTE</strong>: if an endpoint is used for webhooks with a different event type, the webhook will fail and no object will be created. All endpoints check to see if an object already exists with the sent event id. If one already exists, the webhook is ignored.

<h2>Models</h2>
Models are named after events. Currently supported events:
- customer
- invoice
- card
- subscription
- transfer

All models have the same fields:

- event_type: the type of event. i.e. if we get an event of `subscription_created`, this will be 'created'.
- date_received: the datetime that we received the webhook event.
- chargebee_id: the id that chargebee provides for the event. can be used for debouncing purposes.
- raw_data: the json representation of the full request body

Sample Request Body:
```
{
    "id": "ev_3Nl8ERLPElBCRU6",
    "occurred_at": 1341167306,
    "source": "admin_console",
    "object": "event",
    "content": {
        "subscription": {
            "id": "3Nl8ERLPElBCGl1",
            "plan_id": "basic",
            "plan_quantity": 1,
            "status": "future",
            "start_date": 1341772105,
            "trial_start": 1341772105,
            "trial_end": 1344450505,
            "created_at": 1341167305,
            "has_scheduled_changes": false,
            "object": "subscription",
            "addons": [{
                "id": "data_usage",
                "quantity": 1,
                "object": "addon"
            }],
            "due_invoices_count": 0
        },
        "customer": {
            "id": "3Nl8ERLPElBCGl1",
            "first_name": "Benjamin",
            "last_name": "Ross",
            "email": "Benjamin@test.com",
            "auto_collection": "on",
            "created_at": 1341167305,
            "object": "customer",
            "card_status": "valid",
            "payment_method": {
                "object": "payment_method",
                "type": "card",
                "reference_id": "3Nl8ERLPElBCGl1",
                "status": "valid"
            }
        },
        "card": {
            "customer_id": "3Nl8ERLPElBCGl1",
            "status": "valid",
            "gateway": "chargebee",
            "iin": "411111",
            "last4": "1111",
            "card_type": "visa",
            "expiry_month": 9,
            "expiry_year": 2012,
            "object": "card",
            "masked_number": "************1111"
        }
    },
    "event_type": "subscription_created",
    "webhook_status": "not_configured"
}
```

<h2>Authentication</h2>
All endpoints are protected with Basic Authentication. You must set up a username/password basic auth pair with a realm of 'chargebee' for these endpoints to work properly. See https://github.com/briem-bixly/nebrios-authentication for more information on setting up a username/password basic auth pair.
