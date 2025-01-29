import sqlite3

con =sqlite3.connect('uTubeManager.db')
cursor = con.cursor()

cursor.execute(" CREATE TABLE IF NOT EXISTS Videos(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, time TEXT NOT NULL)")

def list_video():
    cursor.execute('SELECT * FROM Videos')
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute('''INSERT INTO Videos(name, time) VALUES(?, ?)''', (name, time))
    con.commit()
    print("Video added successfully")
    
    
def update_video(new_name, new_time, id):
    cursor.execute('''UPDATE Videos SET name = ?, time = ? WHERE id = ?''', (new_name, new_time, id))
    con.commit()
    print("Video updated successfully")
    
def delete_video(id):
    cursor.execute('''DELETE FROM Videos WHERE id = ?''', (id,))
    con.commit() 


def main():
    while True:
        print("\n Youtube Manager app with DB")
        print("\n 1. List Video")
        print("\n 2. Add Video")
        print("\n 3. Update Video")
        print("\n 4. Delete Video")
        print("\n 5. Exit")
        user_input = input("Enter your choice: ")
        
        match user_input:
            case '1':
                list_video()
                
            case '2':
                
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(name, time)
               
            case '3':
                
                id = int(input("Enter video id: "))
                new_name = input("Enter video name: ")
                new_time = input("Enter video time: ")
                update_video( new_name, new_time,id)
                
            case '4':
                id = int(input("Enter video id: "))
                delete_video(id)
                
            case '5':
                break
                
            case _:
                print("Invalid choice")
                break
    con.close()


if __name__ == '__main__':
    main()
    