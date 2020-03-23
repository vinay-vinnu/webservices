
import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# add python site packages, you can use virtualenvs also
site.addsitedir("c:/users/admin/appdata/local/programs/python/python37/lib/site-packages")

# Add the app's directory to the PYTHONPATH 
sys.path.append('C:/Users/admin/webservices') 
sys.path.append('C:/Users/admin/webservices/webservices')  

os.environ['DJANGO_SETTINGS_MODULE'] = 'webservices.settings' 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webservices.settings")  
 
application = get_wsgi_application()    