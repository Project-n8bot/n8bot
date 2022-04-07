import mysql.connector
import os

host_ip = os.environ.get("DB_IP")
db_password = os.environ.get("DB_PASSWORD")
db = mysql.connector.connect(host=host_ip, user="root", password=db_password, database="")
mycursor = db.cursor()

def get_level(user_id):
    sql = "select level from users where user_id = %s"
    mycursor.execute(sql, (user_id, ))
    level = mycursor.fetchall()

    return(level[0][0])

def get_xp(user_id):
    sql = "select xp from users where user_id = %s"
    mycursor.execute(sql, (user_id, ))
    xp = mycursor.fetchall()
    
    return(xp[0][0])

def add_user(member):
    sql = "insert into users (user_id, level, xp) values (%s, %s, %s)"
    val = (member.id, 1, 0)
    mycursor.execute(sql, val)

    db.commit()

def remove_user(member):
    sql = "delete from users where user_id = %s"
    val = (member.id, )
    mycursor.execute(sql, val)

    db.commit()

def gain_xp(member_id, xp_amount):
    user_id = member_id

    level = get_level(user_id)
    xp = get_xp(user_id)

    sql = "update users set xp = %s where user_id = %s"
    val = (xp + xp_amount, user_id)
    mycursor.execute(sql, val)
    
    db.commit()

async def level_up(message):
    user_id = message.author.id
    user = message.author

    level = get_level(user_id)
    xp = get_xp(user_id)
    xp_required = level * (10 * 1.5)

    if xp >= xp_required:
        sql = "update users set level = %s where user_id = %s"
        val = (level + 1, message.author.id)
        mycursor.execute(sql, val)

        db.commit()
        
        await message.channel.send(f"Congrats {user.mention} you leveled up to level " + str(level + 1))

def wipe(member_id):

    sql = "update users set level = 1, xp = 0 where user_id = %s"
    val = (member_id, )
    mycursor.execute(sql, val)

    db.commit()