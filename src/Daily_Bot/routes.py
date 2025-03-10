import asyncio
from fastapi import APIRouter, Request, BackgroundTasks, HTTPException, status
import httpx
from .schemas import MonitorPayload 
from datetime import datetime, timedelta


bot_router = APIRouter()


@bot_router.get("/integration.json", status_code=status.HTTP_200_OK)
def get_integration_json(request: Request):
    base_url = str(request.base_url).rstrip("/")
    return {
        "data": {
            "date": {
                "created_at": "2025-02-17",
                "updated_at": "2025-02-17"
            },
            "descriptions": {
                "app_name": "Daily Motivation Bot",
                "app_description": "Daily Motivation Bot\nSends motivational quotes daily to inspire and uplift team members, helping to maintain a positive and productive work environment. The bot automatically fetches and delivers a new motivational quote each day, encouraging teamwork and boosting morale.",
                "app_logo": "https://cdn-fkmoj.nitrocdn.com/xvpOGZRTxJUhXKufpOYIruQcRqtvAAQX/assets/images/optimized/rev-4e1f421/media.briantracy.com/blog/wp-content/uploads/2024/01/23111358/Quote-1.png",
                "app_url": f"{base_url}",
                "background_color": "#fff"
            },
            "is_active": True,
            "integration_type": "interval",
            "key_features": [
                "Daily Motivational Quotes: Automatically sends a new motivational quote every day.",
                "Inspiration Boost: Helps to uplift and inspire team members to stay positive and productive.",
                "Automated Scheduling: Quotes are delivered at a set interval ensuring consistent motivation.",
                "Easy Integration: Seamlessly integrates with Telex channels for hassle-free deployment.\nCustomizable Settings: Allows customization of delivery time intervals to fit team schedules."
            ],
            "integration_category": "Communication & Collaboration",
            "author": "jeff maine",
            "settings": [
                {
                    "label": "interval",
                    "type": "text",
                    "required": True,
                    "default": "* * * * *"
                }
            ],
            "target_url": "",
            "tick_url": f"{base_url}/tick"
        }
    }

cached_quote = None
cache_expiry = None
lock = asyncio.Lock()

async def get_motivation():
    global cached_quote, cache_expiry
    print("cached_quote:", cached_quote)

    async with lock:
        if cached_quote and cache_expiry and datetime.now() < cache_expiry:
            return cached_quote 

        quote_url = "https://zenquotes.io/api/random/motivational"
        try:
            async with httpx.AsyncClient() as client:
                result = await client.get(quote_url)
                print("api quote hit")
                if result.status_code == 200:
                    quote_data: dict = result.json()[0]
                    quote = quote_data.get("q", "Stay positive and keep moving forward.")
                    author = quote_data.get("a", "Unknown")
                    cached_quote = f"{quote} \n by {author}"
                    cache_expiry = datetime.now() + timedelta(minutes=1)

                    return cached_quote
                return "Error fetching daily quote."
        except Exception as e:
            return f"Error: {str(e)}"




async def monitor_task(payload: MonitorPayload):
    result = await get_motivation()
    print("result:", result)
    data = {
        "message": result,
        "username": "Daily Motivation",
        "event_name": "Daily motivation",
        "status": "success"
    }
    async with httpx.AsyncClient() as client:
        await client.post(payload.return_url, json=data)


@bot_router.post("/tick", status_code=status.HTTP_202_ACCEPTED)
def send_motivation(payload: MonitorPayload, background_tasks: BackgroundTasks):
    background_tasks.add_task(monitor_task, payload)
    return {"status": "accepted"}
