import requests

def get_emsi_auth():

    url = "https://auth.emsicloud.com/connect/token"

    with open("emsi_creds.txt", "r") as credfile:
        for line in credfile:
            if ((line.split(":"))[0]).strip() == "Client ID" :
                client_id = ((line.split(":"))[1]).strip()
            
            if ((line.split(":"))[0]).strip() == "Secret" :
                secret = ((line.split(":"))[1]).strip()


            if ((line.split(":"))[0]).strip() == "Scope" :
                scope= ((line.split(":"))[1]).strip()
    
    payload = "client_id="+client_id+"&client_secret="+secret+"&grant_type=client_credentials&scope="+scope

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)

    return(response.text)
