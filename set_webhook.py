import requests

# Replace these with your own bot token and domain
bot_token = '7926189230:AAFcdMleY25JBfrdRIxvpf9EGDBFQiM-l6A'
webhook_url = 'http://t.me/easylendpc_bot'  # The URL where your Django app is running

# Set the webhook
response = requests.get(f'https://api.telegram.org/bot{bot_token}/setWebhook?url={webhook_url}')

print(response.json())  # Check the response to ensure the webhook is set
