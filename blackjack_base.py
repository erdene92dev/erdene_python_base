from datetime import datetime, date

print('play date:',date.today())

base_deck = []

for num in range(0, 14):
	if num != 0:
		base_deck.append(num)		

full_deck = base_deck*4
full_deck = sorted(full_deck,reverse=False)

full_deck_with_faces = []
for cards in full_deck:
	if cards == 11:
		