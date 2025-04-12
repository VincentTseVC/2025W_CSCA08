from __future__ import annotations

class ZoomUser:
    """ Information about a particular Zoom user. """

    def __init__(self, zoom_username: str,
                 zoom_location: str, zoom_contacts: list[str]) -> None:
        """Initialize a new Zoom user that has username zoom_username,
        location zoom_location and contacts zoom_contacts.

        >>> user1 = ZoomUser('uoft123', 'Toronto', ['debbie', 'paul'])
        >>> user1.username
        'uoft123'
        >>> user1.location
        'Toronto'
        >>> user1.contacts
        ['debbie', 'paul']
        """
        self.username = zoom_username
        self.location = zoom_location
        self.contacts = zoom_contacts


    def __str__(self) -> str:
        """Return a string representation of this Zoom user.

        >>> user1 = ZoomUser('uoft123', 'Toronto', ['debbie'])
        >>> print(user1)
        uoft123 lives in Toronto and has 1 contact(s).
        >>> user2 = ZoomUser('mel', 'Vancouver', ['paul', 'debbie'])
        >>> print(user2)
        mel lives in Vancouver and has 2 contact(s).
        """
        # return self.username + ' lives in ' + self.location + ' and has ' + str(len(self.contacts)) + ' contact(s).'
        # return '{} lives in {} and has {} contact(s).'.format(self.username, self.location, len(self.contacts))
        return f'{self.username} lives in {self.location} and has {len(self.contacts)} contact(s).'

    def same_contacts(self, user_contacts: list[str]) -> bool:
        """Return True iff this Zoom user has the same contacts,
        in any order, as the ones in user_contacts.
        The elements in user_contacts and the contacts of this
        Zoom user may be reordered.

        >>> user1 = ZoomUser('uoft123', 'Toronto', ['debbie', 'paul'])
        >>> contact_list1 = ['paul', 'debbie']
        >>> contact_list2 = []
        >>> user1.same_contacts(contact_list1)
        True
        >>> user1.same_contacts(contact_list2)
        False
        """
        self.contacts.sort()
        user_contacts.sort()

        return self.contacts == user_contacts

    def __eq__(self, other_user: ZoomUser) -> bool:
        """Return True iff this Zoom user has the same contacts as
        Zoom user other_user.

        >>> user1 = ZoomUser('uoft123', 'Toronto', ['debbie', 'paul'])
        >>> user2 = ZoomUser('mel', 'Vancouver', ['paul', 'debbie'])
        >>> user1 == user2
        True
        >>> user3 = ZoomUser('uoft_cs1', 'Toronto',
        ...                   ['debbie', 'ioana', 'alex', 'paul'])
        >>> user1 == user3
        False
        """
        return self.same_contacts(other_user.contacts)

class ZoomCall:
    """ Information about a Zoom call. """

    def __init__(self, call_id: int , call_initiator: ZoomUser) -> None:
        """Initialize a ZoomCall with a call id call_id and a list of members
        that initially only contains Zoom user call_initiator.

        >>> user1 = ZoomUser('uoft123', 'Toronto', ['debbie'])
        >>> call1 = ZoomCall(201, user1)
        >>> call1.call_id
        201
        >>> call1.call_members == [user1]
        True
        """
        self.call_id = call_id
        self.call_members = [call_initiator]

    def add_members(self, potential_members: list[ZoomUser]) -> int:
        """Add call members from potential_members to this Zoom call and return
        the number of newly added call members.
        A person from potential_members can only be added to this call if their
        location is the same as the location of all the other members of that call.

        Precondition:
          - All existing members of this Zoom call share the same location and
            there is at least one member in the call.


        >>> user1 = ZoomUser('uoft123', 'Toronto', ['debbie'])
        >>> user2 = ZoomUser('mel', 'Vancouver', [])
        >>> user3 = ZoomUser('max', 'Toronto', [])
        >>> call1 = ZoomCall(201, user1)
        >>> call1.add_members([user2, user3])
        1
        >>> call1.call_members == [user1, user3]
        True
        """
        房主 = self.call_members[0]

        count = 0
        for member in potential_members:
            if member.location == 房主.location:
                self.call_members.append(member)
                count += 1

        return count