


sudo -u postgres createuser --superuser threebee
sudo -u postgres createdb threebee --owner threebee --password
# IMPORTANT: Grant permission in /etc/postgresql/11/main/pg_hba.conf
