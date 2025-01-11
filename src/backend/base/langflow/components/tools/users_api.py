from langchain_core.tools import Tool
from langflow.inputs import IntInput, SecretStrInput
# from langflow.schema import Data
from langflow.io import DropdownInput, MessageInput, MessageTextInput
from langflow.template import Output
from langflow.custom import Component
from langflow.schema import Data, Message
import json

import requests


class UsersAPIComponent(Component):
    display_name = "Users API"
    description = "Get user information from API by ID."
    name = "UsersAPI"
    icon = "User"

    inputs = [
        MessageTextInput(
            name="given_user_id",
            display_name="User Id",
            info="A given user id.",
        ),
    ]

    outputs = [
        Output(name="user_information", display_name="User Information", method="fetch_user_data"),    
    ] 

    def fetch_user_data(self) -> Message:        
        """
        Fetch user data from JSONPlaceholder by user ID.
        """
        user_id = self.given_user_id

        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        response = requests.get(url)
        data = response.json()
        result = json.dumps(data)

        return result
   