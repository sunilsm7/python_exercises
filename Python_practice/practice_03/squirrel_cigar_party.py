"""
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
Unless it is the weekend, in which case there is no upper bound on the number of cigars.
Return True if the party with the given values is successful, or False otherwise.


squirrel_cigar_party(30, False) -> False
squirrel_cigar_party(50, False) -> True
squirrel_cigar_party(70, True) -> True
"""

def squirrel_cigar_party(cigar_count, is_weekend):
	if is_weekend:
		if cigar_count < 40:
			return False
		# return "Party Successful!"
		return True
	else:
		if cigar_count >= 40 and cigar_count <= 60:
			# return "Party Successful!"
			return True
		else:
			# return "Party Unsuccessful"
			return False
 
def test_squirrel_cigar_party():
	assert squirrel_cigar_party(30, False) == False
	assert squirrel_cigar_party(50, False) == True
	assert squirrel_cigar_party(70, True) == True
	assert squirrel_cigar_party(30, True) == False

test_squirrel_cigar_party()