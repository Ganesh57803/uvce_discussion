# build_files.sh
pip install -r requirements.txt
# virtualenv env
# env/scripts/activate
python3.9 manage.py collectstatic
