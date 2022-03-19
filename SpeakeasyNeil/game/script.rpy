# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define next_chapter = 0
# The game starts here.

label start:
    $ renpy.music.play('main_theme.mp3', channel=u'music', loop=True, fadein=True)
    python:
        fName = renpy.input("What is your first name?")
        lName = renpy.input("What is your last name?")
    scene station
    show screen button_overlay
    show me prol at mid_zoom
    "I climbed off the express train at LaSalle Street Station in Chicago, still wondering how I got myself into this..."
    show me prol worried at mid_zoom
    "(Shipped out to live with my stuffed-shirt of an uncle...)"
    show me prol sideways at mid_zoom
    "(Just because I bobbed my hair and snuck out to one party!)"
    show me prol worried at mid_zoom
    "(Uncle Charlie was all right when I was a kid…but last time we saw each other, I was twelve!)"
    show me prol at mid_zoom
    "The station was packed with lots of high society going about their business, none who gave a second glance my way."
    show me prol sideways at mid_zoom
    "(If Momma hadn’t dressed me like a librarian, I bet I’d be getting some glances from some of these upstanding types!)"
    show me prol at mid_zoom
    "(Vince…something, one of Uncle Charlie’s assistants is supposed to pick me up.)"
    show me prol worried at mid_zoom
    "(Probably some pot-bellied geezer in spats and a high-band collar!)"
    scene station_street
    with fade
    pause
    "After weaving through the crows, I burst out of the terminal into the sun."
    show me prol surprised at mid_zoom
    "(This town is hoppin’! I’ve never seen so many cars…! It’s all real impressive!)"
    hide me
    "(Especially that sharp-looking guy in the fedora perched on top of that fancy car.)"
    show me prol worried at mid_zoom
    "Just then, a car whizzed past, hitting a sinkhole and sending the contents of the puddle all over my heavy skirt."
    dri "HEY! Watch it lady! I’m driving here!!"
    show me prol irritated at mid_zoom
    "(Just great…)"
    show me prol worried at mid_zoom
    "I couldn’t very well go walking around with a soggy skirt, so I lifted it ever so slightly to wring the water out."
    window hide
    show vince_prologue at character_zoom
    $ renpy.pause(3, hard=True)
    window show
    "I heard the catcall come from the man with the fedora, who was now rolling a cigarette."
    q "Nice gams, doll! Looks like they go on for miles!"
    "(Wait a minute. The sign propped up on the front grill…that’s my name!)"
    "(Could that be Vince…?)"
    q "Hey, what, you [fName]?"
    me "Who\'s asking?"
    vince "Name’s Vince Moretti. I’m an associate of your uncle\'s."
    "(Oh? Things are definitely looking up. Nice suit with a tie to match.)"
    "(A pretty face underneath the hat… and that car!)"
    hide vince_prologue
    hide me
    show me prol at ls_mid
    me "You look Italian. Poppa always said never to trust Italians."
    me @ prol sideways"'They\'ll steal you blind while they\'re shakin\' your hand,' he said."
    hide me
    show vince p1 grin at ls_mid
    "Vince slid down the side of the hood and leaned against the car, lighting his cigarette."
    vince @ p1 smirk "You always listen to your pa?"
    hide me
    hide vince
    menu listen_pa:
        "Don\'t pick B or C for now - texts works but no sprites."
        'A: "I\'m a good girl."':
            show me prol at ls_left
            show vince p1 grin at ls_right
            me "I\'m a good girl."
            show me prol sideways
            vince p1 smirk "How\'d you end up here, then?"
            me prol "Well, you can say I\'m misunderstood."
            vince "Meaning your folks stopped believing your stories?" # Missing toothy smile
            show vince
            me @ prol sideways "Hey, at least I got the brains to make up stories!"
            show me prol irritated
            "It was a cheap shot, but after all it was none of his business!"
            show me prol
            vince @ p1 smirk "Like the Frenchmen with their fancy swords say: touche, doll."
            hide me
            show vince p1 grin at ls_mid
            vince "You got me."
            "He slapped his hands to an imaginary wound in his chest."
        'B: "Almost never."':
            me "Almost never."
            vince "Haha! Like I figured. From what I heard, you wouldn\'t be here if you was a listen-to-Papa kind of gal."
            me "You sure got a smart mouth."
            vince "No one ever washed it out for me."
            me "You daring me to try?"
            vince "Not \'cause it don\'t sound like fun... but Charlie\'d have me in a sling."
        'C: "How\'s that your beeswax?"':
            me "How\'s that your beeswax?"
            vince "Ain\'t sayin\' it is, but a guy can be curious."
            me "A guy can be fresh."
            vince "Oh, well, how \'bout that!"
            vince "Not only is she a looker, but she\'s quick with the quips!"
            "(He's got a nice smile. Is he making eyes at me? Might just be all right if he is.)"
    show vince p1 grin at ls_right
    show me prol smile at ls_left
    vince "That haircut you\'re sportin\' under that chicken platter tells me you don\'t listen to your ma much either."
    hide vince
    show me nhprol at mid_zoom_small
    "I pulled off the big, feathered hat Momma had nailed on my noggin with hatpins."
    hide me
    show vince at ls_right
    show me nhprol sideways at ls_left
    me "Gimme a break, will ya? I listened to her harping for the last week."
    show me nhprol
    "Vinced peeked at me from under his hat and grinned." # Missing toothy smile
    me nhprol @ sideways "So, you gonna get my bags or stand there like a stooge admiring my wardrobe?"
    hide me
    show vince at ls_mid
    "He sauntered over and grabbed my suitcases, stowing them in the back of the car."
    hide vince
    show me nhprol at ls_mid
    "I tossed my hat after them."
    show vince p1 grin at ls_right
    show me nhprol smile at ls_left
    me "So just how fast can this car go?"
    show vince at ls_mid
    hide me
    "He chuckled and shook his head, then took down the canvas top, grinning all the while." # Missing toothy smile
    vince @ p1 grin "Looks like dear old Uncle Charlie\'s got his hands full."
    scene car_street
    with fade
    pause
    show me nhprol surprised at ls_right
    show vince p1 grin at ls_left
    "A few minutes later, we were in traffic, me trying to get a good look at everything without looking like a country bumpkin."
    show me nhprol
    vince "That's the new Wrigley Building. Thrity stories."
    vince "The Tribune Tower's gonna be across the street. Thirty-six floors."
    show vince
    show me nhprol surprised
    "He was pointing to the biggest building I'd ever seen."
    show me nhprol
    "I tried to go off all casual, \' cause he was watching for my reaction."
    vince @ p1 grin"Hey, you wanna see Comisky?"
    me @ nhprol worried "What\'s that?"
    vince @ p1 smile "Comisky Park! Home of the Sox! Don\'t you follow baseball?"
    me "The Yanks, sometimes. I\'m not a fanatic about it."
    show me sideways
    vince @ p1 grin "No danger of becoming a fanatic at a Sox game."
    vince @ p1 grin "They ain\'t the same since the scandal. I\'ll take you sometime."
    me @ nhprol "You think Uncle Charlie\'s gonna go for that?"
    vince @ p1 smirk "What he don\'t know can\'t hurt him."
    me "What he finds out might hurt you, though."
    show me nhprol
    # Missing Vince toothy smile
    "(He's got a nice laugh...wide-open and free.)"
    show vince p1 grin
    me "So, tell me. Is Uncle Charlie the same?"
    show vince
    me "I mean, he was always a good egg to me as a kid, but a bit of a moralist, y\'know what I mean?"
    vince "Charlie? Still an upright citizen."
    show me nhprol worried
    vince @ p1 grin "Anti-Saloon League, big wheel Rotarian and in the front pew every Sunday!"
    show me nhprol sideways
    vince @ p1 grin "How about you. What got you this sentence?"
    "(Can I trust this guy? He seems okay but...aw, what\'s the harm?)"
    me @ nhprol "Chopping off all my hair was the start."
    me "Momma was livid, but she was settling down..."
    me @ nhprol "...and then Teddy Denby invited me to this dance down at the armory..."
    # Missing Vince toothy smile
    show me nhprol smile
    "Vince exploded in laughter."
    me @ nhprol sideways "Hey! You gotta get your fun any way you can, when you're growing up in East Nowhere."
    show me nhprol
    vince "Hope you an\' ol\' Teddy had a good time."
    me @ nhprol smile "Teddy was a bust, but the dance part was all right."
    me @ nhprol sideways "Everything seemed to go my way, until I had to mess up and get caught sneaking back in."
    vince @ p1 smirk "That\'s the whole deal? You just snuck out and got collared?"
    # Missing Vince toothy smile
    me nhprol sideways "Well...there might have been some gin involved."
    vince "Oh-ho! Well, you won\'t be getting into the hooch with Charlie keeping an eye out, that\'s for sure."
    me @ nhprol worried "I guess he\'s going to put me to work at his dusty old appliance store in between prayer meetings..."
    show vince p1 grin
    show me nhprol
    "Vince gave me a look I couldn't quite figure."
    vince "Could be worse. Believe me. All Charlie wants is to do right by folks."
    scene house_day
    with fade
    pause
    "(Holy smoke, what a house! Guess the appliance business is booming.)"
    show charlie smile
    "I got my hat back in place just as the man himself burst out the front door."
    ch "[fName]! Heavens, you\'ve grown into a lovely young woman!"
    show charlie smile at ls_left
    show me prol at ls_right
    "(More gray around the ears, but the same ol\' Uncle Charlie...)"
    ch "From what your mother said in her letter, we\'ve snatched you from the very grasp of Satan."
    show charlie
    me @ prol smile "You know Charlie, it was just a dance..."
    show me sideways
    "Uncle Charlie pursed his lips in disapproval, looking under my hat."
    ch "You even cut off your beautiful long hair to imitate those...what are they calling them...?"
    show charlie smile at three_left
    show me prol worried at ls_mid
    show vince at three_right
    vince "Flappers. Like in that Clara Bow picture."
    hide charlie
    show me prol irritated at ls_left
    show vince p2 at ls_right
    "I shot Vince the you-ain\'t-helping look."
    show vince p1 smirk
    "He flashed me a smile and a wink that said he knew it already."
    hide me
    hide vince
    show charlie at ls_mid
    ch "What a mess! No niece of mine is going to become a gin-joint floozy!"
    show me prol worried at ls_right
    show charlie smile at ls_left
    ch "Come inside. I've got a good book for you to study..."
    hide charlie
    show me prol worried at mid_zoom
    "(Ugh. I\'m betting it\'s temperance literature...)"
    hide me
    show charlie at ls_left
    show me prol worried at ls_right
    "Uncle Charlie took me by the elbow and steered me into the house."
    hide charlie
    hide me
    show vince at ls_mid
    "I could\'ve sworn I caught Vince smirking as he followed with my bags."
    scene living_day
    $ renpy.music.play('sad.mp3', channel=u'music', loop=True, fadein=True)
    with fade
    pause
    show me nhprol worried at ls_left
    show charlie at ls_right
    "Uncle Charlie sent Vince off, then sat me down the living room and started in."
    hide me
    show charlie at ls_mid
    "For twenty minutes, he gave me what for on the evils of demon rum, jazz, and fast company."
    hide charlie
    show me nhprol worried at mid_zoom
    "(Guess we're past the magic tricks or Sunday funnies.)"
    scene room_day
    with fade
    pause
    "After he ran out of steam, he set me to unpacking before hoofing it to his office downtown."
    show me nhprol worried at mid_zoom
    "(This room\'s like Queen Victoria\'s overstuffed parlor! I can\'t stand it!)"
    show me nhprol sideways
    "(Wasn't there a movie theater  few blocks over, showing the new Elliot Graham picture?)"
    show me nhprol2
    $ renpy.music.play('funaction.mp3', channel=u'music', loop=True, fadein=True)
    "I changed out of the get up Momma\'d insisted on before she\'d let me get on the train, and into something fit to be seen in."
    show me prol2
    "(I gotta show Uncle Charlie I\'m not going to be a prisoner... even if he gets mad...)"
    show me prol2 smile
    "(I\'m too young to be stuffed in a tomb like King Tut! Besides, he didn\'t exactly say I couldn\'t leave...)"
    scene gladius_day
    with fade
    pause
    show me prol2 smile at ls_mid
    "The picture was \"Girl Trouble\" and it was good. Afterwards, I walked out of the theater entrance..."
    "...still dreaming about being the girl troubling Elliot Graham...when someone pushed into me from behind."
    show me prol2 surprised
    "I stumbled...and was caught by a pair of strong arms attached to a broad chest and chiseled jaw."
    hide me
    q "Well, it\'s not every day I get to sweep a beautiful girl off her feet...even though I didn\'t exactly do the sweeping."
    show me prol2 sideways at ls_mid
    me "Pull the other one. I bet you\'re a regular artist with the broom."
    hide me
    window hide
    show elliot_prologue at character_zoom
    $ renpy.pause(3, hard=True)
    window show
    q "You have the wrong idea, my dear."
    me "Can it, handsome. Modesty fits you like a Santa suit on Charlie Chaplin."
    "He flipped a little square of paper out of his breast pocket and handed it to me."
    q "I fancy your style."
    q "I must be on my way now, but I shall be going to the address on this card later."
    q "I would be absolutely delighted to continue this conversation there."
    "I took the card without thinking, mostly because he was smiling at me with every tooth in his mouth..."
    "(And darned if he doesn\'t STILL look like...)"
    hide elliot_prologue
    q "I\'m Elliot, by the way."
    show me prol2 sideways at mid_zoom
    "(Huh. What are the odds?)"
    scene house_night
    with fade
    pause
    $ renpy.music.play('main_theme.mp3', channel=u'music', loop=True, fadein=True)
    "Uncle Charlie was still out when I got home. I wondered where he was for a moment, but I had better things to do."
    #### CHOOSE YOUR LOOK ####
    window hide
    call screen ls_cards
    label dress_choice:
        if dress == "normal":
            "I changed into my brand new dress, touched up my face, and called a cab to take me to the address on the card."
        else:
            window hide
            show dress_15 at outfit_zoom
            pause
            hide dress_15
            window show
            show me prolf at ls_mid
            "I changed into my only other good dress, touched up my face and called a cab to take me to the address on the card."
    scene store_night
    with fade
    pause
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(Uncle Charlie\'s appliance store?!)"
    hide me
    if dress == "normal":
        show me prolp worried at ls_mid
    else:
        show me prolf surprised at ls_mid
    me "Hey, Mister...you sure this is the right place?"
    cab "I bring you where you tol\' me. Store\'s closed."
    if dress == "normal":
        show me prolp worried at ls_mid
    else:
        show me prolf worried
    "I paid the man and stepped out onto the street, wondering what to do..."
    "I saw a couple heading my way...but then they ducked into the alley beside the store."
    if dress == "normal":
        show me prolp worried at ls_mid
    else:
        show me prolf surprised
    "(Where\'re they going?)"
    scene icebox_entrance
    with fade
    pause
    "I rounded the corner just in time to see the couple disappearing into a door on the side of the building."
    if dress == "normal":
        show me prolp worried at ls_mid
    else:
        show me prolf at ls_mid
    "(Well, what\'ve I got to lose?)"
    scene icebox_entrance_peep
    "I knocked on the door. A peephole slid open and a single pale eye appeared."
    if dress == "normal":
        show me prolp worried at ls_mid
    else:
        show me prolf surprised at ls_mid
    me "I um...got a card from a fella who said he\'d meet me at this address?"
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    me "He said his name was Elliot."
    if dress == "normal":
        show me prolp worried
    else:
        show me prolf worried
    "I flashed the card that Elliot gave me earlier, and the door flew open, emitting a burst of noise and smoke."
    scene dance
    with fade
    pause
    $ renpy.music.play('funaction.mp3', channel=u'music', loop=True, fadein=True)
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(It's a speakeasy! But...right under Uncle Charlie\'s store?!)"
    "I made my way across the hubbub of patrons to a bar worthy of Rockefeller."
    "(How can Uncle Charlie be so far off the beam he doesn\'t know THIS is going on right under his blue nose?)"
    hide me
    scene bar
    show doneil_prologue at character_zoom
    $ renpy.pause(3, hard=True)
    window show
    "Two guys were seated at opposite ends of the bar."
    "One seemed cool like an iceberg..."
    "...the other dark and coiled like a spring..."
    "Iceberg gave me the quick once over, then went back to his drink, muttering."
    q "Julius still auditioning singers? Two\'s not enough?"
    hide doneil_prologue
    if dress == "normal":
        show me prolp surprised
    else:
        show me prolf surprised
    me "I\'m not...I don\'t even--?"
    hide me
    show donovan p1 pursesmirk at ls_left
    show neil fs2 at ls_right
    "Coiled Spring, whose eyes lingered where Iceberg\'s glanced off, kicked in his two cents."
    q "Don\'t mind Neil. He plays at being a man o\' mystery, but Doc\'s just a cold fish."
    hide donovan
    hide neil
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(So Iceberg\'s some kind of doctor named Neil. Okay...)"
    hide me
    if dress == "normal":
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    me "And you...?"
    if dress == "normal":
        show me prolp smile at ls_left
    else:
        show me prolf smile at ls_left
    show donovan p2 pursesmirk at ls_right
    q "Me? Darlin\' I'm the answer to your prayers...I got credit at the bar."
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    d "Name\'s Donovan Gallagher."
    me "I love your accent by the way! Are you English?"
    if dress == "normal":
        show me prolp surprised
    else:
        show me prolf surprised
    show donovan p2 serious
    "The corners of his mouth took a quick turn south."
    hide me
    hide donovan
    show neil fs2 smirk
    n "Kid, never mistake a Mick for a Brit. Liable to wake up dead."
    show neil fs2 smirk at ls_right
    show donovan p2 angry at ls_left
    "Donovan shot daggers at Neil."
    d "Shut up, Dresner. The kid don\'t know better."
    hide neil
    show donovan p2 pursesmirk at ls_right
    if dress == "normal":
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    d "By the way, where ya from?"
    me "Little burg just north of Nothing."
    d "Well then lassie, lemme be the first ta\' buy you a drink to commemorate your arrival."
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    "Donovan cocked his head a little, and shouted without taking away his gaze from mine."
    d "Hey, Cliff!"
    show cliff_prologue at character_zoom
    "The bartender blew through the doors from the backroom, carrying a case of whiskey like it was full of feathers."
    "(Geez! Another fine specimen! Look at those shoulders!)"
    c "What\'cha need, Donovan? I got a mess back here I gotta..."
    "He stopped and gave me the look I was starting to recognize."
    "(These city boys sure aren\'t shy!)"
    hide cliff_prologue
    hide donovan
    show cliff p2 smile at left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    me "What kind of mess?"
    c "Well, y\'know. Stuff coming in, stuff going out, profits, losses. It\'s business stuff."
    show cliff p2 grin
    c @ p2 grin "Nothin\' for a lady patron to be concerned about, that\'s for sure."
    show cliff p2
    hide me
    show donovan p2 pursesmirk at ls_right
    d "Ha. Nothing\' you learned about in your institution neither."
    show donovan p2 blush
    d "Do your job and wet our whistles already!"
    show cliff p2 smile
    show donovan p2 blush at ls_mid
    "Donovan slapped him hard on his shoulder, and Cliff dropped the tally sheets clutched in his hand."
    hide donovan
    show cliff p2 smile at center
    "Surprisingly, Cliff started picking up the papers without retort, or a change in his pleasant expression."
    show cliff p3 smile at left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    "Feeling bad and out of sympathy, I helped him out and noticed the haphazard writing on one of the sheets."
    show cliff p3 smirk
    if dress == "normal":
        show me prolp surprised
    else:
        show me prolf surprised
    me "Well, here\'s your problem..."
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    "I pointed to a couple of columns of figures that were transposed."
    me "You need a real spreadsheet, not this scribble. Look...here\'re your REAL inventory numbers..."
    show cliff p3
    "I nipped the pencil from his pocket and added up the columns in about twenty seconds."
    hide me
    show cliff p3 smirk at left
    show donovan p2 surprise
    show neil fs1 smile at ls_right
    "Cliff, Donovan, and Neil looked on, amazed at my parlor trick."
    hide cliff
    hide donovan
    hide neil
    if dress == "normal":
        show me prolp sideways at ls_mid
    else:
        show me prolf sideways at ls_mid
    me "Hey, it\'s not like I\'m a trained monkey!"
    if dress == "normal":
        show me prolp irritated
    else:
        show me prolf irritated
    me "I did two years at Mrs. Bradburn\'s Secretarial and Business College."
    show cliff p3 smirk at left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    c "Well, you sure are prettier than a trained monkey. How\'d you wind up here?"
    me "Funny story. Thee was this guy outside the picture show."
    show cliff p3 smile
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    me "I tell ya, he looked just like Elliot Graham! Anyway, he gave me this card..."
    hide cliff
    hide me
    show donovan p2 pursesmirk at ls_left
    show neil fs2 sideways at ls_right
    "I slid it across the bar. Neil and Donovan both snorted into their drinks."
    hide donovan
    hide neil
    show cliff p3 smirk at ls_mid
    c "Would it send you for a spin if I told you it WAS Elliot Graham?"
    hide cliff
    if dress == "normal":
        show me prolp surprised at ls_mid
    else:
        show me prolf surprised at ls_mid
    me "No! You\'re not pulling my leg?"
    hide me
    show donovan p2 pursesmirk
    d "He does a little recruiting for the management when he\'s in town."
    show donovan p2 pursesmirk at ls_left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    d "Never hurts business to have the pond stocked. How about that drink?"
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    me "Sure. Something with gin...but no bathtub stuff!"
    hide donovan
    hide me
    show cliff p2 smile
    "I watched with interest as Cliff made my drink."
    "I\'d never seen anyone make an honest to God cocktail before, but it didn\'t seem like all that much booze was going into it..."
    hide cliff
    show donovan p2 at ls_mid
    d "I see what\'cher doin\' there, Cliff! Make it full strength!"
    hide donovan
    show cliff p2 smile at left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    c "All right, but listen, keep your wits about you with this one."
    hide cliff
    hide me
    show donovan p2 pursesmirk
    d "Don\'be scarin\' the wee girl, Clifton."
    hide donovan
    show cliff p3 at left
    if dress == "normal":
        show me prolp smile at ls_right
    else:
        show me prolf smile at ls_right
    me "Say, Cliff, can I ask you something? Who owns this place, anyway? See, my uncle..."
    hide cliff
    show donovan p2 pursesmirk at ls_left
    "But as the place was filling up, he had to dash off. Donovan and I kept talking."
    show donovan p2 pursesmirk at ls_mid
    hide me
    "He was charming, my drink was strong, and I was having fun. Then the band started up."
    scene dance
    show julfia_prologue at character_zoom
    "A handsome young black man sat down at the paino and they kicked up {i}I\'m Somebody\'s Somebody{/i}."
    "(Wow! They\'re really good! That fella has a nice touch on the keys.)"
    "The rest of the band joined in..."
    "The singer, a real knockout, started singing in a clear alto, just a little rough on the edges..."
    "(Perfect for this kind of music.)"
    hide julfia_prologue
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "...and in a snap, the joint was jumping!"
    scene bar
    show donovan p2 pursesmirk at ls_left
    if dress == "normal":
        show me prolp smile at ls_right
    else:
        show me prolf smile at ls_right
    me "They\'re great! Who\'re they?"
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    d "The canary\'s Sofia Martinez, and Julius Harper on the ivories."
    "The dance floor was starting to fill up. I grabbed Donovan's hand."
    show donovan p2 surprise
    me "C\'mon, I do a mean Charleston."
    hide me
    show neil fs2 grin at ls_right
    n "Donovan never dances. Doesn\'t want you to see how much booze he\'s got on board."
    show donovan p2
    d "How \'bout you, Doc? You offerin\' to hop with the lady?"
    show neil fs1 sideways
    n "Ah...no...I..."
    show donovan p2 pursesmirk
    show neil fs1
    d "I thought so. Claims he\'s got a bum leg from the war. I think he\'s just a stiff."
    hide donovan
    hide neil
    show elliot p1 hat grin
    "Just then, Elliot Graham made an appearance, surrounded by a bevy of gorgeous women..."
    hide elliot
    show donovan p2 pursesmirk at ls_left
    if dress == "normal":
        show me prolp surprised at ls_right
    else:
        show me prolf surprised at ls_right
    d "Well, if it ain\'t the Great Lover himself."
    hide donovan
    hide me
    show elliot p1 grin
    "Elliot saw Donovan and started to move toward us, smiling broadly when he saw me."
    hide elliot
    show vince
    "His bevy stuck close and, mixed in with them was a familiar figure..."
    hide vince
    if dress == "normal":
        show me prolp surprised at ls_mid
    else:
        show me prolf surprised at ls_mid
    me "Vince?!"
    hide me
    show donovan p1 surprise
    d "You...know Vince?"
    hide donovan
    if dress == "normal":
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show elliot p1 beam at ls_right
    "I didn\'t have time to answer, or even to ponder what Vince\'s presence meant, because, excuse me...movie star!"
    e "Well! If it isn\'t the beautiful young lady from the picture show today!"
    e "I\'m so very glad you made it tonight! Would you fancy a dance?"
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    "I took another gulp of my drink."
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    show elliot p1 grin
    "Elliot\'s harem stared daggers at me as he took my hand and led me to the dance floor..."
    scene dance
    show julius
    "Julius saw Elliot and broke into the Charleston."
    hide julius
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    show elliot p1 grin at ls_left
    "He swept me into his arms and took me on a quick tour of the floor, our feet flying."
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    "(I\'m DANCING with Elliot Graham!)"
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    "(He\'s good...feels as smooth as it looks the movies. Elegant.)"
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    "(Guess that's the way they teach it across the pond...or maybe he learned it in Hollywood...)"
    hide me
    hide elliot
    show vince p2
    "As Elliot and I cut the rug, I caught glimpses of Vince."
    $ renpy.music.play('suspense.mp3', channel=u'music', loop=True, fadein=True)
    hide vince
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(Is he running this place on the sly?)"
    "(Is that how the Ice Box ended up under Uncle Charlie\'s store?)"
    "(Or is there more to Uncle Charlie than meets the eye?)"
    hide me
    scene bar
    show vince p1 stern at ls_left
    show cliff p3 at ls_right
    "When we finished the dance, Vince was at the bar, talking to Cliff. They were both looking my way."
    show cliff p3 angry
    "(Are they talking about me?)"
    hide cliff
    show vince p1 stern at ls_mid
    "Vince signaled to Elliot, who excused himself."
    show vince p1 stern at ls_left
    show elliot p1 smile at ls_right
    "I worked through the crowd to get close enough to eavesdrop."
    vince "You invited her?"
    e @ p1 grin "She is absolutely splendid, wouldn\'t you say?"
    show elliot p1 sideways
    vince @ p2 "The hottest. In more ways than one."
    hide elliot
    hide vince
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(Nice to know they think I\'m hotsy-totsy, but why is everyone looking like they stepped in Granny\'s petunias?)"
    hide me
    show vince p2 at ls_left
    show elliot p1 glance at ls_right
    e "What do you mean?"
    show vince p2 stern
    show elliot p2 surprised
    c "She\'s Charlie\'s NIECE, lunkhead!"
    hide vince
    show cliff p3 angry at ls_left
    show elliot p1 glance
    c "She\'s fresh off the train to get the temperance treatment, not a stiff belt of Elliot Graham!"
    hide elliot
    hide cliff
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(They ALL know Uncle Charlie? What is going on here?)"
    hide me
    show elliot p2 surprised at ls_mid
    "Elliot looked stunned, but then he caught me watching..."
    show elliot p1 grin
    "...and his expression slid seamlessly into that charming smile I knew so well from the pictures."
    hide elliot
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "Just then, a handsome fella sidled my way to ask if I wanted to dance."
    "(Guess that mystery\'ll keep. I still feel like dancing!)"
    $ renpy.music.play('main_theme.mp3', channel=u'music', loop=True, fadein=True)
    "I hit the floor again and danced away the rest of the band\'s set."
    scene dance
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "Sitting at the end of the bar, catching my breath, I did my best to be nonchalant about the looks being thrown my way..."
    "... by Vince, Cliff, Elliot and now Neil and Donovan!"
    "(Can\'t make out whether they think I\'m the reincarnation of Good Queen Bess or some floozy they saw on a Wanted poster!)"
    "(Time to get away from the crawling eyes!)"
    hide me
    show julius p2 at ls_mid
    "I noticed the piano player...sitting alone in a corner with a book and wandered over."
    hide julius
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(Wow is he good to look at!)"
    hide me
    show julius p2 at ls_left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    "He glanced up at me as I approached, a warm-but-wary smile breaking across his face."
    show julius p1 at ls_left
    me @ prolf smile "You play beautifully...I\'ve never heard live jazz played with such emotion...and you\'re the band leader too?"
    j "Yes, ma\'am, I am. And thank you for the kind words."
    "I introduced myself."
    j "I\'m Julius Harper, ma\'am."
    me @ prolf sideways "Please don\'t call me \'ma\'am\'. Makes me feel like Methuselah\'s sister!"
    j @ p1 smile "I\'ll try...but it\'s a habit."
    me @ prolf smile "So...whatcha readin\'? Poetry?"
    "He blinked up at me and held my eyes with his gorgeous light eyes..."
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    "(Really striking! And he looks me in the eyes more\'n most men I meet!)"
    "The way he\'s looking, it\'s like he\'s looking INTO me. A gal could get used to that kind of attention!)"
    "Then he started reading and the whole business between us cinched up a few notches."
    hide me prolf
    show julius p2 at ls_mid
    "(Reciting...in a rich, full voice as warm as his smile.)"
    "It was a poem about old, old rivers and how poets bathed in those rivers throughout all time..."
    j "...I\'ve known rivers. Ancient, dusky rivers. My soul has grown deep like the rivers."
    show julius p1 at ls_left
    if dress == "normal":
        show me prolp smile at ls_right
    else:
        show me prolf smile at ls_right
    me "Wow...that was...beautiful, Julius. Did you..."
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    j @ p1 smile"Naw. Fella name of Langston Hughes wrote it. To me, his stuff sounds like jazz."
    me "I can see that."
    j "Gotta get back to work."
    me @ prolf smile "Hey, can you play my favorite song for me?"
    show julius p1 smile at left
    if dress == "normal":
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    "I whispered in his ear. He got a broad smile. I gave him a peck on the cheek."
    hide me
    show julius p1 smile at ls_mid
    j "I do believe Cleo knows that one."
    "Julius winked and headed back to the stage."
    scene bar
    show cleo at ls_left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    "I headed back to the bar, where I found a spot next to a gal sporting a chic bob just like Colleen Moore\'s."
    hide me
    hide cleo
    show sofia at ls_mid
    "Just then, the singer from earlier came up to the bar."
    "(Donovan said her name was...Sofia...something.)"
    show sofia at ls_right
    show cleo at ls_left
    "She tapped the woman with the bob on the shoulder."
    s "Hey ya, Cleo. Julius says it\'s time to do your thing. Me, I\'m getting a drink!"
    cl "Just the one, Soph. Still a few sets to do tonight."
    hide cleo
    show sofia p1 smile at left
    if dress == "normal":
        show me prolp smile at ls_right
    else:
        show me prolf smile at ls_right
    "With that, she broke from the bar and headed casually toward the stage. Sofia turned around and seemed to see me for the first time."
    show sofia p1 smirk
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    s "Well hello, Red. Saw you on the floor earlier. Nice steppin\'. You\'re a little ray of sunshine on a dark night."
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    me "Thanks. With this hair, I could never get away with much without bein\' noticed so I just gave up tryin\'."
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    "(No reason to tell her it\'s dyed!)"
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    me "Not to get noticed that is. Let me buy that drink for you."
    show sofia p1 smile
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    s "Sure. Who\'m I thankin\'?"
    show sofia p1 surprised
    me "[fName] [lName]..."
    show sofia p1 smirk
    if dress == "normal":
        show me prolp surprised
    else:
        show me prolf surprised
    "Her eyebrow went up at the mention of my name..."
    if dress == "normal":
        show me prolp worried
    else:
        show me prolf worried
    "(My LAST name...hmmm. Another puzzle piece...but I don\'t get the picture yet.)"
    show sofia
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    me "...and you\'re Sofia...Martinez, right?"
    s @ p1 smirk "That\'s me. Martini with a 'Z'."
    show sofia p1 smile
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    me "You\'ve got a great voice for those Annette Hanshaw numbers."
    show sofia p2 smile
    s "Thanks, the light jazzy tunes are my sweet spot. You\'re about to hear a real singer, though."
    "She gestured toward the stage as the  band struck up a slow, smoky version of {i}\'Tain\'t Nobody\'s Business if I Do{/i}."
    "(That\'s the one I requested!)"
    "As Cleo belted out the first lines, I saw Sofia\'s point."
    me "Wow. There\'s some depth there."
    show sofia p2 smirk
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    s "Miss Cleo Mayfield. If she ain\'t done it, she\'s seen it...an\' she puts it all in her music."
    "(She\'s got good taste...and some musical insight.)"
    show sofia p2 smirk
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    me "So what about you?"
    show sofia p1 smile
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    s "Oh no, chica, you\'re the new hen in the house so you give first. What\'s your story?"
    show sofia
    "So I told her."
    s "Your first night out in the big city an\' you end up in the Ice Box! What\'re the odds?"
    show sofia p1 smirk
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    "I saw her glancing over my shoulder toward the fellas at the other end of the bar."
    me "Whatta you mean 'odds'? What\'ve you got...?!"
    hide me
    show sofia p1 smile at center
    s "Oh no...you\'re the one\'s got \'it\', sister."
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    show sofia p1 smirk at ls_left
    "She leaned in as she said it, her dark eyes looking right into mine."
    "Her downcast eyelashes and her slight smile were unmistakably flirtatious."
    show sofia
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    me "You\'ve got some hidden depths of your own, don\'t you?"
    show sofia p1 smirk
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    s "Well, there\'s the depths I try to share in my singin\', an\' then there\'s the other kind. The kind I\'d need a gal to help me explore."
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    "I felt myself blush."
    show sofia p2
    s "Don\'t mean to embarrass you. I jus\' thought I got a signal."
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    me "Embarrassin\' me is harder than my complexion makes it look. I was just...surprised."
    s @ p2 smile "Good surprised or bad surprised?"
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    show sofia p2 smirk
    "It was my turn to smile and bat my eyelashes."
    me "Surprised surprised. But it\'s like you said, it\'s my first night in the big city..."
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    "She touched my arm with fingers that seemed to know right where to go."
    s "Not lookin\' to dive too deep too fast?"
    "I looked around. All those fellas were trying to act casual, but I got the feeling they were watching every move we made."
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    me "I figure I\'d better stay paddlin\' on the surface \'til I get a finger on the pulse around here."
    show sofia p2 sad
    "Sofia sighed theatrically."
    show sofia p2
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    s "Sure. I getcha, sweetie. Me, I\'m gonna go back to Cleo up on the next number..."
    "She knocked the last of her drink back."
    s @ p2 smile "...thanks for the drink."
    hide sofia
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "I watched her go and it was a sight to see."
    "(And I imagine she knows it too. Whew. What a night!)"
    hide me
    show vince
    "Right then I spotted Vince watching me."
    if dress == "normal":
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show vince at ls_right
    me "Come on, you owe me a dance after that sass at the station."
    show vince p1 smile
    "He looked like he\'d been caught with his hand in the cookie jar then, shrugged."
    show vince
    vince "Sure thing, doll."
    scene dance
    show vince at ls_left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    "Turns out, Vince was a good dancer."
    if dress == "normal":
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    "When Julius swung the band into a slower number, Vince pulled me close."
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    vince "You think Uncle Charlie\'s gonna go for this?"
    show vince p1 grin
    me "A wise man once said, \'What he don\'t know can\'t hurt him.\'"
    "He just smirked at my arched eyebrow remark, but he didn\'t let me go, which suited me."
    show vince
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    "His hand on my back pushed my front against his front."
    "When the band ended their set, I didn\'t let him go too fast."
    "We both felt the sparks. His eyes were glued to mine as we stood on the floor."
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    me "Is it just me, or is it getting awful warm in here?"
    show vince p1 smile
    "He kind of shook himself, like a dog waking up from a good nap."
    show vince p1 smile at left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    vince "Uh...yeah...I should...do something about that..."
    show vince p1 grin at left_zoom
    if dress == "normal":
        show me prolp at shrink
    else:
        show me prolf at shrink
    "He peeled himself off me, but he kept looking back. And every time he did, I was still watching."
    scene bar
    show cliff p2 smile
    "Cliff was in a lull when I bellied up."
    show cliff p2 smile at left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    me "Where\'s Donovan?"
    c "Had to go to work. Say, how\'d you learn all those dances out there in Zilchville?"
    me "From the movies. Then we\'d practice to records on the Victrola with my girlfriends. We got pretty good."
    show cliff p2 grin
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    c "I\'ll say. Ready for another drink?"
    show cliff p2 smile
    "Cliff went light on this one."
    show cliff p3 smile
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    "(He\'s looking out for me. How sweet.)"
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    me "You ever get out from behind the bar to shake a leg?"
    show cliff p3 grin
    c "I stay here. The girls come to me."
    show cliff p2 smile
    if dress == "normal":
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    "I reached over and grabbed a hunk of bicep just as Vince walked up."
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    "(Solid as a rock...soft skin, too.)"
    me "What do you do for exercise, Mr. Conway?"
    hide me
    show vince p2 smile at ls_left # Missing toothy
    show cliff p2 smile at ls_right
    "Cliff raised an eyebrow and Vince guffawed."
    vince "She meant the weights, you mug. Not the other thing."
    hide vince
    show cliff p2 smile at left
    if dress == "normal":
        show me prolp sideways at ls_right
    else:
        show me prolf sideways at ls_right
    "Realizing what he must\'ve thought what I meant, it was my turn to blush."
    c "Sorry. Shouldn\'t have taken you like that."
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    "(This one\'s a real gentleman. Wouldn\'t want him thinking I\'m too much of a lady, though.)"
    show cliff p2 smirk
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    me "Cliff, nobody takes me any way I don\'t want to be taken."
    hide me
    show vince at left # Missing toothy smile
    show cliff p2 smile at right
    "Vince chuckled. Cliff turned away to help a customer, but not before I caught sight of his blush."
    hide vince
    hide cliff
    show neil fs2 at ls_mid
    "Neil was still holding up the other side of the bar, so I wandered over to try my luck."
    show neil fs2 at ls_right
    if dress == "normal":
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    me "You don\'t dance...don\'t even bounce your foot to the music. You hold that glass any tighter, it\'s gonna break."
    n "You saying something?"
    me @ prolf sideways "Why\'re you even here?"
    show neil fs2 sideways
    n "Fending off the advances of mildly inebriated tomatoes like yourself has its rewards."
    me "Everybody\'s gotta have a hobby...but I don\'t think that\'s yours."
    me "You could pickle your liver at some quiet joint..."
    "Maybe the booze was making me smarter or just more willing to say whatever came into my head."
    show neil fs2
    me "Maybe you got scars from the war...even a bum leg, like Donovan said,"
    me "but the real wound you brought back ain\'t on the outside."
    show neil fs2 angry
    "Neil made those ice blue eyes wide, like headlights on a new Caddy."
    $ renpy.music.play('suspense.mp3', channel=u'music', loop=True, fadein=True)
    n "You\'re punching above your weight, kid. Get lost."
    hide neil
    if dress == "normal":
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    "He seemed to mean it, so I got lost...but I left knowing I\'d been right."
    $ renpy.music.play('main_theme.mp3', channel=u'music', loop=True, fadein=True)
    if dress == "normal":
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show elliot p1 smile at ls_right
    "I grabbed Elliot and dove back onto the dance floor as the band moved into another upbeat number."
    "After a couple of dances, the floor was getting crowded. Elliot lead me to a table in the back where a group of men were playing poker."
    hide elliot
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(That\'s a decent stack of cash in the pot!)"
    show gerald_prologue at character_zoom
    "We watched them finish a hand. A lean, pale red-haired fellow raked in the pot and turned a raking smile toward me and Elliot."
    q "Now it\'s a fine thing you introduced me to this crowd of deep pockets tonight, Graham. Should fund a winter week in Florida..."
    q "And it\'s clear your generosity knows no bounds as here you are, about to introduce me to the beauty I\'ll take with me!"
    "(Wow. The men move faster than the cars in this burg!)"
    hide gerald_prologue
    hide me
    show elliot p1 smile at ls_right
    show gerald p1 smile at left
    e "I\'d like you to meet a new acquaintance of mine..."
    hide elliot
    show gerald p1
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    "I stuck my hand out. Elliot\'s friend took it and, instead of shaking, kissed the back of it as he stood."
    hide me
    show elliot p1 grin at ls_right
    e "...this is Miss [me] [lName]. [fName], I\'d like you to meet Mr. Gerald O\'Fallon."
    hide elliot
    if dress == "normal":
        show me prolp surprised at ls_right
    else:
        show me prolf surprised at ls_right
    g "Miss [fName]...related to Charlie [lName] of Charlie\'s Appliances?"
    me "Um...yeah."
    hide gerald
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(Geez! How well known IS Charlie in this town?)"
    hide me
    show gerald p1 wink at left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    g "The ravishing sight of you makes the pleasure of your acquaintance all mine."
    hide gerald
    hide me
    show elliot p1 grin at ls_mid
    e "Gerald is one of the city\'s leading entrepreneurs, supplying Chicago\'s denizens with libations..."
    e "...from the confines of his competing establishment not far from here."
    hide elliot
    show gerald p1 at ls_left
    if dress == "normal":
        show me prolp smile at ls_right
    else:
        show me prolf smile at ls_right
    me "Not a native Chicagoan, I\'m guessing?"
    show gerald p1 smile
    g "I came by way of New York...and in all my travels, I\'ve yet to meet a vision as fetching as stands before me now."
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    me "Do I look like a piece of soda bread to you?"
    show gerald p1 surprised
    show elliot p2 sideways
    "He and Elliot both gave me a look."
    hide elliot
    if dress == "normal":
        show me prolp sideways at ls_right
    else:
        show me prolf sideways at ls_right
    me "I\'m only askin\' cause you\'re slatherin\' on the blarney like it was butter."
    hide me
    show gerald p1
    show elliot p2 smile at ls_right
    e "Oh-ho! I believe that point goes to [fName]."
    hide gerald
    if dress == "normal":
        show me prolp smile at ls_left
    else:
        show me prolf smile at ls_left
    me "We\'re not keepin\' score, Elliot. At least, Mr. O\'Fallon better hope we\'re not. We\'ve barely met an\' he\'s already down a few runs."
    hide elliot
    show gerald p2 at ls_left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    g "Baseball\'s not really my game. Cards, now..."
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    me "A gambler who runs a speakeasy an\' flirts like there\'s no tomorrow. Be still my flutterin\' heart."
    hide me
    show gerald p2 smile
    show elliot p1 smile at ls_right
    g "I do like her, Elliot. She has wit."
    hide elliot
    if dress == "normal":
        show me prolp sideways at ls_right
    else:
        show me prolf sideways at ls_right
    me "She also has a Momma who likes chasin\' boys off her porch with a broom."
    show gerald p2 smile at ls_mid
    hide me
    g "I think you underestimate my capacity to charm mothers of all shapes, sizes, and persuasions."
    $ renpy.music.play('suspense.mp3', channel=u'music', loop=True, fadein=True)
    hide gerald
    if dress == "normal":
        show me prolp worried at ls_left
    else:
        show me prolf worried at ls_left
    show vince p2 stern at ls_right
    "Gerald stiffened slightly as he looked over my shoulder."
    hide me
    show vince p2 angry at ls_mid
    vince "You bring one\'a your Ma\'s extra brooms, [fName]?"
    hide vince
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(Vince! Holy gee, you couldn\'t cut the air between him and Gerald with a sharp axe!)"
    hide me
    show vince p2 angry at ls_left
    show gerald p1 angry at ls_right
    vince "Cause I\'ll use it to sweep this hustler right out the door and down the alley. Come to think, I\'ll do it without the broom."
    hide gerald
    hide vince
    show elliot p2 glance at ls_mid
    e "Now, now, Vince! No need for..."
    hide elliot
    show vince p1 stern at ls_left
    show gerald p1 at ls_right
    g "It\'s all right, Elliot. Moretti and I have an understanding when we run into each other..."
    show vince p2 angry
    show gerald p1 pout
    g "He says something uncivil, I do him the courtesy of laughing it off instead of paying him out for the insult..."
    show vince p1 stern
    show gerald p1 angry
    g "It\'s saved his friends the cost of a funeral on several occasions."
    hide vince
    hide gerald
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(He means it! And the way Vince is looking at him, the feelin\'s mutual!)"
    hide me
    show gerald p1 smile at ls_mid
    "Gerald gathered the rest of his cash from the table, and tossed me what I had to guess was his most charming smile."
    hide gerald
    if dress == "normal":
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    "(It works, that\'s for sure!)"
    hide me
    if dress == "normal":
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show gerald p1 smile at ls_right
    g "I hope to have the joy of further acquaintance, Miss [fName]."
    hide gerald
    if dress == "normal":
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    "With that, he was gone."
    scene dance_empty
    with fade
    pause
    $ renpy.music.play('main_theme.mp3', channel=u'music', loop=True, fadein=True)
    if dress == "normal":
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    "The rest of the night passed in a blur of dance steps, hot licks, and gin fumes."
    "I watched as the patrons left one by one and the band started packing up."
    hide me
    show vince at ls_mid
    "From the corner of my eye, I noticed Vince walking towards me."
    #Missing toothy smile
    "His dashing smile hasn\'t waned a bit since I saw him for the first time earlier today."
    show vince at ls_left
    if dress == "normal":
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    vince "Your chariot awaits, doll."
    vince "Now, I ain\'t responsible for how you get in without gettin\' collared,"
    show vince p1 smirk
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    vince "though seems like you got a lot of experience with that."
    vince "You can\'t tell Charlie where you been, or all our asses\'ll be in a sling!"
    "I was about to grill him again about who really ran this place when the phone behind the bar rang."
    scene bar
    show cliff p3 at ls_mid
    $ renpy.music.play('suspense.mp3', channel=u'music', loop=True, fadein=True)
    "Cliff answered then, motioned Vince over. I trailed along, curious."
    show cliff p3 at ls_left
    show vince p1 stern at ls_right
    "I couldn\'t tell what was up from Cliff\'s expression, but Vince looked pretty grim."
    show vince p2 stern
    vince "Spill it, Cliff. What\'s going on."
    hide vince
    show cliff p3 angry at ls_mid
    c "It\'s Charlie. He\'s been shot."
    scene car_street_night
    show vince p1 stern at ls_left
    if dress == "normal":
        show me prolp worried at ls_right
    else:
        show me prolf worried at ls_right
    "Vince drove. Fast. I had a million questions, But I clammed up and thought my thoughts."
    if dress == "normal":
        show me prolp irritated
    else:
        show me prolf irritated
    "(Whoever called knew they\'d reach someone who knew Uncle Charlie...)"
    "(so Charlie must know about the speakeasy...which means...?)"
    if dress == "normal":
        show me prolp worried
    else:
        show me prolf worried
    "(Gosh, I hope the old boot is all right!)"
    scene hospital_hallway
    with fade
    pause
    show elliot p2 sad at ls_left
    show julius p2 card sad teeth at ls_right
    $ renpy.music.play('sad.mp3', channel=u'music', loop=True, fadein=True)
    "I was surprised to see Elliot in the hospital lobby with Julius and Sofia."
    hide elliot
    hide julius
    show sofia p2 casual at ls_left
    show donovan uniform at ls_right
    "They were talking to a uniform cop who turned around just as we came in..."
    hide sofia
    show donovan uniform at ls_mid
    "Donovan! He\'s a COP?)"
    hide donovan
    show neil fs1 at ls_mid
    "My jaw was still on the floor when Neil came down the hall."
    n @ fs1 smirk "Just got through talking with his doctor. Barring infection, he\'s going to be all right."
    hide neil
    "Everyone cheered their relief."
    if dress == "normal":
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    "(It\'s nice to see everybody wishing him well.)"
    if dress == "normal":
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show neil fs1 smirk at ls_right
    "Finally, the doctor said a few of us could go in."
    hide me
    hide neil
    "We whittled it down to me, Vince, Cliff, Neil, and Donovan."
    scene hospital_night
    pause
    window hide
    show charlie sick smile at ls_mid
    "Uncle Charlie did not look good, but he was sitting up. He pulled on a smile when he saw me."
    ch "[fName], I\'m sorry you had to be here for this."
    show charlie sick smile at ls_right
    show vince p2 angry at ls_left
    vince "Don\'t you worry, Charlie! We\'ll get the bastards who did this!"
    "Charlie laughed nervously."
    ch "Calm down, Vince. It\'s just a case of mistaken identity..."
    hide vince
    if dress == "normal":
        show me prolp  worried at ls_left
    else:
        show me prolf worried at ls_left
    me "How\'re you feeling?"
    ch "I\'ll be alright, dear. Can you wait outside? I need to talk to my associates..."
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    show charlie sick frown
    me "Is this about the speakeasy underneath the shop?"
    "He went from pale to paler."
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    me "It\'s the bee\'s knees! You\'ve got a little inventory problem, but..."
    hide me
    show charlie sick at ls_mid
    ch "Who the hell...pardon my French, [fName]...let her into the speak?!"
    show charlie sick at ls_right
    show vince p1 stern at ls_left
    "He suddenly turned his glare at Vince."
    ch "Was it you, Vince?"
    hide vince
    hide charlie
    menu speak_entry:
        "Don\'t pick B or C for now - texts works but no sprites."
        "A: Take full responsibility":
            if dress == "normal":
                show me prolp worried at ls_mid
            else:
                show me prolf worried at ls_mid
            me "Don\'t be mad at them, Uncle Charlie. I found my way there on my own...mostly..."
            if dress == "normal":
                show me prolp sideways at ls_left
            else:
                show me prolf sideways at ls_left
            show charlie sick frown at ls_right
            ch "How\'d THAT work?"
            me "I went to the movies..."
            show charlie sick
            ch "You left the house after I was gone?!"
            hide me
            hide charlie
            show neil fs2 sideways at ls_mid
            n "Charlie, can you please keep in mind you were just shot?"
            n "[fName], you might want to avoid raising his blood pressure."
            hide neil
            if dress == "normal":
                show me prolp sideways at ls_left
            else:
                show me prolf sideways at ls_left
            show charlie sick at ls_right
            me "I was bored. I went to the movies and ran into Elliot..."
            me "...and he gave me on of those Icebox cards...so...I went..."
            if dress == "normal":
                show me prolp
            else:
                show me prolf
            ch "Fine. I get it. You slipped the leash and the dominos started falling."
            if dress == "normal":
                show me prolp sideways
            else:
                show me prolf sideways
            "(Kind of a mixed metaphor...but probably not the best time to bring that up.)"
            hide me
            hide charlie
        "B: Blame him for leaving you alone.":
            me "It\'s not his fault, Uncle Charlie. Or mine! You left me alone in your big old boring house..."
            ch "Then you unpack. Read a book! Make some damn dinner!"
            me "I have one suitcase, so unpacking took five minutes...your books are all about dead people..."
            me "...and you wouldn\'t want to eat anything I\'d cook, believe you me."
            ch "All right. What\'s done is done. You went out and just happened into the Icebox by chance?"
            me "No, I went to the movies and met Elliot..."
            ch "You know Elliot?"
            me "I do now."
            me "Elliot gave me one of the little Icebox cards so...I went. Then Vince walked in and everybody was talking about you..."
            "Uncle Charlie sighed, his head falling back on the pillow."
            ch "All right, all right. It ain\'t exactly no harm, no foul...but it\'s nobody\'s fault. I guess."
        "C: Make it sound like a coincidence.":
            me "Um, well. It\'s a funny story. Kind of a series of accidents, really."
            ch "If it ain\'t starring Chaplin, Keaton and both Laurel AND Hardy, I\'m not going to be laughing, I promise."
            me "It does have a movie star in it..."
            ch "Let me guess, Elliot turned on the million watt smile, and invited you to the \'box."
            me "It\'s not his fault he\'s air tight! Being handsome is practically part of job description."
            "Vince gave me a wink."
            vince "Yeah, you should be proud she\'s no bug-eyed Betty, neither. I\'m not a fan of Mr. Charm there, but even I can see what he saw in her..."
            "(That\'s sweet.)"
            ch "Shaddup, you. You\'re not helping her case...or yours."
            me "Anyway, next thing I know, I\'m out in front of the appliance store..."
            ch "You just happened by, did you? Dressed like that?"
            "(Oops.)"
            me "Well...I went back to your house after the picture, but you were still gone and Mrs. Fitzhugh had come and gone...so..."
    if dress == "normal":
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show charlie sick at ls_right
    ch "I get it. And once you got to the \'box, there was no way you wouldn\'t figure it out, smart gal that you are."
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    "(Time to change the subject.)"
    if dress == "normal":
        show me prolp irritated
    else:
        show me prolf irritated
    me "So...now what? Neil says you\'re going to be out of commission for a few weeks..."
    hide charlie
    show neil fs2 at ls_right
    n "Months."
    if dress == "normal":
        show me prolp sideways
    else:
        show me prolf sideways
    "(Not a man to sugarcoat anything.)"
    hide me
    hide neil
    show vince p2 at ls_mid
    vince "I can take it over. I bring the booze in anyway, might as well retail it..."
    "(So Vince is a bootlegger?!)"
    hide vince
    show charlie sick smile at ls_mid
    ch "No. Sorry, Vince. You\'re too much of a loose cannon."
    ch "Even Donovan can\'t cover for your temper every time..."
    show charlie sick
    ch "Maybe we just shut down \'til I\'m back on my feet..."
    show cliff p4 at ls_left
    show charlie sick smile at ls_right
    c "Due respect, boss, we\'ll lose our customers. Julius and the band...the whole staff..."
    show charlie sick
    ch "All right. You don\'t have to paint me a picture."
    "Out of the clear blue, an idea popped into my head and came right out of my mouth."
    hide charlie
    hide cliff
    $ renpy.music.play('funaction.mp3', channel=u'music', loop=True, fadein=True)
    if dress == "normal":
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    me "Me. It should be me. I should run the Ice Box."
    hide me
    show cliff p4 smirk at ls_left
    show vince p1 smile at ls_right
    "Every guy in the room looked like I\'d just told \'em clowns on pink elephants were coming for Christmas."
    hide cliff
    hide vince
    if dress == "normal":
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    "Before they could say why not, I started telling \'em why."
    if dress == "normal":
        show me prolp surprised
    else:
        show me prolf surprised###
    show me prolf irritated
    me "I graduated from Mrs. Bradburn\'s Secretarial and Business College, worked in Pop\'s office at the factory..."
    me "I\'m good with numbers, plus I\'m more sociable than all these guys put together, except maybe Elliot..."
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    me "And face it Uncle Charlie, I\'m FAMILY..."
    "(Uncle Charlie\'s got that shrewd look in his eye, like Pops when he\'s sizing up a deal.)"
    me "...you got to trust family first, am I right? Oh, and one more thing..."
    me "I got away with more stuff back home than Momma and Pops ever knew. So, looks like I got your devious streak."
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    me "I think that makes me a sure fire success in the speakeasy racket!"
    hide me
    show charlie sick at ls_mid
    "He sat in silence for a minute, rolling it over in his mind."
    "The guys all looked at me like I\'d just done a magic trick to even him to think about it."
    "Uncle Charlie\'s eyes flicked from one of us to the next. He took a deep breath."
    show charlie sick smile
    ch "All right, [fName], you\'re the new official proprietor of Charlie\'s Appliances and..."
    ch "...everything below street level..."
    if dress == "normal":
        show me prolp smile at ls_left
    else:
        show me prolf smile at ls_left
    show charlie sick smile at ls_right
    "I gave a little squeak and clapped my hands."
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    ch "Vince and Cliff\'ll show you the ropes..."
    ch "But you got to do one thing, besides coming to visit me, that is..."
    if dress == "normal":
        show me prolp smile
    else:
        show me prolf smile
    me "You name it!"
    if dress == "normal":
        show me prolp irritated
    else:
        show me prolf irritated
    ch "You\'re getting into a dangerous business. Maybe you\'re smart, even tough for a girl..."
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    ch "...but you ain\'t the kind of tough you sometimes gotta be for the Chicago booze trade..."
    ch "So, you pick one of these fellas to back you up. Deal?"
    hide charlie
    if dress == "normal":
        show me prolp smile at mid_zoom_small
    else:
        show me prolf smile at mid_zoom_small
    "(I\'d promise him the moon with a blue bow on it right now I\'m so excited!)"
    hide me
    if dress == "normal":
        show me prolp smile at ls_left
    else:
        show me prolf smile at ls_left
    show charlie sick smile at ls_right
    me "It\'s a deal, Uncle Charlie!"
    if dress == "normal":
        show me prolp
    else:
        show me prolf
    ch "All right then...I want you to think about this and I\'m gonna provide you with my expert advice."
    ch "These\'re all solid folks, but each one of \'em has his peccadillos, you might say..."
    hide me
    show charlie sick smile at ls_mid
    ch "So...who\'s it going to be to help you run the speakeasy?"
    scene tbc
    with fade
    pause
            #### PROLOGUE END
#    $ next_chapter = next_chapter + 1
#    jump next_chapter_menu
