# vana-banguat
RESTful API on Python to access Banguats' information about change rate between types of currency.

# 1. Requirements (anaconda environment)
conda install -c anaconda pandas
pip install -U Flask
pip install flask-restful

# 2. Run API
python api.py

# 3. Test API
- Single date
http://localhost:5000/items?date=2021-02-19&currency=USD

-Range of dates
http://localhost:5000/items?start_date=2021-02-14&end_date=2021-02-17&currency=USD