import random
from typing import List, Tuple
from prettytable import PrettyTable


class NotSoSecretSanta:
    def __init__(self, participants: List[str], couple_pairs: List[Tuple[str, str]]) -> None:
        """
        Args:
            participants (List[str]): List of people participating.
            couple_pairs (List[Tuple[str, str]]): List of tuples where each tuple contains two people.
        """
        self.participants = participants
        self.couple_pairs = couple_pairs

    def is_couple(self, person1: str, person2: str) -> bool:
        """
        Check if two people are in a couple.

        Args:
            person1 (str): First person.
            person2 (str): Second person.

        Returns:
            bool: True if the people are in a couple, False otherwise.
        """
        return (person1, person2) in self.couple_pairs or (person2, person1) in self.couple_pairs

    def is_gift_exchange(self, table_list, person1, person2):
        for row in table_list:
            if person2 in row[0]:
                if person1 in row[1]:
                    return True
        return False




    def generate_matches(self) -> PrettyTable:
        """
        Simulate the Secret Santa gift exchange.

        Returns:
            PrettyTable: Table showing the gift exchange pairing.

        """
        table = PrettyTable()
        table.field_names = ['Giver', 'Receiver']

        table_list = []

        received = []
        max_attempts = len(self.participants) * (len(self.participants) - 1)
        attempts = 0

        for person in self.participants:
            give_to = random.choice(self.participants)

            while person == give_to or self.is_couple(person, give_to) or give_to in received or self.is_gift_exchange(table_list, person, give_to):
                give_to = random.choice(self.participants)
                attempts += 1
                if attempts >= max_attempts:
                    return False

            table_list.append([person, give_to])
            received.append(give_to)

        table.add_rows(table_list)

        print(table)
        return True


if __name__ == '__main__':
    # participants = ['Jo', 'Jason', 'Laura', 'Nick', 'Jenny', 'Lynne', 'Ivor', 'Tim', 'Michelle']
    # couple_pairs = [('Tim', 'Michelle'), ('Lynne', 'Ivor'), ('Jo', 'Jason'), ('Nick', 'Jenny')]

    participants = [ 'Tim', 'Michelle', 'John', 'Julie', 'Ben', 'Colin', 'Valerie', 'Jenny','Phil']
    couple_pairs = [('Tim', 'Michelle'), ('John', 'Julie'), ('Colin', 'Valerie'), ('Phil', 'Jenny')]





    simulator = NotSoSecretSanta(participants, couple_pairs)
    results = simulator.generate_matches()
    while not results:
        results = simulator.generate_matches()
