import random
from tm_pkg.tavern import Employee, Tavern

events_this_playthrough = []

waitress = Employee()
bard = Employee()
tavern = Tavern()
waitress.name = 'Ava'
bard.name = 'Clarence'

def player_input(flavor_text,choice1, choice2, choice3):
    while True:
        print(flavor_text)
        print(choice1)
        print(choice2)
        print(choice3)
        player_choice = input("Which will it be? ").strip()
        if player_choice == "1" or player_choice == "2" or player_choice == "3":
            break
        else:
            print("\nInvalid input, please select 1, 2, or 3.\n")
    return player_choice
    

def r_event():
    total_events = [1,2,3,4,5,6,7,8]
    this_event = random.choice(total_events)
    
    # Ensure this playthrough doesn't have the same event happen multiple times by checking the list #
    while this_event in events_this_playthrough:
        this_event = random.choice(total_events)
    # Add this event into the events this playthrough list #
    events_this_playthrough.append(this_event)

    # Drunken Mage Event #
    if this_event == 1:
        print("A well dressed but extremely inebriated mage asks the waitress for another bottle of your finest Firebrandy. He has already had three bottles of Flamebeard's Firebrandy (25 gp per bottle).")
        print("You notice that there is a half empty bottle of the Flamebeard's Firebrandy at an empty table and that it would be easy enough to refill it with low end Firebrandy which could net you an extra 15gp.")
        flavor_text = "\nThis leaves you with three choices: "
        choice1 = "1 - Send a new bottle of Flamebeard's to the mage."
        choice2 = "2 - Take a chance that the mage won't notice and send him the mixed Firebrandy."
        choice3 = "3 - Tell the mage he has had enough and that it is time to settle his bill."
        result = player_input(flavor_text, choice1, choice2, choice3)
        if result == "1":
            print("The mage seems satisfied and after this last bottle has decided to close out his tab. You gain 100gp and he tips the waitress 5gp.")
            tavern.profit(100)
            waitress.happiness = waitress.happiness + 1
        if result == "2":
            tavern.karma = tavern.karma - 1
            notice = random.randint(1,2)
            if notice == 1:
                print("The mage seems to not have noticed. After this last bottle he closes out his tab. You gain 115gp and he tips the waitress 5gp.")
                tavern.profit(115)
                waitress.happiness = waitress.happiness + 1
            elif notice == 2:
                print("The mage noticed that something seemed off and annoyed, he confronts the waitress. The waitress comes to you in a panic and tells you of the situation. You personally walk out and apologize to the mage.")
                waitress.happiness_loss(1)  
                mage_attitude = random.randint(1,2)
                if mage_attitude == 1:
                    print("\nThe mage seems satisfied with your apology and offer for the last Firebrandy to be on the house. He finishes his drink and pays his tab. You gain 75gp but he doesn't tip the waitress and she loses enthusiasm.")
                    tavern.profit(75)
                else:
                    print("\nThe drunken mage is furious and not only does he refuse to pay his bill, he also blows a hole in the roof. You made no money and it is going to cost you 25gp to repair the roof.")
                    tavern.profit(-70)
        if result =="3":
            print("\nThe drunken mage doesn't understand why he is being cut off and after paying his bill, he decides to saunter down to the next tavern. You gain 75gp and he tips the waitress 3gp.")
            tavern.profit(75)
    
    # Brewer Event #    
    elif this_event == 2:
        print("A stout dwarven man comes into the tavern asking to speak with the owner of the establishment. You approach the dwarf and notice that he is wearing some sort of cask on his back. The dwarf greets you by saying \"Aye so you must be the owner of this here establishment. My name is Brahn Stormstout, and I come to make you an offer ye cannot refuse!\"")
        print("You are skeptical but intrigued at what Brahn could possibly be here to offer you. Brahn requests that you bring four tankards, two filled to the brim with mead and two that are empty. When you return with the tankards Brahn grabs the two that are empty and fills them using the cask on his back. He then implores you to do a taste test comparing his brew to what you sell at the tavern. Brahn definitely knows his stuff as the mead he brought tastes much better than the mead you currently sell.")
        print("Brahn presents you with an offer, to become your new mead provider all it will cost you is 1500 gp per week. You currently pay 750gp per week, but with this new mead, you feel certain you will get an increase in business.")
        flavor_text = "\nWhat do you want to do?"
        choice1 = "1 - Agree to the 1500gp per week offer."
        choice2 = "2 - Tell Brahn the mead isn't that good and the best you can do is match the 750gp."
        choice3 = "3 - Decline the offer, you aren't in a place to make those kinds of financial decisions."
        result = player_input(flavor_text, choice1, choice2, choice3)
        if result == "1":
            tavern.daily_income = 150 
            tavern.gp -= 1500
            print("You accept Brahn's deal and feel as though your tavern will have a higher income with the new mead.")
        if result == "2":
            tavern.karma -= 1
            rint = random.randint(1,2)
            if rint == 1:
                print("Brahn looks at you as though you insulted his mother. He feels insulted at your words and walks away in stunned disbelief.")
            elif rint == 2:
                print("Brahn looks as you in stunned disbelief. He lets out a deep sigh, and finally agrees to 750gp per week.")
                tavern.gp -= 750
        if result == "3":
            print("You gracefully decline the offer and let Brahn know that you are honored that he thought of you, but for now you are unable to change meads.")

    # Rats in the Cellar Event #
    elif this_event == 3:
        print("While you are preparing dinner, you go down to the cellar to get a sack of potatoes. While down there you hear some scurrying around and notice a giant 3 foot rat bound around the corner. You should probably get that taken care of. You return to the tavern where you notice a group of young adventurers that might be best suited for this task.")
        flavor_text = "\nWhat do you do?"
        choice1 = "1 - Save the coin by sending the waitress and bard down there together to deal with it."
        choice2 = "2 - Ask the group of young adventurers to take care of it for a reward."
        choice3 = "3 - Ignore the problem, after all what's the worst that can happen?"
        result = player_input(flavor_text, choice1, choice2, choice3)
        if result == "1":
            print("They succeed in dealing with the rat, but they are grossed out and feel taken advantage of.")
            bard.happiness -= 1
            waitress.happiness -= 1
        if result == "2":
            flavor_text_2 = "\nThe adventurers seem up to the task, but ask about the reward."
            choice1_2 = "1 - Offer 50gp and free ale for the night."
            choice2_2 = "2 - Offer 50gp."
            choice3_2 = "3 - Offer free ale for the night."
            result2 = player_input(flavor_text_2, choice1_2, choice2_2, choice3_2)
            if result2 == "1":
                print("the adventurers are more than happy with your offer and take care of the problem swiftly and quietly")
                tavern.gp -= 70
            if result2 == "2":
                tavern.gp -= 50
                print("The adventurers accept your deal, but go at it half heartedly")
            if result2 == "3":
                print("The adventurers get a bit sloshed before starting and proceed to make a lot of noise dealing with the rat to the point that you have to ask the bard to be louder. The bard is annoyed at the request, but at least you saved 50gp.")
                tavern.gp -= 20
                bard.happiness -= 1
        if result == "3":
            print("The food out of your kitchen causes people to get sick, and you can't help but think it may be because of the rats. You go down and deal with the rat yourself, and pay 100gp to keep from being shut down.")
            tavern.karma -= 2
            tavern.gp -= 100

    # Catering Event #
    elif this_event == 4:
        print("There is a wedding that has asked you to cater the food and drink. You are planning to send two casks of honey mead and a whole boar accompanied by sides of bread, cheese, and potatoes. They have provided you with 600gp for supplies and an additional 200gp to deliver them to the event, however the delivery service is unable to make the delivery.")
        flavor_text = "\nWhat do you do?"
        choice1 = "1 - Inform the wedding party that you are going to be unable to make the delivery returning the 200gp for delivery. But they will need to come get the food and drink that you have prepared for the event."
        choice2 = "2 - Keep all of the money and make the delivery yourself."
        choice3 = "3 - Keep the money for the supplies and make the delivery yourself, but return the 200gp for delivery as a wedding present to the bride and groom."
        result = player_input(flavor_text, choice1, choice2, choice3)
        if result == "1":
            print("The wedding party comes and gets the supplies and painstakingly moves the supplies themselves.")
            tavern.karma -= 1
            tavern.profit(600)
        if result == "2":
            print("The wedding goes well, and you made a nice profit.")
            tavern.profit(800)
        if result == "3":
            print("The bride and groom hold a special toast to you thanking you for your generosity. You feel good about the choice you made.")
            tavern.profit(600)
            tavern.karma += 1
        
    # Flask Event #
    elif this_event == 5:
        print("Shortly after dinnertime, Ava comes to you saying that she is pretty sure she saw one of the locals refill their tankard with the contents of a flask. Everyone knows this is against the rules and generally frowned upon. He is sitting with a small group who has been buying drinks steadily.")
        flavor_text = "\nWhat do you do?"
        choice1 = "1 - Tell Ava to ignore it and bring it up again later if it continues to happen."
        choice2 = "2 - Confront the customer."
        choice3 = "3 - Ignore the situation all together."
        result = player_input(flavor_text, choice1, choice2, choice3)
        if result == "1":
            print("Ava comes back to you about half an hour later and it seems the customer is intent to get out of paying for any more ale.")
            result = "2"
        if result == "2":
            print("You approach the customer.")
            flavor_text_2 = "\nWhat do you say?"
            choice1_2 = "1 - My waitress says she saw you refilling your tankard with a flask, if we see it again you are going to have to leave."
            choice2_2 = "2 - Hey guys, I just wanted to remind you that we don't  allow outside food or drink to be consumed on our grounds, we had an issue with somebody else doing it and we had to kick them out."
            choice3_2 = "3 - You shout out to everyone at the bar that you don't allow outside food or drink on our grounds."
            result2 = player_input(flavor_text_2, choice1_2, choice2_2, choice3_2)
            if result2 == "1":
                waitress.happiness -= 1
                print("The customer half-heartedly appologizes and is curt to the waitress for the rest of the night.")
            if result2 == "2":
                print("They seem to take what you had to say seriously and buy another round of ale.")
                tavern.profit(50)
            if result2 == "3":
                print("All of the customers in the tavern seem a little offput by your shoutting. You feel as though there is a shift in the atmosphere.")
                bard.happiness -= 1
        if result == "3":
            print("You proceed through the day with no further incident.")
    
    # Waitress Event #
    elif this_event == 6:
        print("Early on in the evening you notice a customer heckling and  getting handsy with Ava. Usually Ava handles things herself fairly well, but for some reason she seems to just be letting it happen. You ask her about it, and she seems really flustered. She mentions that the customer in question is actually her ex boyfriend. Apparently they had a really bad breakup a few weeks ago and he has decided that tonight he is going to do his best to make her life hell.")
        flavor_text = "\nWhat do you do?"
        choice1 = "1 - Send Ava home."
        choice2 = "2 - Tell Ava that you will take care of him."
        choice3 = "3 - Tell her to buck up and do her job, her personal life shouldn't be affecting her work."
        result = player_input(flavor_text, choice1, choice2, choice3)
        if result =="1":
            print("You think you can handle the rest of the night without her and suggest that she slips out the back that way she can avoid him following her. She thanks you and takes her leave.")
            waitress.happiness += 1
        if result =="2":
            flavor_text_2 = "\nWhat do you do?"
            choice1_2 = "1 - Tell the customer that it's time he leaves."
            choice2_2 = "2 - Explain to the customer that if he doesn't leave Ava alone, there will be consequences."
            choice3_2 = "3 - Words are for chumps, pick him up and throw him out onto the street."
            result2 = player_input(flavor_text_2, choice1_2, choice2_2, choice3_2)
            if result2 == "1":
                print("The customer leaves the tavern, but tells Ava he will be back.")
            if result2 == "2":
                print("The customer scoffs at you but leaves the tavern vowing to never return.")
                waitress.happiness +=1
                tavern.karma +=1
            if result2 == "3":
                rint = random.randint(1,2)
                if rint == 1:
                    print("You pick him up before he even knows what's happened and send him ass of teakettle. Ava seems grateful and you feel good about your choice.")
                    waitress.happiness += 1
                    tavern.karma += 1
                if rint == 2:
                    print("You go to pick him up and realize he is much heavier than he looks. You are unable to pick him up. In response he stands up and before you know it you know it the whole tavern erupts into a big brawl. After the fight, Ava seems annoyed that you butted into her business and made things worse. It costs you 200gp in repairs.")
                    waitress.happiness -= 1
                    tavern.gp -= 200
        if result =="3":
            print("Ava starts to cry, which makes you feel a little bad, but you mean what you said.")
            waitress.happiness -= 2
            tavern.karma -= 1
        
    # Weather Event #
    elif this_event == 7:
        print("You would think it was a slow day as the weather outside has steadily been growing worse and worse but that doesn't seem to stop your patrons. You hear lots of thunder and can hear the sound of the blusterous wind and torrential rain. You step up to the window to gaze outside at the nasty weather and you see a stagecoach that appears to be struggling, but slowly advancing towards your tavern. You feel bad for them out in that rain, but are happy that it looks like you may soon have some customers.")
        print("\nSuddenly one of the wheels on the stagecoach shifts and bends leaving the travelers stranded. After a few minutes the people who were on the stagecoach come stumbling in. You see there are a total of five of them. The five of them come in and ask if there is any way they can stay there until the storm dies down since the wheel on their stagecoach is bent and will need to be fixed before they can continue on their pilgrimage. You know full well that they don't have much of a choice in being able to go elsewhere. The normal price for what they are going to want is about 60gp.")
        flavor_text = "\nWhat is your response?"
        choice1 = "1 - Tell them you are happy to be of service while also charging them double since they don't have any other options."
        choice2 = "2 - Tell them of course and giving them the normal pricing."
        choice3 = "3 - Tell them you would be happy to help out, and give them a good discount on everything since they can't help needing to make this stop."
        result = player_input(flavor_text, choice1, choice2, choice3)
        if result =="1":
            print("The travelers seem to realize what you are doing, but realize they don't have much of a choice and begrudgingly pay you the 120gp.")
            tavern.karma -= 1
            tavern.profit(120)
        if result =="2":
            print("The travelers pay you the normal rate of 60gp and the night goes on as normal.")
            tavern.profit(60)
        if result =="3":
            print("The travelers are extremely grateful for your hospitality and pay you the 30gp. You hear them telling other patrons of your kindness.")
            tavern.karma += 1
            tavern.profit(30)

    # Bewitcher Event #
    elif this_event == 8:
        print("It's midday and so far it's been seeming like it's going to be a pretty uneventful day. That is, until a beautiful half elven woman walks into the Boars Head. She catches the eye of every man and even some of the women. She seems content to herself in the corner of the room. Your bard, Clarence is very clearly smitten with her the moment she walked in and proceeds to start serenading her becoming the new focus of his inspiration. She hasn't yet purchased anything herself, but it seems that most of the men in the tavern have gone out of their way to start migrating towards her and buying her food and drinks. You can feel a slight pull in the back of your mind to do the same, and can't help but feel like she may be up to no good.")
        flavor_text = "\nWhat would you like to do?"
        choice1 = "1 - Confront her and tell her if she doesn't stop whatever it is she is doing, then she is going to have to leave."
        choice2 = "2 - Demand that she leave right away."
        choice3 = "3 - Let her do what she wants, people are still spending money and after all that’s what the tavern is here for."
        result = player_input(flavor_text, choice1, choice2, choice3)
        if result =="1":
            print("As you are confronting her, you feel a sudden strong pull in the back of your mind that you are powerless to resist. You black out and suddenly come to later in the night in your back room. Upon awakening, you realize she is gone and your safe from the previous nights is empty. She cleaned you out but didn't touch the money at the register.")
            tavern.gp = 0
        if result =="2":
            print("Immediately after you demand that she leaves you motion to Clarence to help escort her out. She stands to leave and out of nowhere kisses Clarence. All of a sudden you see Clarence's expression of trying to act tough and imposing swap to being kind and caring. You realize that he was just charmed. As she heads for the door, she snaps her fingers and Clarence starts strumming on his lute while following her and he starts singing \"Toss a coin to the Bewitcher oh tavern of plenty…\" A few hours later, Clarence returns but he seems different, as though the happiness was sucked right out of him.")
            bard.happiness = 0
        if result =="3":
            print("She seems to have her fun and then leaves alone. You made an extra 100gp than what you would have normally.")
            tavern.profit(100)
    
# End of Day #
def end_of_day():    
    print("End of day summary:")
    print("You pay the Waitress: ", waitress.wage, "gold pieces")    
    print("You pay the Bard: ", bard.wage, "gold pieces")
    tavern.end_of_day(waitress,bard)

# Payroll Event #
def payroll():
    print("Currently the Boars Head has plenty of supplies. Your staff includes a waitress, and a bard.")
    print("\nAs in any business your choices as the boss change the way your employees approach their work. Just remember the happier your employees are, the more productive they will be.")
    print("You have just hired a new waitress named Ava. Ava is a local of the town whose family has come on hard times. As a result she was more than happy to accept the job offer before you had even discussed pay.")
    flavortext = "\nYou must now decide how much you are going to pay Ava . . ."
    choice1 = "\n1 - 25gp per day"
    choice2 = "2 - 50gp per day"
    choice3 = "3 - 75gp per day"
    waitress_choice = player_input(flavortext,choice1,choice2,choice3)
    print("You also have a bard named Clarence, he is a man of many talents and excels at playing a wide selection of instruments. Clarence used to play for tips, but you have seen him as a valuable asset and it would be a shame to lose him.")
    flavortext = "\nYou must now decide how much you are going to pay Clarence . . ."
    choice1 = "\n1 - 10gp per day"
    choice2 = "2 - 25gp per day"
    choice3 = "3 - 50gp per day"
    bard_choice = player_input(flavortext,choice1,choice2,choice3)
    if waitress_choice == '1':
        waitress.wage = 25
    if waitress_choice == '2':
        waitress.wage = 50
    if waitress_choice == '3':
        waitress.wage = 75
    if bard_choice == '3':
        bard.wage= 50
    if bard_choice == '2':
        bard.wage = 25
    if bard_choice == '1':
        bard.wage = 10
    waitress.happiness = (int(waitress_choice) *2)
    bard.happiness = (int(bard_choice) *2)

# Monday - Wimpy Event #
def wimpy_event():
    print("Around midday, a dopey looking man walks in to the tavern. You overhear him boasting about how he is about to come into some money, but don't quite catch the details. He looks ragged and gaunt as though he hasn't eaten a full meal in days. He eventually finds his way up to the bar and asks for food and ale. You ask him if he wants to open a tab or pay upfront. The man gets a little sheepish and says \"Please sir I will gladly pay you Tuesday for food and ale today.\"")
    flavor_text = "\nWhat would you like to do?"
    choice1 = "1 - Take pity on the man and let him have the food and ale he ordered, but that is all he can have until he pays."
    choice2 = "2 - Tell him this is a tavern not a church, there are no free handouts here, but if he comes across some coin then he is welcome to come back."
    choice3 = "3 - You are feeling generous and decide to allow him to eat and drink to his hearts content knowing full well that you will likely not get any money."
    result = player_input(flavor_text, choice1, choice2, choice3)
    if result == "1":
        print("The man is grateful and makes a promise that he will return tomorrow with the gold. To which he never does, but after all you had expected as much.")
        tavern.karma += 1
        tavern.gp -= 10
    if result == "2":
        print("The man is dismayed and leaves. You never see him again but can't help but wonder if you did the right thing.")
        tavern.karma -= 1
    if result == "3":
        print("The man eats and drinks until he can consume no more. He then lets his disguise fall and you see that actually he is a high ranking member of the church of Pelor. You know that followers of Pelor believe there is no higher calling than helping those in need. This was all a test, and you passed! He blesses your tavern and pays you 30gp for the food and ale.")
        tavern.karma += 2
        tavern.profit(30)

# Friday - Missing Boarder Event #
def missing_boarder():
    print("Earlier in the week, you had a visitor named Juan Tallman registered for a room and paid upfront for the whole week asking not to be disturbed. It was late when they arrived and you didn't get a good look at them, just that they were tall and were wearing a trench coat. Neither you nor your staff have seen them since they checked in four days ago and you are a bit concerned for their wellbeing.")
    print("You get to the top of the stairs and you knock on the door to their room. There is no response, but you hear some scurrying behind the door.")
    flavor_text = "\nWhat do you do next?"
    choice1 = "1 - Check the door to see if it is locked and if not then walk in."
    choice2 = "2 - Call out to the customer \"Juan, I am just doing a wellness check, I know you didn't want to be disturbed, but after not seeing you for four days I thought I should make sure you are alright and that you don't need anything.\""
    choice3 = "3 - Walk back downstairs. After all, the customer did ask not to be disturbed."
    result = player_input(flavor_text, choice1, choice2, choice3)
    if result == "1":
        print("The door isn't locked. You open the door wide open and hear the noise of scurrying. Inside you see what appear to be three kobold children scrambling to hide in different corners of the room with a trench coat laying next to the door. You Confront the children because it is clear to you now that Juan Tallman was really just the three kobold standing on each other's shoulders while wearing a trench coat. After a lot of probing, the children explain that their tribe had been marked as enemies of Waterdeep and the children had fled before an incoming invasion. The children look as though they have been homeless for some time and expect that they had to do many odd jobs to get enough money for this room.")
        flavor_text_2 = "\nWhat do you want to do in response to this information?"
        choice1_2 = "1 - Offer to let them live here as long as they like so long as they help around the tavern, doing odd jobs like washing dishes and sweeping the floors."
        choice2_2 = "2 - Hand them up to the guards so that they can deal with the kids how they see fit."
        choice3_2 = "3 - Tell them they are welcome to stay until their money runs out and then they have to go."
        result2 = player_input(flavor_text_2, choice1_2, choice2_2, choice3_2)
        if result2 == "1":
            print("The kids are excited at the prospect of having a place they can call home and promise to do the best they can to help out around the tavern.")
            tavern.karma += 1
        if result2 == "2":
            print("The guards thank you for your assistance in rounding up potentially dangerous individuals. You can't help but think that they are way over exaggerating and feel like you may have cursed the kids to a rough life. The guards pay you 50gp for your assistance.")
            tavern.karma -= 2
            tavern.profit(50)
        if result2 == "3":
            print("The kids thank you for your silence but are also slightly dismayed by the thought of going back to the streets.")
            tavern.karma -= 1
    if result == "2":
        print("You hear \"Everything's fine, now leave me alone!\" in response. You return downstairs and proceed like nothing happened. The rest of the night goes on with nothing out of the ordinary happening.")
    if result == "3":
        print("he rest of the night goes on with nothing out of the ordinary happening.")

# Ending #
def finale():
    if tavern.gp < 3000:
        print("It has come to the end of the week when the debt is due, you are worried as you haven't ammassed the gold required to pay off the debt. You gather what little gold you do have, and prepare for the debt collector to arrive.")
    else:
        print("It has come to the end of the week when the debt is due, you are pleased that you have ammassed the gold required to pay off the debt. You gather the money and prepare for the debt collector to arrive.")
    
    print("The debt collector from the Royal Bank of Waterdeep arrives at the bar, and you invite him to your office to conduct your business. The collector seems surprised to see you as he thought another man owned the tavern. You explain what transpired and the surprise to find out about the debt.")
    
    if tavern.karma >= 5:
        print("Just then you hear a knock at the door, the stranger is dressed in holy garments with the sigil of Pelor adorning them. He asks to speak on your behalf. He explains that they have heard of the good you have done for the people of Waterdeep and explain that they would like to help you out of your situation. The stranger then presents the debt collector with a bag of gold pieces and tells you both that the church of Pelor is thankful for your service to the community and wishes for it to continue. The stranger then turns and leaves leaving both you and the debt collector awestruck. The debt collecter finally breaks the silence and says... \"Well it seems as though the gods shine upon you. I will be sure to inform the council of what has transpired and that you are not the same man who was here before.\"")
        print("He then gives you a nod and a wave and heads out of the tavern. You did it! Based off your decisions you helped out enough people that word got around to your good deeds and the loan was repayed. You lean back in your chair and can't help but think of what the world has in store for you next.")
        print("\nCongratulations, you have successfully beaten Tavernmaster and recieved the good karma ending.")

    elif tavern.gp >= 3000:
        print("You pay the tax collector, and he seems happy that he doesn't have to close you down. He then gives you a nod and a wave and heads out of the tavern. You did it! You lean back in your chair and can't help but think of what the world has in store for you next.")
        print("\nCongratulations, you have successfully beaten Tavernmaster and recieved the payoff ending.")
    else:
        print("The debt collector sighs, this is his least favorite part of the job. He lets you know that you have until the end of the day to settle your affairs and vacate the premises. You can't help but feel as though you did something wrong along the way and that you should have been able to meet the deadline. You decide maybe I should just stick to adventuring and leave the business running to the professionals.")
        print("\n Unfortunately you have failed to beat Tavernmaster. Better luck next time.")
    
    print("    Stats for your playthrough    ")
    print(f"\nEnding Karma: {tavern.karma}")
    print(f"Ending Gold: {tavern.gp}")
    print(f"Waitress Happiness: {waitress.happiness}")
    print(f"Bard Happiness: {bard.happiness}")
    input("Press enter to continue . . .")