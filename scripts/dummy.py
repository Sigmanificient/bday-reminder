import sqlite3


def main():
    with (
        sqlite3.connect("bday_reminder/bday.db") as conn,
        open("scripts/create_dummy_user.sqlite") as f,
    ):
        conn.execute(f.read())

    print("Dummy user created")


if __name__ == "__main__":
    main()
