#defs

    ## raceAndClass
    ## function which accepts 2 lists and 1 number
    ## and returns a random unique mix of the lists
    ## in the form: return[[a,b][a,b]... c times]

def raceAndClass(list1, list2, amount):
    finalList = []
    while amount != 0:
        
        index1 = random.randint(0,len(list1) - 1)
        index2 = random.randint(0,len(list2) - 1)

        finalList = finalList + [list1[index1],list2[index2]]
        
        del list1[index1]
        del list2[index2]
        
        amount = amount-1
        
    return finalList


#imports
import random, sys, os, math


#vars
startPoint = ''
    #intro
myName,myAge = '', 0
    #grove
journey,day = 0,0
    #sphinx
offering,tries = 0,0
    #assassin
nights,totalA = 0,0
    #revenge
waves,totalW = 0,0
    #guess
secret = 0
    #lists
        #first, the arrays themselves
raceList = ['lashunta', 'cecaelia', 'drow', 'centaur', 'ogre', 'vampire', 'gargoyle', 'spirit-kin', 'ancient', 'undead', 'sentient item']
classList = ['mage', 'artist', 'warrior', 'occultist', 'inquisitor', 'seer', 'theurge', 'dancer', 'savage', 'duelist']
roleList = [['a despot', 'formidable', 'monster'], ['virtuous', 'friend', 'euphoric']]
        #then, specific instances
todaysChars = raceAndClass(raceList,classList,3)
raceChar, classChar, raceInterest, classInterest, raceRival, classRival = todaysChars #dont think i need todaysChars but i like it for now
roleChar = roleList[random.randint(0,1)][random.randint(0,1)+random.randint(0,1)]


#lists
print('Today, you are a ' + raceChar + ' ' + classChar + '.')
print('You are called ' + roleChar + ' by those that have known you.')
print('You have two old acquiantances...')
print('An old rival of yours, a ' + raceRival + ' ' + classRival + '.')
print('And a former interest, a ' + raceInterest + ' ' + classInterest + '.')


#menu
print('')
print('Where shall we pick up?')
print('intro, grove, sphinx, assassin, revenge, guess, new?')
startPoint=input()

print('Picking up where last we left off...')
print('')

# an if function to skip around to parts i want to test
if str(startPoint)=='intro':
    startPoint='grove'
    
    #intro, basic vars
    print('"Ha! Good morning!"')
    print('')
    print('"You there, who are you?"')
    myName = input()
    print('"Greetings, "' + myName + '", your title is:"')
    print('"' + str(len(myName)) + ' runes long!"')
    print('')
    print('"How many seasons have you seen?"')
    myAge = input()
    try:
        print('"You will have lasted ' + str(int(myAge) + 1) + ' in a few weeks! Ha!"')
    except:
        print('"Ah.. alright then.."')

        
    print('"Be along now! There is much to be done!" And so, you travelled.')
    print('')

if str(startPoint)=='grove':
    startPoint='sphinx'
    #grove, if statements, a while loop
    print('After some time, you arrive at the grove. The tallest tree speaks.')
    if myName == 'Usamrah':
        print('"Welcome, Waterspeaker"')
        print('"Give Aeryll our tidings."')
    elif myName == 'Aeryll':
        print('"Where is the heir? You must be by her side!"')
    elif myName == 'Jorgen':
        print('"What a fine gentleman you are."')
    elif myName == 'Pigeon':
        print('"You know what you have done. This is no home to you, betrayer."')
    elif myName == 'Laksha':
        print('Or, it would have spoke, if your soldiers hadnt burned this place some time ago.')
    else:
        print('"Pleasure to meet you. Queens grace to you."')
        print('"Be on your way, now."')
    print('')
    
    print('The road is not well travelled this time of year. How many days travel?')
    journey = input()
    try:
        if int(journey) >= 0:
            print('And so')
    except:
        journey = 3
    print('You set out, travelling once again.')
    day = 0
    while day < int(journey):
        print('...and on...')
        day = day+1
    print('Until finally you arrive!')
    print('')

if str(startPoint)=='sphinx':
    startPoint='assassin'
    
    #sphinx, while loops
    print('The sphinx awaits you.')
    print('"Do you have what I require?", it asks you.')
    offering = input()
    tries = 0
    while offering != 'a riddle':
        print('"No! You know what I desire!"')
        offering = input()
        if offering == 'a pun':
            print('"Clever try. Almost, but..."')
            continue
        tries = tries+1
        if tries > 2:
            print('"You bore me." The sphinx slashes at you, and leaves you beside the road.')
            sys.exit()
        elif tries != 0:
            if tries == 1:
                print(str(tries) + ' try...')
            else:
                print(str(tries) + ' tries...')
    print('The creature gives a toothy grin of delight, and soars away.')
    print('')

if str(startPoint)=='assassin':
    startPoint='revenge'
    
    #assassins, for loops 1
    print('Some time later, assassins came.')
    print('For how many nights?')
    nights=input()
    totalA=0
    for a in range(int(nights)):
        print('On the first night, they sent ' + str(a+1) + '.')
        totalA=totalA+a+1
    print('But to no avail!')
    print('You slew ' + str(totalA) + ' in all!')
    print('')

if str(startPoint)=='revenge':
    startPoint='guess'
    
    #revenge, for loops 2
    print('Whether from rage or a desire to see the conflict ended, you took revenge on them at their monastery.')
    print('How many waves?')
    waves=input()
    totalW=0
    for w in range(10, 10+5*int(waves), 5):
        print('And then ' + str(w) + ' came, but you denied them.')
        totalW=totalW+w
    print('When it was all done, ' + str(totalW) + ' had come against you and been defeated.')
    print('')

if str(startPoint)=='guess':

    #guess, a little game using random module
    print('Some time later, after you had left the ruins of the monastery behind,')
    print('you were making your soup on a cold, windy night...')
    print('...when a spirit showed itself to you.')
    print('')
    print('"...Hey! Hey! Whats your name, strangeling??"')
    print('"..."')
    if myName=='':
        print('"...! oooooh, how mysterious."')
    else:
        print('"' + str(myName) + ', huh? Nice ta meetcha!"')
    print('')
    print('"I have a lil game for ya' + str(myName) + '..."')
    print('"I am thinking of a number between 1 and 20! Guess! Give ya 6 tries."')

    secret = random.randint(1,20)
    for guessesTaken in range(1,7):
        print('"Go on! Give us a try, now!"')
        guess = int(input())
        if guess < secret:
            print('"Noooo, too low!"')
        elif guess > secret:
            print('"You trying to make up for something? Too big!"')
        else:
            break #this is the right guess!
    if guess == secret:
        print('"Awww, ' + myName + ' howd ya know!? Youre a clever one..."')
    else:
        print('"Nyeh heh heh heh, it was ' + str(secret) + '! Hah!"')

if str(startPoint)=='new':
    print("Nothing here yet.")    
