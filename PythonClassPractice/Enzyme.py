from __future__ import annotations

class Enzyme:
    """ Information about a particular enzyme. """

    def __init__(self, enzyme_name: str,
                       recognition_sequence: str) -> None:
        """Initialize a new enzyme with name enzyme_name and
        sequence recognition_sequence.
        >>> enzyme1 = Enzyme('Sau3A', 'GATC')
        >>> user1.name
        'Sau3A'
        >>> user1.sequence
        'GATC'
        """
        self.name = enzyme_name
        self.sequence = recognition_sequence

    def __str__(self) -> str:
        """Return a string representation of this enzyme.

        >>> enzyme1 = Enzyme('Sau3A', 'GATC')
        >>> print(enzyme1)
        The enzyme Sau3A has a recognition sequence of length 4
        >>> enzyme2 = Enzyme('HgaI', 'GACGC')
        >>> print(enzyme2)
        The enzyme HgaI has a recognition sequence of length 5
        """
        return f'The enzyme {self.name} has a recognition sequence of length {len(self.sequence)}'

class DNAStrand:
    """ Information about a DNA strand. """

    def __init__(self, new_strand: str) -> None:
        """Initialize a new DNA strand that has strand new_strand
        and an empty list of enzymes.

        >>> strand1 = DNAStrand('AGGCCT')
        >>> strand1.strand
        'AGGCCT'
        >>> strand1.enzymes
        []
        """
        self.strand = new_strand
        self.enzymes = []

    def is_cutter(self, enzyme: Enzyme) -> bool:
        """Return True iff enzyme's sequences appears one or more
        times in this DNA strand's strand.

        >>> enzyme1 = Enzyme('HaeIII', 'GGCC')
        >>> strand1 = DNAStrand('AGGCCT')
        >>> strand1.is_cutter(enzyme1)
        True
        >>> enzyme2 = Enzyme('Sau3A', 'GATC')
        >>> strand1.is_cutter(enzyme2)
        False
        """
        return enzyme.sequence in self.strand


    def add_enzyme(self, potential_enzyme_name: str,
                   potential_enzyme_sequence: str) -> None:
        """Modify this DNA strand's enzyme list to add the potential
        enzyme with name potential_enzyme_name and sequence
        potential_enzyme_sequence if and only if the potential enzyme
        is a cutter of the strand (as defined by the is_cutter method),
        and potential_enzyme_sequence is not a sequence of any enzyme
        this DNA strand already has. If this DNA strand already has
        an enzyme with that sequence, do not modify the enzyme list.

        >>> strand1 = DNAStrand('AGGCCT')
        >>> enzyme1 = Enzyme('HaeIII', 'GGCC')
        >>> strand1.enzymes.append(enzyme1)
        >>> len(strand1.enzymes)
        1
        >>> strand1.add_enzyme('XYZ', 'GGCC')
        >>> len(strand1.enzymes)
        1
        >>> strand1.add_enzyme('StuI', 'AGGCCT')
        >>> len(strand1.enzymes)
        2
        >>> strand1.add_enzyme('Sau3A', 'GATC')
        >>> len(strand1.enzymes)
        2
        """
        enzyme = Enzyme(potential_enzyme_name, potential_enzyme_sequence)

        if not self.is_cutter(enzyme):
            return

        for ez in self.enzymes:
            if ez.sequence == enzyme.sequence:
                return

        self.enzymes.append(enzyme)



