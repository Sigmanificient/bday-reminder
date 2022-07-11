import sqlite3


def add_user():
	with (
		sqlite3.connect("bday_reminder/bday.db") as conn,
		open("scripts/add_user.sqlite") as f,
	):
		conn.execute(f.read())

	print("User added")


def main():
	try:
		add_user()
	except sqlite3.OperationalError:
		print("The database hasn't been created yet, please run the application first.")
	else:
		print("Dummy user created")


if __name__ == "__main__":
	main()
