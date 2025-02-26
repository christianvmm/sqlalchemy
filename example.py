from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Transaction

DATABASE_URL = "postgresql://postgres:@localhost:5432/finance"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def insert_role():
	transaction = Transaction(
		user_id=1,
		destiny_id=1,
		amount=400,
		description="hello word",
		category_id=1,
		type="INC"
	)

	session.add(transaction)
	session.commit()
	print("Transaction created")

def get_transactions():
	transactions = session.query(Transaction).all()

	for transaction in transactions:
		print(transaction.id, transaction.description, transaction.amount)


def delete_transaction(id):
	transaction = session.get(Transaction, int(id))

	if(transaction):
		session.delete(transaction)
		session.commit()
		print("deleted")


def update_transaction(id):
	transaction = session.get(Transaction, int(id))

	if(transaction):
		transaction.description = "idk bitch"
		session.commit()
		print("updated")


# insert_role()
# get_transactions()
# delete_transaction(4194)
# update_transaction(4097)