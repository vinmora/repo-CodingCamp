import json
from datetime import datetime


USER_DATA_FILE = "users.json"


def load_users():
    try:
        with open(USER_DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  


def save_users(users):
    with open(USER_DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


def display_users(users):
    print("\nDaftar Pengguna:")
    for user in users:
        print(f"🆔 ID: {user['id']} | 👤 Nama: {user['name']} | 📧 Email: {user['email']} | 📅 Bergabung: {user['join_date']}")
    print("-" * 50)


def add_user(name, email):
    users = load_users()
    
    new_user = {
        "id": len(users) + 1,  
        "name": name,
        "email": email,
        "join_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    users.append(new_user)
    save_users(users)
    print(f"✅ Pengguna {name} berhasil ditambahkan!")


def find_user(user_id):
    users = load_users()
    user = next((u for u in users if u["id"] == user_id), None)
    return user


def update_user(user_id, new_name=None, new_email=None):
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            if new_name:
                user["name"] = new_name
            if new_email:
                user["email"] = new_email
            save_users(users)
            print(f"🔄 Pengguna ID {user_id} berhasil diperbarui!")
            return
    print(f"❌ Pengguna dengan ID {user_id} tidak ditemukan!")


def delete_user(user_id):
    users = load_users()
    users = [user for user in users if user["id"] != user_id]
    save_users(users)
    print(f"🗑 Pengguna ID {user_id} telah dihapus.")


if __name__ == "__main__":
 
    add_user("Alice Johnson", "alice@example.com")
    add_user("Bob Smith", "bob@example.com")

   
    display_users(load_users())

   
    user = find_user(1)
    if user:
        print(f"🔍 Pengguna Ditemukan: {user['name']} ({user['email']})")
    
    update_user(1, new_name="Alice Williams")


    delete_user(2)

   
    display_users(load_users())
