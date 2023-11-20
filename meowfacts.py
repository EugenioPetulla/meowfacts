from cat.mad_hatter.decorators import tool
import requests


@tool(return_direct=True)
def meow_facts(input, cat):
    """
    Useful to respond with an interesting fact about cats.
    Input is None 
    """
    url = "https://meowfacts.herokuapp.com/"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and isinstance(data["data"], list) and len(data["data"]) > 0:
                return data["data"][0]
            else:
                return "No meow facts available"
        else:
            return f"Failed to fetch data. Status code: {response.status_code}"
    except requests.RequestException as e:
        return f"Error: {e}"