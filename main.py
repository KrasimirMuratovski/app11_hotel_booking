import pandas as pd


df = pd.read_csv("hotels.csv", dtype={"id":str})


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




print(df)
hotel_ID = input("Enter hotel id: ")
hotel = Hotel(hotel_ID)
if hotel.available():
	hotel.book()
	name = input("Enter your name: ")
	reservation_ticket = ReservationTicket(name, hotel)
	print(reservation_ticket.generate())
else:
	print("The hotel is not available")