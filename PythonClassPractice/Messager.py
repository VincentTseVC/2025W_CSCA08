from __future__ import annotations
from _typeshed import NoneType

class MessengerUser:
	""" Information about a particular Messenger user. """


	def __init__(self, messenger_username: str) -> None:
		"""Initialize a new Messenger user that has username 
		messenger_username, and an empty friends list.

		>>> user1 = MessengerUser('tom')
		>>> user1.username 
		'tom'
		>>> user1.friends 
		[] 
		"""

	def __str__(self) -> str:
		"""Return a string representation of this Messenger user.

		>>> user1 = MessengerUser('tom')
		>>> user1.friends.append('jen')
		>>> print(user1) 
		User tom has 1 friend(s).
		>>> user2 = MessengerUser('jen')
		>>> user2.friends.extend(['paul', 'tom'])
		>>> print(user2) 
		User jen has 2 friend(s). 
		"""

	def are_friends(self, other_user: MessengerUser) -> bool:
		"""Return True iff this MessengerUser and other_user are friends.

		>>> user1 = MessengerUser('tom')
		>>> user1.friends.extend(['jen', 'paul'])
		>>> user2 = MessengerUser('jen')
		>>> user2.friends.extend(['tom', 'paul'])
		>>> user3 = MessengerUser('paul')
		>>> user3.friends.extend(['jen'])
		>>> user1.are_friends(user2) 
		True
		>>> user1.are_friends(user3) 
		False 
		"""

class MessengerChat:
	""" Information about a Messenger Chat. """

	def __init__(self, chat_id: int, chat_initiator: MessengerUser) -> NoneType:
		"""Initialize a new Messenger chat that has chat id chat_id and a list of 
		members that initially only contains chat_initiator.

		>>> user1 = MessengerUser('tom')
		>>> chat1 = MessengerChat(201, user1)
		>>> chat1.chat_id 
		201
		>>> chat1.chat_members == [user1] 
		True 
		"""


	def add_member(self, potential_member: MessengerUser) -> bool:
		"""Return True iff potential_member can be added to this chat, 
		and if so, modify this MessengerChat's chat_members to add 
		potential_member to the chat. A MessengerUser can be added to 
		this chat if and only if they are friends with at least one 
		other member of the chat.

		Precondition: 
		  - All existing members of this MessengerChat are friends with 
		    at least one other member, or the chat contains only the 
			chat initiator. There is at least one member in the 
			MessengerChat.


		>>> user1 = MessengerUser('tom')
		>>> user1.friends.extend(['paul', 'jen'])
		>>> user2 = MessengerUser('jen')
		>>> user2.friends.extend(['tom', 'paul'])
		>>> user3 = MessengerUser('max')
		>>> user3.friends.extend(['paul'])
		>>> chat1 = MessengerChat(201, user1)
		>>> chat1.add_member(user2) 
		True
		>>> chat1.chat_members == [user1, user2] 
		True
		>>> chat1.add_member(user3) 
		False
		>>> chat1.chat_members == [user1, user2] 
		True 
		"""
