import gd
import asyncio
import os
from dotenv import load_dotenv

# Load account information from .env
load_dotenv()

# Initialize the client
client = gd.Client()

async def GetLevel():
    # Login to account
    try:
        await client.login(os.getenv("GD_USERNAME"), os.getenv("GD_PASSWORD"))
    except:
        print("Failed to login; Check .env")
        return

    # Download level
    try:
        level = await client.get_level(int(input("GD Level ID: ")))
    except:
        print("Failed to get level")
        return
    
    # Print the 
    print("Name: " + level.name)
    print("ID: " + str(level.id))

    # Check if copyable
    if level.is_copyable() == True:
        # Check if level has a password
        if level.password != None:
            print("Copy Password: " + str(level.password))
        else:
            print("No copy password")
    else:
        print("Level not copyable")

# Run an asynchronous function using asyncio to get level information
asyncio.run(GetLevel())
