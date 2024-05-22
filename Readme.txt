/auth/users/
/api/api-token-auth/ (post)  
/api/booking/
/api/booking/<int:pk>
/api/menu-items/
/api/menu-items/<int:pk>
/restaurant/booking/tables/
/api/message/
python manage.py test   

optinal steps to setup pipenv and install mysqlclient:
================================================
python -m pip install django
pipenv --python `which python3` install

mysql
===========
pip install wheel
pip install pymysql
sudo /usr/local/mysql/support-files/mysql.server start