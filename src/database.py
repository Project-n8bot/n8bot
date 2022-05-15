from pymongo import MongoClient
import os

db = MongoClient(os.environ.get("MONGO_URL"))

general = db.general
leveling = general.leveling

def get_level(user_id):
    level = leveling.find_one({"_id": user_id})
    if not level:
        add_user(user_id)
        level = 1
    else:
        level = level["level"]
    return level

def get_xp(user_id):
    xp = leveling.find_one({"_id": user_id})
    if not xp:
        add_user(user_id)
        xp = 0
    else:
        xp = xp["xp"]
    return xp

def add_user(_id):
    data = {
        "_id": _id,
        "level": 1,
        "xp": 0
    }
    leveling.insert_one(data)

def remove_user(member):
    leveling.delete_one({"_id": member.id})

def gain_xp(member_id, xp_amount):
    user_id = member_id

    level = get_level(user_id)
    xp = get_xp(user_id)

    leveling.update_one({"_id": user_id}, {"$inc": {"xp": xp_amount}})

async def level_up(message):
    user_id = message.author.id
    user = message.author

    level = get_level(user_id)
    xp = get_xp(user_id)
    xp_required = level * (10 * 1.5)

    if xp >= xp_required:
        leveling.update_one({"_id": user_id}, {"$set": {"level": level + 1}})

        await message.channel.send(f"Congrats {user.mention} you leveled up to level " + str(level + 1))

def wipe(member_id):
    leveling.update_one({"_id": member_id}, {"$set": {"level": 1, "xp": 0}})
