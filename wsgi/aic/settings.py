import os

RSS_URL = 'http://finance.yahoo.com/news/?format=rss'
SECRET_KEY = "klasfiasdf12kCF(uL>ASJ123r5b129cfujxzl;kjashb124e12edljcv"

production = os.environ.get('OPENSHIFT_POSTGRESQL_DB_URL') is not None

if production:
    DB_URL = os.environ.get('OPENSHIFT_POSTGRESQL_DB_URL')
    DOMAIN = 'http://aic13lab2topic2-mobileworks.rhcloud.com'
    CROWD_DOMAIN = 'http://aic13lab2topic2-mobileworks.rhcloud.com'
else:
    DB_URL = 'postgresql://aic:aic@localhost/aic'
    DOMAIN = 'http://127.0.0.1:5000'
    CROWD_DOMAIN = 'http://127.0.0.1:5001'
