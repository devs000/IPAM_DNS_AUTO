from ansible.module_utils.basic import AnsibleModule
import requests
import json

def main():
    module_args = dict(
        api_url=dict(type="str", required=True),
        ip=dict(type="str", required=True),
        hostname=dict(type="str", required=True)
    )

    module = AnsibleModule(argument_spec=module_args)
    api_url = module.params["api_url"]
    ip = module.params["ip"]
    hostname = module.params["hostname"]

    data = {
        "ip": ip,
        "hostname": hostname
    }

    try:
        response = requests.post(f"{api_url}/dns/reserve_dns", json=data)
        response.raise_for_status()
        data = response.json()
        module.exit_json(changed=True, response=data)

    except requests.exceptions.RequestException as e:
        module.fail_json(msg=f"Erreur de connexion à l'API : {e}", status_code=500)
    except requests.exceptions.HTTPError as e:
        module.fail_json(msg=f"Erreur HTTP : {e}", status_code=response.status_code, response_text=response.text)    
    except Exception as e:
        module.fail_json(msg=f"Une erreur inattendue s'est produite : {e}", status_code=500)

if __name__ == "__main__":
    main()