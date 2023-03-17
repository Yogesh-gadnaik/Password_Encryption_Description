import pypyodbc
import bcrypt

connection = pypyodbc.connect("""Driver={SQL Server};
                           Server=172.16.10.45;
                           Database=yogesh;
                           uid=talend2019;
                           pwd=Mouri@123;""")
cursor = connection.cursor()


def database_entry(name, password, gender, city):

    cursor.execute("insert into user_details(Name,Password,Gender,City) values('" +
                   name+"','"+password+"','"+gender+"','"+city+"')")
    cursor.commit()
    cursor.execute("select * from user_details where City='" + city+"'",)
    data = cursor.fetchone()
    print(data)
    if data:
        return 1
    else:
        return 0


def hide_pass(password):
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    encrypted_data = hashed.decode()
    return encrypted_data


def check_password(name, password):
    password = password.encode('utf-8')
    print(password)
    cursor.execute(
        "select password from user_details where Name='" + name+"'")
    data = cursor.fetchall()
    # print(data)
    for name in data:
        for hashname in name:
            # print(hashname)
            hash_pass = hashname.encode()
            print(hash_pass)
            if bcrypt.checkpw(password, hash_pass):
                return 1
            else:
                pass
    return 0


def recover(name, city, newpass):
    password = newpass.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))
    encrypted_data = hashed.decode()
    cursor.execute("update user_details set Password='" +
                   encrypted_data+"' where Name='"+name+"' and City='"+city+"'")
    cursor.commit()
    cursor.execute("select * from user_details where City='" + city+"'",)
    data = cursor.fetchone()
    print(data)
    if data:
        return name
    else:
        return 0
