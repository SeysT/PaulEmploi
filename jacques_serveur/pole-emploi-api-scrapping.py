from requests import post
import time

POLE_EMPLOI_API_TIMEOUT = 1.2
POLE_EMPLOI_TOKEN_URL = 'https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=%2Fpartenaire'
POLE_EMPLOI_SEARCH_URL = 'https://api.emploi-store.fr/partenaire/offresdemploi/v1/rechercheroffres'
POLE_EMPLOI_CLIENT_ID = 'PAR_paulemploiletinderdescand_564ca946d246c8de2309f7967d0fd1576d8f1fe8af69f0e82f0c45e54156e82f'
POLE_EMPLOI_CLIENT_SECRET = '7dd3b6f9d6ac3e33b331e71ae3a675189cbe8fec4d572a15cdad467a7e043f86'
POLE_EMPLOI_SCOPE = 'application_PAR_paulemploiletinderdescand_564ca946d246c8de2309f7967d0fd1576d8f1fe8af69f0e82f0c45e54156e82f api_offresdemploiv1 o2dsoffre'

POLE_EMPLOI_SEARCH_KEYWORD = 'informatique'
RESULTS_PER_PAGE = 20
offers_list = []

if __name__ == '__main__':

    # getting a token
    auth_url = POLE_EMPLOI_TOKEN_URL
    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': POLE_EMPLOI_CLIENT_ID,
        'client_secret': POLE_EMPLOI_CLIENT_SECRET,
        'scope': POLE_EMPLOI_SCOPE
    }
    auth_header = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    auth_req = post(auth_url, data=auth_data, headers=auth_header)
    token = auth_req.json()['access_token']

    # first request to know the number of results
    url = 'https://api.emploi-store.fr/partenaire/offresdemploi/v1/rechercheroffres'
    header = {
        'Authorization': 'Bearer {}'.format(token),
        'Content-Type': 'application/json'
    }
    data = {
        'technicalParameters': {
            'page': 1,
            'per_page': RESULTS_PER_PAGE,
            'sort': 1
        },
        'criterias': {
            'keywords': POLE_EMPLOI_SEARCH_KEYWORD
        }
    }
    first_offer = post(url, json=data, headers=header)
    tot_results = first_offer.json()['technicalParameters']['totalNumber']
    tot_pages = int(tot_results / RESULTS_PER_PAGE)

    # other request to get all the offers
    for page_number in range(1, tot_pages):

        url = POLE_EMPLOI_SEARCH_URL
        header = {
            'Authorization': 'Bearer {}'.format(token),
            'Content-Type': 'application/json'
        }
        data = {
            'technicalParameters': {
                'page': page_number,
                'per_page': 10,
                'sort': 1
            },
            'criterias': {
                'keywords': POLE_EMPLOI_SEARCH_KEYWORD
            }
        }
        offers_received = post(url, json=data, headers=header)

        for offer in range(len(offers_received.json()['results'])):
            offers_list.append(offer)
        print("Nombre d'offres obtenues : ", len(offers_list))
        time.sleep(POLE_EMPLOI_API_TIMEOUT)
