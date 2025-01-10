from langchain_core.tools import Tool
from langflow.base.langchain_utilities.model import LCToolComponent
from langflow.inputs import IntInput, SecretStrInput
from langflow.schema import Data
import requests


class UsersAPIComponent(LCToolComponent):
    display_name = "Users API"
    description = "Get users by API."
    name = "UsersAPI"
    icon = "User"
    inputs = [
        IntInput(name="user_id", display_name="User ID", required=True),
    ]

    def _fetch_user_data(self, user_id: int) -> dict:
        """
        Fetch user data from JSONPlaceholder by user ID.
        """
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return {"error": f"User with ID {user_id} not found."}

    def run_model(self) -> Data:
        """
        Run the tool to fetch user data.
        """
        result = self._fetch_user_data(user_id=self.user_id)
        self.status = result
        return Data(data=result, text=str(result))

    def build_tool(self) -> Tool:
        """
        Build the LangChain Tool object.
        """
        return Tool(
            name="users_api",
            description="Fetch user details by user ID from JSONPlaceholder.",
            func=self.run_model,
        )
