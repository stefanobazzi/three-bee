# Three-Bee

### DB Setup
Installazione DB:

    sudo apt-get install postgresql
    sudo apt-get install python-psycopg2
    sudo apt-get install libpq-dev

Setup:
    sudo -u postgres createuser --superuser threebee
    sudo -u postgres createdb threebee --owner threebee --password
    # IMPORTANT: Grant permission in /etc/postgresql/11/main/pg_hba.conf
  
### Installazione

    # creare il virutalenv
    pip install -r requirements.txt
    python mange.py migrate