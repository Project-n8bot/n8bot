from pymongo import MongoClient
import os

db = MongoClient(os.environ.get("MONGO_URL"))

general = db.general
leveling = general.leveling

def get_level(user_id):
    return get_user(user_id)["level"]

def get_xp(user_id):
    return get_user(user_id)["xp"]

def add_user(_id):
    data = {
        "_id": _id,
        "level": 1,
        "xp": 0
    }
    leveling.insert_one(data)

def get_user(member_id):
    user = leveling.find_one({"_id": member_id})
    if not user:
        add_user(member_id)
        user = {"_id": member_id,"level": 1,"xp": 0}
    return user

def remove_user(member):
    leveling.delete_one({"_id": member.id})

def gain_xp(member_id, xp_amount):
    leveling.update_one({"_id": member_id}, {"$inc": {"xp": xp_amount}})

async def level_up(message):
    user_id = message.author.id
    user = message.author

    user_data = get_user(user_id)
    xp = user_data["xp"]
    level = user_data["level"]

    xp_required = 5 * (level*level) + (50 * level) + 100

    if xp >= xp_required:
        leveling.update_one({"_id": user_id}, {"$set": {"level": level + 1}})

        await message.channel.send(f"Congrats {user.mention} you leveled up to level " + str(level + 1))

def wipe(member_id):
    leveling.update_one({"_id": member_id}, {"$set": {"level": 1, "xp": 0}})

def get_top_users(amount):
    users = leveling.find().sort("xp", -1).limit(amount)
    return [user for user in users]