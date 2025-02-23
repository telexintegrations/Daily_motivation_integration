# Daily Motivation Bot for Telex  
**Type:** Interval Integration  

## Description  
The **Daily Motivation Bot** sends motivational quotes daily to inspire and uplift team members, helping to maintain a positive and productive work environment. The bot automatically fetches and delivers a new motivational quote each day, encouraging teamwork and boosting morale.  

## Key Features  
- **Daily Motivational Quotes:** Automatically sends a new motivational quote every day.  
- **Inspiration Boost:** Helps to uplift and inspire team members to stay positive and productive.  
- **Automated Scheduling:** Quotes are delivered at a set interval, ensuring consistent motivation.  
- **Easy Integration:** Seamlessly integrates with Telex channels for hassle-free deployment.  
- **Customizable Settings:** Allows customization of delivery time intervals to fit team schedules.  

## Integration JSON  
```json
{
    "data": {
        "date": {
            "created_at": "2025-02-17",
            "updated_at": "2025-02-17"
        },
        "descriptions": {
            "app_name": "Daily Motivation Bot",
            "app_description": "Daily Motivation Bot\nSends motivational quotes daily to inspire and uplift team members, helping to maintain a positive and productive work environment. The bot automatically fetches and delivers a new motivational quote each day, encouraging teamwork and boosting morale.",
            "app_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSowU4UV3Sncxajn1Smd8UMnTaN9Mm6mtk5NA&usqp=CAU",
            "app_url": "https://daily-motivation-integration.onrender.com",
            "background_color": "#fff"
        },
        "is_active": true,
        "integration_type": "interval",
        "key_features": [
            "Daily Motivational Quotes: Automatically sends a new motivational quote every day.",
            "Inspiration Boost: Helps to uplift and inspire team members to stay positive and productive.",
            "Automated Scheduling: Quotes are delivered at a set interval ensuring consistent motivation.",
            "Easy Integration: Seamlessly integrates with Telex channels for hassle-free deployment.\nCustomizable Settings: Allows customization of delivery time intervals to fit team schedules."
        ],
        "integration_category": "Communication & Collaboration",
        "author": "jeffmaine",
        "settings": [
            {
                "label": "time interval",
                "type": "text",
                "required": true,
                "default": "* * * * *"
            }
        ],
        "target_url": "",
        "tick_url": "https://daily-motivation-integration.onrender.com/tick"
    }
}
```
## Prerequisites  
- **Python 3.9+**  
- **FastAPI**  
- **HTTPX**  
- **Telex account and channel**  

## Installation  
### 1. Clone the Repository  
```sh
git clone git@github.com:telexintegrations/telex-daily-motivation-integration.git
cd telex-daily-motivation-integration
```

### 2. Create a Virtual Environment 
```sh
python3 -m venv venv
source venv/bin/activate  
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage  
### 1. Run the Application Locally  
```sh
uvicorn src:app --reload
```

### 2. Test locally
```sh
pytest -v
```


### 3. Access the Integration JSON
Open your browser and navigate to: 
```sh
http://127.0.0.1:8000/integration.json
```

check for the json details

## Deployment

The integration is deployed on render.com and can be accessed here:  
[Live Deployment](https://daily-motivation-integration.onrender.com)

### 3. Telex Integration
- Add the integration JSON URL in your Telex organization.
- Configure the time interval in the settings (e.g., `0 9 * * *` for 9am every day).


# Testing the Daily Motivation Bot Integration on Telex

This guide provides a step-by-step approach to testing the **Daily Motivation Bot** integration within the Telex platform. The bot is designed to deliver a motivational quote to your Telex channel once daily.

## Prerequisites

Before proceeding, ensure you have the following:

- **Telex Account**: Access to an active Telex account.
- **Telex Channel**: A channel within Telex where the bot will post daily messages.
- **Integration URL**: The publicly accessible URL of your deployed Daily Motivation Bot.

## Steps to Test the Integration

### 1. Deploy the Daily Motivation Bot

Ensure your Daily Motivation Bot is deployed and accessible via a public URL /integraation.json . This deployment is crucial for Telex to communicate with your bot.

### 2. Add the Integration to Telex

1. **Log in to Telex**: Access your Telex account with your credentials.
2. **Navigate to Integrations**: From the dashboard, click on the "Integrations" tab.
3. **Add New Integration**:
   - Click on "Add Integration."
   - paste the /integratiion.json endpoint url
   - Save the integration.

### 3. Configure the Integration

1. **Set the Time Interval**:
   - Access the settings of the "Daily Motivation Bot" integration.
   - Specify the time interval using cron syntax to determine when the bot should send messages. For example, to send a message every day at 9:00 AM, use `0 9 * * *`.
   - Save the configuration.

### 4. Verify the Integration

To ensure the bot functions as expected, you can perform a manual test:

1. **Trigger the Bot Manually**:
   - Access your deployed bot's server or hosting environment.
   - Manually invoke the function responsible for sending the motivational quote. This action simulates the scheduled task and allows you to verify the bot's functionality.

2. **Check the Telex Channel**:
   - Navigate to the Telex channel designated to receive the bot's messages.
   - Confirm that the motivational quote has been posted successfully.

### 5. Monitor Scheduled Messages

After verification, allow the bot to operate on its scheduled interval. Ensure that the bot posts a new motivational quote at the specified time each day.

## Troubleshooting

- **No Message Posted**: If the bot doesn't post a message:
  - Verify that the bot's server is running without errors.
  - Ensure the Integration URL is correct and publicly accessible.
  - Check the cron syntax in the integration settings for accuracy.

- **Incorrect Posting Time**: If messages are posted at unexpected times:
  - Confirm that the cron expression matches the desired schedule.
  - Ensure the server's timezone aligns with your intended posting times.

By following this guide, you can effectively test and validate the Daily Motivation Bot integration within your Telex environment, ensuring consistent and timely delivery of motivational content to your team.


## Screenshots
![alt text](<Screenshot 2025-02-17 at 20.11.27.png>)