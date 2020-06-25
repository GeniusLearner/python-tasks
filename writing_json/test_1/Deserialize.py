import json

backjack_hand =(8,"q")
encoded_hand = json.dumps(backjack_hand)
decoded_hand = json.loads(encoded_hand)

decoded_hand
# [8, 'q']
#It returns a list, rather that tuple

backjack_hand == tuple(decoded_hand)
#True
