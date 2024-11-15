import pandas as pd


df = pd.read_csv("hotels.csv", dtype={"id":str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")###
df_card_security = pd.read_csv("card-security.csv", dtype=str)


class Hotel:
	def __init__(self, hotel_id):
		self.hotel_id = hotel_id
		self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze() ###

	def available(self):
		availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze() ###
		if availability == "yes":
			return True
		else:
			return False

	def book(self):
		df.loc[df["id"] == self.hotel_id, "available"] = "no"
		df.to_csv("hotels.csv", index=False) ### TODO

class SpaHotel(Hotel):
	def book_spa_package(self):
		pass



class ReservationTicket:
	def __init__(self, customer_name, hotel_object):
		self.customer_name = customer_name
		self.hotel_object = hotel_object

	def generate(self):
		content = f"""Thank you for your reservation
		Here are your booking data:
		Name: {self.customer_name}
		Hotel name: {self.hotel_object.name}
		"""
		return content


class ReservationTicketSpa(ReservationTicket):
	def generate(self):
		content = f"""Thank you for your SPA reservation
		Here are your SPA booking data:
		Name: {self.customer_name}
		Hotel name: {self.hotel_object.name}
		"""
		return content




class CreditCard:
	def __init__(self, number):
		self.number = number

	def validate(self,expiration, holder, cvc):
		card_data = {"number": self.number, "expiration": expiration,"holder":holder ,"cvc": cvc}
		if card_data in df_cards:
			return True

class SecureCreditCard(CreditCard):
	# def __init__(self, number):
	# 	super().__init__(number) ### CAN SKIP THIS IF THE init OF INHERTITING CLASS HAS NOTHING NEW

	def authenticate(self, given_password):
		password = df_card_security.loc[df_card_security["number"] == self.number, "password"].squeeze()
		if password == given_password:
			return True

print(df)
hotel_ID = input("Enter hotel id: ")
hotel = SpaHotel(hotel_ID)

if hotel.available():
	credit_card = SecureCreditCard(number = "1234567890123456")
	if credit_card.validate(expiration="12/26", holder = "JOHN SMITH", cvc = "123"):
		if credit_card.authenticate(given_password="mypass"):
			hotel.book()
			name = input("Enter your name: ")
			reservation_ticket = ReservationTicket(name, hotel)
			print(reservation_ticket.generate())
			is_spa = input("Do you want to book SPA package: ")
			if is_spa == "yes":
				hotel.book_spa_package()
				reservation_ticket = ReservationTicketSpa(name, hotel)
				print(reservation_ticket.generate())

		else:
			print("Credit card authentication failed")
	else:
		print("Payment problem")
else:
	print("The hotel is not available")