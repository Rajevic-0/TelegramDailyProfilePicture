import asyncio
import telethon
from telethon.tl.functions.photos import DeletePhotosRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
import os

apiId = 123456
apiHash = "Your api apiHash"

#The name of your photos, put them on a folder called photos.
photos = { 
    0: "monday.jpg",
    1: "tuesday.jpg",
    2: "wednesday.jpg",
    3: "thursday.jpg",
    4: "friday.jpg",
    5: "saturday.jpg", 
    6: "sunday.jpg"
}

async def main():
    today = datetime.now().weekday()
    path = os.path.join("photos", photos[today])

    async with telethon.TelegramClient("session", apiId, apiHash) as client:
        current = await client.get_profile_photos("me", limit=1)
        if current:
            await client(DeletePhotosRequest(current))

        uploaded = await client.upload_file(path)
        await client(UploadProfilePhotoRequest(file=uploaded))

asyncio.run(main())