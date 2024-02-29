pip install -r requirements.txt

pip install tensorrt
!pip install tensorflow-gpu==2.8.0

cd ml_service

python3 manage.py migrate

python3 manage.py runserver
