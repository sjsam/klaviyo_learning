import os
from dotenv import load_dotenv
from klaviyo_api import KlaviyoAPI

# Get the path of the current directory
current_directory = os.path.dirname(__file__)
# Read the environment file from ".env.local" one level up
loaded = load_dotenv(dotenv_path=f"{current_directory}/../env.local")
if not loaded:
    raise Exception("Failed to load environment file")
klaviyo_private_key = os.environ.get("KLAVIYO_PRIVATE_KEY")
klaviyo_public_key = os.environ.get("KLAVIYO_PUBLIC_KEY")

# Initialize the Klaviyo API
klaviyo = KlaviyoAPI(klaviyo_private_key, max_delay=60, max_retries=3)
# Get all lists
lists = klaviyo.Lists.get_lists()
for lst in lists.data:
    print(lst.id)
    print(lst.attributes.name)
    print("--------------------")

# Get a specific list using filter
print("Get a specific list")
lists = klaviyo.Lists.get_lists(filter="equals(name,'Wine Tours')")
list_id = ""
for lst in lists.data:
    list_id = lst.id
    print(lst.id)
    print(lst.attributes.name)
    print("--------------------")

# Get the profiles in a list
list_profiles = klaviyo.Lists.get_list_profiles(list_id)
print("Profiles in the list")
print("--------------------")
for profile in list_profiles.data:
    print("ID : ", profile.id)
    print("Email : ", profile.attributes.email)

print("--------------------")
print("Total Profiles : ", len(list_profiles.data))
