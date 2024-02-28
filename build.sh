pip install -r requirements.txt

pip install --upgrade tensorflow tensorflow-gpu tensorflow-tensorrt

cd ml_service

python3 manage.py migrate

python3 manage.py runserver
