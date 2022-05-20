
"""
Primer design 
    Biologist who work in lab need primers in many experiments that require DNA/RNA replication
    and the aim of this program is to help them choose the primer that helps them acheive their experiment
    The rules for desgining a good primer are :
        - has a length between 10-20
        - has a C/G percentage of 40-60
        - Ends with 2 or 3 C/G bases without order
        - Does not have a tandom repeate (i.e one base repeats many times sequensionly)
        - Tm (melting tempreture) between 50-65
            Tm = 81.5 + 0.41 * percentage of C/G for each primer - 675/20
    * Forward primer is the same as the original sequence
    * Reverse primer is the reverse complemetary of the original sequence
"""


from rich import print
from itertools import groupby

original = "ATGAGCACTGAAGCATGATCCGGGACGTGGAGCTGGCCGAGGAGGCGCTCCCCAAGAAGACAGGGGGGCCCCAGGGCTCCAGGCGTTGCTTGTTCCTCAGCCTCTTCTCCTTCCTGATCGTGGCAGGCGCCACCACGCTCTTCTGCCTGCTGCACTTTGGAGTGATCGGCCCCCAGAGGGAAGAGGTGAGTGCCTGGCCAGCCTTCATCCACTCTCCCACCCAAGGGGAAATGGAGACGCAAGAGAGGGAGAGAGATGGGATGGGTGAAAGATGTGCGCTGATAGGGAGGGATGGAGAGAAAAAAACGTGGAGAAAGACGGGGATGCAGAAAGAGATGTGGCAAGAGATGGGGAAGAGAGAGAGAGAAAGATGGAGAGACAGGATGTCTGGCACATGGAAGGTGCTCACTAAGTGTGTATGGAGTGAATGAATGAATGAATGAATGAACAAGCAGATATATAAATAAGATATGGAGACAGATGTGGGGTGTGAGAAGAGAGATGGGGGAAGAAACAAGTGATATGAATAAAGATGGTGAGACAGAAAGAGCGGGAAATATGACAGCTAAGGAGAGAGATGGGGGAGATAAGGAGAGAAGAAGATAGGGTGTCTGGCACACAGAAGACACTCAGGGAAAGAGCTGTTGAATGCCTGGAAGGTGAATACACAGATGAATGGAGAGAGAAAACCAGACACCTCAGGGCTAAGAGCGCAGGCCAGACAGGCAGCCAGCTGTTCCTCCTTTAAGGGTGACTCCCTCGATGTTAACCATTCTCCTTCTCCCCAACAGTTCCCCAGGGACCTCTCTCTAATCAGCCCTCTGGCCCAGGCAGTCAGTAAGTGTCTCCAAACCTCTTTCCTAATTCTGGGTTTGGGTTTGGGGGTAGGGTTAGTACCGGTATGGAAGCAGTGGGGGAAATTTAAAGTTTTGGTCTTGGGGGAGGATGGATGGAGGTGAAAGTAGGGGGGTATTTTCTAGGAAGTTTAAGGGTCTCAGCTTTTTCTTTTCTCTCTCCTCTTCAGGATCATCTTCTCGAACCCCGAGTGACAAGCCTGTAGCCCATGTTGTAGGTAAGAGCTCTGAGGATGTGTCTTGGAACTTGGAGGGCTAGGATTTGGGGATTGAAGCCCGGCTGATGGTAGGCAGAACTTGGAGACAATGTGAGAAGGACTCGCTGAGCTCAAGGGAAGGGTGGAGGAACAGCACAGGCCTTAGTGGGATACTCAGAACGTCATGGCCAGGTGGGATGTGGGATGACAGACAGAGAGGACAGGAACCGGATGTGGGGTGGGCAGAGCTCGAGGGCCAGGATGTGGAGAGTGAACCGACATGGCCACACTGACTCTCCTCTCCCTCTCTCCCTCCCTCCAGCAAACCCTCAAGCTGAGGGGCAGCTCCAGTGGCTGAACCGCCGGGCCAATGCCCTCCTGGCCAATGGCGTGGAGCTGAGAGATAACCAGCTGGTGGTGCCATCAGAGGGCCTGTACCTCATCTACTCCCAGGTCCTCTTCAAGGGCCAAGGCTGCCCCTCCACCCATGTGCTCCTCACCCACACCATCAGCCGCATCGCCGTCTCCTACCAGACCAAGGTCAACCTCCTCTCTGCCATCAAGAGCCCCTGCCAGAGGGAGACCCCAGAGGGGGCTGAGGCCAAGCCCTGGTATGAGCCCATCTATCTGGGAGGGGTCTTCCAGCTGGAGAAGGGTGACCGACTCAGCGCTGAGATCAATCGGCCC"
original = original[0:200]

# Make a small framgments of the original DNA of the same length of primer
def make_sub_Dna(dna):
    """
    Take the original sequence and make subsequences of it of length 20 (primer length can vary depends on the experiment)
    """
    subDna = []  # each element will contain a primer of 20 bases
    for i in range(0, len(dna),20): # depends on how many primers you want, you can make the 3rd argument (step) in the range = the primer length
        subDna.append(dna[i:i+20])
        if len(dna[i:i+20]) < 20:
            subDna.remove(dna[i:i+20])
    return subDna


class Fragments:
    def __init__(self, locus, fragment_seq, percent, repeats, ending, Tm, Ta):
        self.fragment_seq = fragment_seq
        self.repeats = repeats
        self.percent = percent
        self.ending = ending
        self.locus = locus
        self.Tm = Tm
        self.Ta = Ta


# The forward primers is the same as the original (complementary to the second strand)
forward_Primers = make_sub_Dna(original[0:100])


# Check the primers rules for each of the primers in the lists above and choose the best primer
global checker   # global var to use in many functions


def count_Percentage(primer):
    """
    Takes a primer sequence and returns the percentage of C and G
    """
    count = 0
    percenatage = 0
    count += primer.count('C')
    count += primer.count('G')
    percenatage = int(100 * count/len(primer))
    return percenatage


def check_ends(primer):
    """
    Takes a primer sequence and check the ends of it
    input : ACTGACTG
    output : False ( it does not end with at least 2 bases of G or C in both sides)
    
    input : CCCTATGAGGG
    output : True
    """
    last_3 = primer[len(primer)-3:len(primer)]
    first_3 = primer[0:3]
    first_2 = primer[0:2]
    last_2 = primer[-2:len(primer)]

    # the 1st and last is the same base or the 1st and last is C and G
    if (primer[0] == 'G' and primer[-1] == 'G') or (primer[0] == 'G' and primer[-1] == 'C'):
        checker = True
    elif (primer[0] == "C" and primer[-1] == "C") or (primer[0] == 'C' and primer[-1] == 'G'):
        checker = True
    else:
        # the 1st and the last two
        for (base1, base2) in (first_2, last_2):
            if (base1 != "A" and base1 != "T") and (base2 != "A" and base2 != "T"):
                checker = True
            else:
                checker = False
                break
        else:
            # the 1st and the last three
            for (bases1, bases2, bases3) in (first_3, last_3):
                if (bases1 != "A" and bases1 != "T") and (bases2 != "A" and bases2 != "T") and (bases3 != "A" and bases3 != "T"):
                    checker = True
                else:
                    checker = False
                    break
    return checker


def check_repatition(primer):
    """
    input : "AAATGC"
    output : True (there is a tandom repeat)
    
    input : "ATGCAC"
    output : False (there is No tandom repeat)
    """
    groups = groupby(primer)
    result = [(label, sum(1 for any in group)) for label, group in groups]
    list = [x[1] for x in result]
    for repeats in list:
        # the True and False here is based on what we want,not the checking of the condition
        if repeats >= 3:
            checker = False
            break
        elif repeats < 3:
            checker = True
    return checker


#space=(" "*10)
print("Forward Primers\t     "+"C/G(40-60%)" +
      "   C/G Ending   Tandem Repeat Tm(50-65°C)\n"+("-"*75))
print("5' Leading-----> 3'\n")


def check_Tm(tm):
    """
    Tm (melting tempreture) should be between 50 and 65 
    """
    if tm >= 50 and tm <= 65:
        return True
    else:
        return False


theBest = ""
theBest_loc = theBest_percent = theBest_Ta = 0
theBest_List = []
theBest_locs = []
best_and_Locus = dict() #will contain all the choosen primers that achieved most of the rules 


def make_primers_Obj(primersList):
    """
    Make primers objects and choose the best of it (the ones that have more True values which represents how many conditions it acheived)
    """
    locus = 0
    is_good_percent = False
    for primer in primersList:
        percent_each_primer = count_Percentage(primer)

        if percent_each_primer >= 40 and percent_each_primer <= 60:
            is_good_percent = True
        else:
            is_good_percent = False

        tm = 81.5 + 0.41 * percent_each_primer - 675/20
        ta = tm - 5
        locus += 1
        # def __init__( locus,fragment_seq , percent ,repeats, ending, Tm , Ta)
        fragment_obj = Fragments(locus, primer, is_good_percent, check_repatition(
            primer), check_ends(primer), tm, ta)

        print(fragment_obj.locus, end=".")
        print(fragment_obj.fragment_seq, " ", fragment_obj.percent, "\t", fragment_obj.ending,
              "\t\t", fragment_obj.repeats, "\t", fragment_obj.Tm, check_Tm(tm))

        # if all or most of the conditions were true
        if (is_good_percent and fragment_obj.repeats and fragment_obj.ending and check_Tm(tm)) or (is_good_percent and fragment_obj.repeats and fragment_obj.ending and check_Tm(tm) == False):
            theBest = fragment_obj.fragment_seq
            theBest_loc = fragment_obj.locus
            theBest_Ta = str(fragment_obj.Ta)
            theBest_Ta += " °C"
            best_and_Locus[theBest] = [theBest_loc, theBest_Ta]
            is_Found = True
        else:
            is_Found = False

    if is_Found == True:
        print("\nThe Best Primers and their location and Ta are: ",
              best_and_Locus, "\n")
    # else:
    #     print("\nNo good primer is found :(\n")


make_primers_Obj(forward_Primers)


# Making the reverse primers list

# Make complementary strand
def make_complementary(start, end, original):
    bases = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    complementary = ""
    for base in original[start:end]:
         complementary += bases.get(base)
    return complementary
    

# Get the complemetary and make small seq from it's reverse
complement = make_complementary(len(original)-100, len(original), original)

reverse_Primers = make_sub_Dna(complement[::-1])

print("\nReverse Primers\t     "+"C/G(40-60%)" +
      "   C/G Ending   Tandem Repeat Tm(50-65°C)\n"+("-"*75))
print("5' <-----Lagging 3'\n")
make_primers_Obj(reverse_Primers)
