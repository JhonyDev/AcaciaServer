# M-PESA INTEGRATION 

> This is the module for integrating mpesa stk push.

Endpoint url is `<domain/api/mpesa-stk-push>`

Only the post method is allowed for this endpoint.

`POST` method example.

Example data expected:

    {
    "user_id": "1",
    "user_phone": "254746400709"
    }    
User id is the id of the user in the system
User phone is the phone number of the user without the +. Changing the format will cause an error.

### Response

Valid phone number and user id and a successful transaction returns a 200/201 code otherwise it will throw error check for any code greater than 299 response and throw error.

With a successfull push the user is marked as paid.

Transactions can be accessed by a get request to `<domain/api/transaction>`

This endpoint is filterable by user id, user phone, completed and purpose as shown:

`http://localhost:8000/api/transaction/?user_id=1&user_phone=&completed=&purpose=`

