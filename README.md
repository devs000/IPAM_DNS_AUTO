# TP13 - Création d'un rôle Ansible `ipam_dns_role`

Ce projet consiste à créer un rôle Ansible pour gérer la réservation d'adresses IP et l'ajout de noms d'hôte dans un système IPAM (IP Address Management) et DNS (Domain Name System). 
- Le rôle est exécuté via un playbook Ansible.

## Prérequis

Avant d'exécuter le playbook, assurez-vous d'avoir les éléments suivants installés :

1. **Python 3** : Le projet utilise Python pour exécuter le serveur et les scripts.
2. **Ansible** : Installé pour exécuter le playbook.
3. **Flask** : Le serveur `server.py` utilise Flask pour simuler les API IPAM/DNS.
4. Nous avons ajouté les modules dans le repertoire Library en role 

Pour installer les dépendances, exécutez :

```sh
    python3 -m venv .venv
    source .venv/bin/activate
    pip install ansible flask
```

### Exécution du projet

1. **Démarrer le serveur IPAM/DNS :**

Le serveur server.py simule les API IPAM et DNS. Pour le démarrer, exécutez :

```sh
python3 server.py
```
- Le serveur écoutera sur http://127.0.0.1:8000.

2. **Exécuter le playbook Ansible :**

Le playbook playbook.yml exécute le rôle ipam_dns_role pour réserver des adresses IP et ajouter des noms d'hôte. Pour l'exécuter, utilisez la commande suivante :
```sh
ansible-playbook playbook.yml
```
- **Contenu du playbook :**

Le playbook définit une liste de noms d'hôte (hostnames);
exécute le rôle ipam_dns_role en localhost.

```yml
---
- name: Start IPAM and DNS servers
  hosts: localhost
  vars:
    hostnames:
      - host1.devops.com
      - host2.devops.com
      - host3.devops.com
      - host4.devops.com
      - host5.devops.com
      - host6.devops.com
      - host7.devops.com
      - host8.devops.com
      - host9.devops.com
      - host10.devops.com
  roles:
    - ipam_dns_role
```
3. **Tâches du rôle ipam_dns_role:**
Les tâches du rôle sont définies dans ipam_dns_role/tasks/main.yml. Elles incluent :

- **Créer une liste factice :**
Une liste de 10 éléments est générée pour itérer sur les réservations d'adresses IP.
- **Obtenir une IP libre :**
Une requête est envoyée à l'API IPAM pour récupérer une adresse IP disponible.
- **Réserver une IP et ajouter un nom d'hôte :**
L'adresse IP est réservée et associée à un nom d'hôte via l'API IPAM.
- **Enregistrer l'IP et le nom d'hôte dans le DNS :**
L'adresse IP et le nom d'hôte sont enregistrés dans le système DNS via une API.
- **Configurer l'accès :**
Une requête est envoyée pour gérer la creation username et password à la hostname




