# Name: Abderrahmane Chebli
# Student ID:260965432


# Write function below including a docstring
def is_compatible(donor, recipient):
    """

    :param donor: blood type of the donor
    :param recipient:  blood type of the recipient
    :return: boolean value. true stands for compatible and false for incompatible

    >>> is_compatible("0+", "AB-")
    False
    >>> is_compatible("AB-", "AB+")
    True
    """
    #setting variables

    d_rhesus = donor[len(donor)-1]
    r_rhesus = recipient[len(recipient) - 1]
    d_antigen = donor[0:len(donor)-1]
    r_antigen = recipient[0:len(recipient)-1]

    #checking antigen compatibility

    antigen_compatibility = (d_antigen == r_antigen) or (r_antigen == "AB") or (d_antigen == "O")

    #checking rhesus compatibility

    rhesus_compatibility = not (d_rhesus == "+" and r_rhesus == "-")

    return (antigen_compatibility and rhesus_compatibility)








# Test cases:
print(is_compatible("O+", "AB-"))  # False
print(is_compatible("O+", "A+"))  # True
print(is_compatible("A-", "AB-"))  # True
print(is_compatible("B+", "O+"))    #False
print(is_compatible("AB-", "AB+"))  #True
print(is_compatible("AB+", "O+"))   #False