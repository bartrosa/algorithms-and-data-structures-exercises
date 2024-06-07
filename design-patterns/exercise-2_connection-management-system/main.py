from api_factory import ApiFactory
from config import API_CONFIG

def main():
    print("Available APIs:")
    for api_name in API_CONFIG.keys():
        print(f"- {api_name}")
    
    chosen_api = input("Choose an API to connect (e.g. twitter, github): ").strip().lower()
    
    if chosen_api not in API_CONFIG:
        print("Invalid API choice. Exiting.")
        return
    
    api = ApiFactory.get_api(chosen_api)
    
    if api:
        print(f"Successfully connected to {chosen_api}.")
        api.perform_basic_operations()
    else:
        print("Failed to connect to the API.")

if __name__ == "__main__":
    main()
