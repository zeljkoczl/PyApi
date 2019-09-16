#dependencies za REST i JSON
import requests
import json

#headers var
headers = {
    "X-Recharge-Access-Token": "abc123",
    "Accept":"application/json",
    "Content-Type":"application/json"
}

#POST endpoint za pravljenje novog korisnika
url = "https://api.rechargeapps.com/customers"

#JSON sa podacima za novog korisnika
data = {
  "email": "s2p22hy3bg623ib@payspun.com",
  "first_name": "Matthew",
  "last_name": "Smith",
  "billing_first_name": "Matthew",
  "billing_last_name": "Smith",
  "billing_address1": "3489  Diamond Street",
  "billing_zip": "68047",
  "billing_city": "Pender",
  "billing_province": "Nebraska",
  "billing_country": "United States",
  "billing_phone": "4029226120"
}

#POST zahtev prema API za pravljenje novog korisnika
result = requests.post(url, json.dumps(data), headers=headers)

#odgovor u JSON
res = result.json()

#var neophodne za pravljenje adrese a dobijene iz API odgovora
customer_id = res['customer']['id']

idstr = str(customer_id)
#POST endpoint za pravljenje nove adrese
url_add = "https://api.rechargeapps.com/customers/" + idstr + "/addresses"

#JSON sa podacima za novu adresu
data_add = {
    "address1": "3489  Diamond Street",
    "city": "Pender",
    "province": "Nebraska",
    "first_name": "Matthew",
    "last_name": "Smith",
    "zip": "68047",
    "phone": "4029226120",
    "country": "United States",
  }

#POST zahtev prema API za pravljenje nove adrese
result_add = requests.post(url_add, data=json.dumps(data_add), headers=headers)
res_a = result_add.json()

#var neophodne za pravljenje pretplate a dobijene iz API odgovora, na jednu adresu moguce je dodati samo jednu pretplatu na jedan proizvod
address_id = res_a['address']['id']

#POST endpoint za pravljenje nove pretplate
url_sub = "https://api.rechargeapps.com/subscriptions"

#JSON sa podacima za dodavanje pretplate
data_sub = {
  "customer_id": customer_id,
  "address_id": address_id, 
  "next_charge_scheduled_at": "2018-12-12T00:00:00",
  "product_title": "Beans",
  "price": "1",
  "quantity": "1",
  "shopify_variant_id": "3844892483", 
  "order_interval_unit": "week",
  "order_interval_frequency": "2",
  "charge_interval_frequency": "1"
}

#POST zahtev prema API za dodavanje nove pretplate
result_sub = requests.post(url_sub, data=json.dumps(data_sub), headers=headers) 
res_s = result_sub.json()

print(res_s)

sub_id = res_s['subscription']['id']

print(customer_id) #customer_id
print(address_id) #address_id
print(sub_id) #sub_id
