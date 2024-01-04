# Weather Alert Script

This script checks the weather forecast for a specific location and sends an SMS alert if it's going to rain.

## Requirements

- Python 3
- `requests` library
- `twilio` library
- `python-dotenv` library

## Setup

1. Clone this repository.
2. Install the required Python libraries using pip:

    ```bash
    pip install requests twilio python-dotenv
    ```

3. Create a `.env` file in the same directory as your script. Inside this file, you'll need to include your OpenWeatherMap API key, Twilio account SID, and Twilio auth token:

    ```env
    API_KEY=your_openweathermap_api_key
    ACCOUNT_SID=your_twilio_account_sid
    AUTH_TOKEN=your_twilio_auth_token
    ```

    Replace `your_openweathermap_api_key`, `your_twilio_account_sid`, and `your_twilio_auth_token` with your actual keys.

## Usage

Run the script with Python:

```bash
python weather_alert.py
```
If rain is forecasted in the next four data points from the OpenWeatherMap API, the script will send an SMS alert to the specified phone number.

## Note
Please make sure to update your number.
