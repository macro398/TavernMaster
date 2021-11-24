from tm_pkg.events import end_of_day, r_event, payroll, missing_boarder, wimpy_event, finale
from tm_pkg.image import image
import os

# Adding a Clear Screen lamda expression #
def clear(): return os.system('cls')
clear()
print('')
image()

# Uncomment the next line to play music in the background #
#os.system("start /MIN python tm_pkg\\play_music.py")    

# Game Intro #
print("Welcome to Tavernmaster.")
print("\nOne slow stormy night, you sit playing cards with the owner of the tavern you have been staying at for a few days after the last big job. You find yourself up pretty good and at this point Tavernkeeper is almost out of gold. The Tavernkeeper feeling desperate makes you a deal, if you win this next hand, you get the Tavern, but he keeps the money. But if he wins, he keeps the tavern and the money. Now normally this kind of all or nothing bet would scare you off. But you are sitting on a flush, and after all... you have always wanted a tavern. You agree to his deal and he smugly flips three aces. Much to his dismay, you flip your flush and he angrily signs over the deed to the Boar's Head Tavern.")
print("\nThe Boar's Head is a modest tavern located in the trade district of the coastal city of Waterdeep. The ground floor is a taproom with a fair number of tables, stools, and benches, while the second floor has rooms for weary travelers. You feel although you may not have any gold now, with this Tavern, you surely will make back what you lost with interest.")
input("Press enter to continue . . .")
clear()
print("When you arrive at the Boars Head the next morning you find a note attached to the door. The note reads . . .")
print("To whom it may concern:")
print("\nWe have been far too leniant as of late and we demand that you pay us the 3000gp you owe us by the end of the week or forfeit the property!")
print("The message is signed with the sigil of the Royal Bank of Waterdeep")
print("\nIt seems as though there was a loan taken out on the Boar's Head by the previous owner. You know that you aren't going to get out of this easily.")
print("Luckily today is the start of Fleetswake, a festival that celebrates the sea and maritime trade and brings in people from all over. If you play your cards right, you just may be able to aquire enough gold to pay off the bank and keep the Boars Head afloat.")
input("Press enter to continue . . .")

# Start of Play #
# Payroll Event #
clear()
payroll()
input("Press enter to continue . . .")
clear()
#   Monday  #
# Wimpy Event #
wimpy_event()
input("Press enter to continue . . .")
clear()
# End of Day 1 #
end_of_day()
input("Press enter to continue . . .")
clear()
#   Tuesday  #
# Random Event 1 #
r_event()
input("Press enter to continue . . .")
clear()
# End of Day 2 #
end_of_day()
input("Press enter to continue . . .")
clear()
#   Wednesday     #
# Random Event 2 #
r_event()
input("Press enter to continue . . .")
clear()
# End of Day 3 #
end_of_day()
input("Press enter to continue . . .")
clear()
#   Thursday   #
# Random Event 3 #
r_event()
input("Press enter to continue . . .")
clear()
# End of Day 4 #
end_of_day()
input("Press enter to continue . . .")
clear()
# Friday #
# Missing Boarder Event #
missing_boarder()
input("Press enter to continue . . .")
clear()
# End of Day 5 #
end_of_day()
input("Press enter to continue . . .")
clear()
# Saturday #
# Random Event 4 #
r_event()
input("Press enter to continue . . .")
clear()
# End of Day  #
end_of_day()
input("Press enter to continue . . .")
clear()
# Finale #
finale()