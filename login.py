from twikit import Client

USERNAME = 'YOUR_USERNAME'
EMAIL = 'YOUR_EMAIL'
PASSWORD = 'YOUR_PASSWORD'

client = Client('en-US')

# Login to the service with provided user credentials
client.login(
    auth_info_1=USERNAME ,
    auth_info_2=EMAIL,
    password=PASSWORD
)

client.get_cookies()
client.save_cookies('cookies.json')
