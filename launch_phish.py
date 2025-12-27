import requests
import time
import urllib3
urllib3.disable_warnings()
API_KEY = "API KEY DE GOPHISH"
BASE_URL = "https://127.0.0.1:3333"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
# Création campagne 
campaign_data = {
    "name": "compain_EH",
    "template": {"name": "EH template"},
    "page": {"name": "EH_landing_page"},
    "smtp": {"name": "MailHog"},
    "groups": [{"name": "groupe EH"}],
    "url":"http://127.0.0.1"
}
response = requests.post(
    f"{BASE_URL}/api/campaigns/",
    json=campaign_data,
    headers=headers,
    verify=False
)
if response.status_code != 201:
    print("Erreur création campagne")
    print(response.text)
    exit()
campaign_id = response.json()["id"]
print(f"Campagne créée | ID = {campaign_id}")
CLICK_STATUSES = ["Clicked Link", "Submitted Data"]
while True:
    r = requests.get(
        f"{BASE_URL}/api/campaigns/{campaign_id}",
        headers=headers,
        verify=False
    )
    results = r.json()["results"]
    total = len(results)
    clicks = sum(1 for r in results if r["status"] in CLICK_STATUSES)
    taux = (clicks / total * 100) if total > 0 else 0
    print("────────────")
    print(f" Total : {total}")
    print(f"Clicks : {clicks}")
    print(f"Taux : {taux:.2f}%")
    print("────────────\n")
    time.sleep(5)
