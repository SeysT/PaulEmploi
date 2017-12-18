from django.core.management.base import BaseCommand
from requests import post
from time import sleep

from api.models.offer import Offer, Degree, Skill, Language, Contract, Location, Company

POLE_EMPLOI_API_TIMEOUT = 1.2
POLE_EMPLOI_TOKEN_URL = 'https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=%2Fpartenaire'
POLE_EMPLOI_SEARCH_URL = 'https://api.emploi-store.fr/partenaire/offresdemploi/v1/rechercheroffres'
POLE_EMPLOI_CLIENT_ID = 'PAR_paulemploiletinderdescand_564ca946d246c8de2309f7967d0fd1576d8f1fe8af69f0e82f0c45e54156e82f'
POLE_EMPLOI_CLIENT_SECRET = '7dd3b6f9d6ac3e33b331e71ae3a675189cbe8fec4d572a15cdad467a7e043f86'
POLE_EMPLOI_SCOPE = 'application_PAR_paulemploiletinderdescand_564ca946d246c8de2309f7967d0fd1576d8f1fe8af69f0e82f0c45e54156e82f api_offresdemploiv1 o2dsoffre'

POLE_EMPLOI_SEARCH_KEYWORD = 'programmation'
RESULTS_PER_PAGE = 20


class Command(BaseCommand):
    help = 'Run this command to scrap the data from the Pole Emploi API and storing the result in the database'

    def __init__(self):
        super().__init__()
        self.token = None
        self.tot_pages = None

    def handle(self, *args, **options):
        self.token = self.get_token()
        self.tot_pages = self.get_pages_count()
        self.populate_db()

    def get_token(self):
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
        return auth_req.json()['access_token']

    def get_pages_count(self):

        # first request to know the number of results
        url = POLE_EMPLOI_SEARCH_URL
        header = {
            'Authorization': 'Bearer {}'.format(self.token),
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
        print("Nombre total d'offres : ", tot_results)
        return tot_pages

    def populate_db(self):

        # other request to get all the offers
        for page_number in range(1, self.tot_pages):
            # for page_number in range(1):

            url = POLE_EMPLOI_SEARCH_URL
            header = {
                'Authorization': 'Bearer {}'.format(self.token),
                'Content-Type': 'application/json'
            }
            data = {
                'technicalParameters': {
                    'page': page_number,
                    'per_page': RESULTS_PER_PAGE,
                    'sort': 1
                },
                'criterias': {
                    'keywords': POLE_EMPLOI_SEARCH_KEYWORD
                }
            }
            offers_received = post(url, json=data, headers=header)
            # print(offers_received.json()['results'])

            for offer in offers_received.json()['results']:

                # check if the different degree, skill ... exists, otherwise create it
                # degre, exists = Degree.get_or_create(name=offer[''])

                # create the offer in the database
                # Offer.objects.create(
                #     title=offer['title'],
                #     min_salary=offer['minSalary'],
                #     max_salary=offer['maxSalary'],
                #     weekly_work_time=offer['weeklyWorkTime']
                # )
                pass

            sleep(POLE_EMPLOI_API_TIMEOUT)
