from groq import Groq

from schemas import FoodShop
import json
class GroqClient:
    def __init__(self):
        self.client = Groq(api_key="YOUR_API_KEY")  # Replace with your actual API key (https://platform.groq.ai/account/api-keys,don't worry its free)

def extract_food_shop(text: str) -> FoodShop:
    client = GroqClient().client
    response =  client.chat.completions.create(
        model="llama-3.3-70b-versatile",         
        max_tokens=1024,
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "extract_food_shop_data",
                    "description": "Extracts food shop data from a receipt",
                    "parameters": FoodShop.model_json_schema()
                }
            }
        ],
        tool_choice={"type": "function", 
                     "function": {"name": "extract_food_shop_data"}
                     },
        
        messages=[
            {"role": "user", 
             "content": f"Extract data from this receipt:\n\n{text}"
            }
        ]
    )
    tool_call = response.choices[0].message.tool_calls[0]
    args_dict = json.loads(tool_call.function.arguments)
    result = FoodShop(**args_dict)
    
    return result


if __name__ == "__main__":
    

    sample_text = """
    PT. Memex
    Telp: 08123456789
    Tanggal: 01/06/2019 12:22
    
    Ayam Geprek     2x   50.000    100.000
    Nasi Goreng     1x   30.000     30.000
    Nasi Goreng Spesial  1x  190.000  190.000
    """
    
    result = extract_food_shop(sample_text)
    print(result)