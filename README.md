### Créer et configurer l'environnement virtuel sous Windows :

pip install virtualenv
cd "project_path"
virtualenv env -p "python_path"
./env/Scripts/activate
pip install -r requirements.txt

### Créer et configure l'environnement virtuel sous Linux :

pip install virtualenv
cd "project_path"
virtualenv env -p "python_path"
source ./env/bin/activate
pip install -r requirements.t