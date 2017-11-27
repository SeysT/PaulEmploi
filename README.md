# Paul Emploi

## Installer le projet

### Pré-requis

Avant toute opération, il faut avoir installer les dépendances suivantes :
- Python 3.6+ : https://www.python.org/
- NodeJS 8.9.1+ et npm 5.5.1+ : https://nodejs.org/

### Installation

#### 1. Cloner le projet :

Pour commencer il faut cloner le projet :

```sh
$ git clone git@gitlab.centralesupelec.fr:2014legerm/paul-emploi.git
$ cd paul-emploi
```

#### 2. Setup le projet VueJS :

Pour configurer correctement le client il faut d'abord installer de manière globale Vue et Vue-cli

```sh
$ npm install --global vue
$ npm install --global vue-cli
```

Il faut ensuite initialiser le projet :

```sh
$ cd pierre-client
$ npm install
```

#### 3. Setup le projet Django

Pour configurer le projet Django, il faut d'abord setup un environnement virtuel. Si virtualenv n'est pas installé :

```sh
$ pip install virtualenv
```

Il faut ensuite créer l'environnement virtuel dans le projet jacques_serveur :

```sh
$ cd jacques_serveur
$ virtualenv env -p "your_python_path"
```

Il faut ensuite activer l'environnement virtuel. Sous Linux :

```sh
$ source ./env/bin/activate
```

Et sous Windows :

```sh
$ ./env/Scripts/activate
```

Pour installer les requirements :

```sh
$ pip install -r requirements.txt
```

### Faire tourner les différents serveurs

#### 1. Serveur de développement frontend

Pour faire tourner le serveur de développement :

```sh
$ cd pierre-client
$ npm run dev
```

#### 2. Serveur backend

Pour faire tourner le serveur Django :

```sh
$ cd jacques_serveur
$ python manage.py runserver
```