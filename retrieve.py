import requests
import csv
import json
from auth import get_emsi_auth

comma = ","

response = get_emsi_auth()
print("response",response)
converted_response = json.loads(response)
# print("converted response", converted_response)
access_token = converted_response["access_token"]

# print("access token", access_token)

url = "https://emsiservices.com/skills/versions/latest/skills"

# querystring = {"q":".NET","typeIds":"ST1,ST2","fields":"id,name,type,infoUrl","limit":"5"}
# querystring = {"limit": "5"}

headers = {"Authorization": "Bearer " + access_token}

# print("headers", headers)

# skill_response = requests.request("GET", url, headers=headers, params=querystring)
skill_response = requests.request("GET", url, headers=headers)

# print("skill response", skill_response.text)

converted_skill_response = json.loads(str(skill_response.text))
# print("converted skill response", converted_skill_response)

with open("output.csv", "w") as outfile:

    # title_string = "Attribution Name, Attribution Text, TypeID, Type Name, SkillID, Skill Name, TagKey, TagValue, infoUrl, IsSoftware, IsLanguage, Skill Description, Description Source, Category ID, Category Name, Sub Category ID, Sub Category Name "
    title_string = "Attribution Name, Attribution Text,TypeID, Type Name, SkillID, Skill Name, infoUrl "
    # print(title_string)
    outfile.write(title_string)
    attributions = converted_skill_response["attributions"]
    for attrow in attributions:
        att_name = attrow["name"]
        att_text = attrow["text"]
    data = converted_skill_response["data"]
    for datarow in data:
        
        data_type_id = datarow["type"]["id"]
        data_type_name = datarow["type"]["name"]

        id = datarow["id"]
        name = datarow["name"]
 
        """ data_tags_key = datarow["tags"]["key"]
        data_tags_value = datarow["tags"]["value"] """

        infoUrl = datarow["infoUrl"]
        # isSoftware = datarow["isSoftware"]
        # isLanguage = datarow["isLanguage"]
        # description = datarow["description"]
        # descriptionSource = datarow["descriptionSource"]

        # category_id = datarow["category"]["id"]
        # category_name = datarow["category"]["name"]

        # subcategory_id = datarow["subcategory"]["id"]
        # subcategory_name = datarow["subcategory"]["name"]

        out_string = (
            att_name
            + comma
            + att_text
            + comma
            + data_type_id
            + comma
            + data_type_name
            + comma
            + id
            + comma
            + name
            + comma
            # + data_tags_key
            # + comma
            # + data_tags_value
            # + comma
            + infoUrl
            + comma
            # + isSoftware
            # + comma
            # + isLanguage
            # + comma
            # + description
            # + comma
            # + descriptionSource
            # + comma
            # + category_id
            # + comma
            # + category_name
            # + comma
            # + subcategory_id
            # + comma
            # + subcategory_name
        )
        # print(out_string)
        outfile.write("\n")
        outfile.write(out_string)
