# SNWT
Scanning Network &amp; Websites Tool

## Installation

```bash
git clone https://github.com/zteeed/SNWT.git
rm -rf /var/www/html && mkdir -p /var/www/html
mv SNWT/* /var/www/html
```

### networkscan

```bash
bash networkscan/install/install.sh
```

Configuration manuelle:
- Éditer /etc/apache2/apache2.conf et modifier `AllowOverride None` en `AllowOverride All` en dessous de `<Directory /var/www>` pour permettre aux fichiers `.htaccess` d'être éxécuté.
- Éditer pg_hba.conf (`find /etc -name pg_hba.conf`) et remplacer `local  all postgres  peer` en `local  all postgres  trust`
- Éditer la crontab: `30 4 * * * cd /var/www/html/networkscan; python3 main.py`

Schéma de la base de donnée:


### revproxy

```bash
bash revproxy/install/install.sh
```

Configuration manuelle:
- Éditer pg_hba.conf (`find /etc -name pg_hba.conf`) pour permettre la connection en remote: `host  all  all  A.B.C.D/E  md5` où A.B.C.D/E correspond à un sous réseau.
- Éditer postgresql.conf (`find /etc -name postgresql.conf`) pour permettre la connexion en remote: `listen_addresses = '*'`
- Éditer le fichier `networkscan/data.csv` à partir du template `networscan/data.csv.example` pour permettre au script `networkscan/main.py` d'explorer les sous réseaux indiqués:
```csv
catégorie.name;IP/mask;description
test1;10.10.10.0/24;commentaire2
test2;192.100.45.128/26;commentaire2
```
- Éditer la crontab: `30 * * * * cd /root/SNWT/revproxy; python3 main.py`

Schéma de la base de donnée:

### postgresql

Configuration manuelle:
- Pour vous faciliter la tâche vous disposez d'un fichier `export.sql` dans le dossier `install/data` afin de réatblir la base de donnée vierge en cas de problème, même si les scripts python gèrent la reconstruction de la base de donnée.
- `sudo -u postgres psql`
```sql
CREATE ROLE respoweb WITH LOGIN;
\password respoweb
CREATE DATABASE dbname
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO respoweb;
```
- Si vous rencontrez l'erreur `new encoding (UTF8) is incompatible with the encoding of the template database
(SQL_ASCII)`:

```SQL
UPDATE pg_database SET datistemplate = FALSE WHERE datname = 'template1';
DROP DATABASE template1;
CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UNICODE';
UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'template1';
\c template1
VACUUM FREEZE;
```

### fonctionnalités à prévoir

- Récupérer via l'API ADH6 les données adhérents en fonction de l'IP
- Récupérer le noms des subdirectory du server web pour indexer les pages cachées
