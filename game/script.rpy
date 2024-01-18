define next_chapter = 0

label start:
    $ renpy.music.play('main_theme.mp3', channel=u'music', loop=True, fadein=True)
    python:
        fName = renpy.input()
        lName = renpy.input()
    scene station
    show screen button_overlay
    show me prol at mid_zoom
    show me prol worried at mid_zoom
    show me prol sideways at mid_zoom
    show me prol worried at mid_zoom
    show me prol at mid_zoom
    show me prol sideways at mid_zoom
    show me prol at mid_zoom
    show me prol worried at mid_zoom
    scene station_street
    with fade
    pause
    show me prol surprised at mid_zoom
    hide me
    show me prol worried at mid_zoom
    show me prol irritated at mid_zoom
    show me prol worried at mid_zoom
    window hide
    show vince_prologue at character_zoom
    $ renpy.pause(3, hard=True)
    window show
    hide vince_prologue
    hide me
    show me prol at ls_mid
    hide me
    show vince p1 grin at ls_mid
    hide me
    hide vince
    menu listen_pa:
            show me prol at ls_left
            show vince p1 grin at ls_right
            show me prol sideways
            show vince
            me @ prol sideways
            show me prol irritated
            show me prol
            vince @ p1 smirk
            hide me
            show vince p1 grin at ls_mid
    show vince p1 grin at ls_right
    show me prol smile at ls_left
    hide vince
    show me nhprol at mid_zoom_small
    hide me
    show vince at ls_right
    show me nhprol sideways at ls_left
    show me nhprol
    me nhprol @ sideways
    hide me
    show vince at ls_mid
    hide vince
    show me nhprol at ls_mid
    show vince p1 grin at ls_right
    show me nhprol smile at ls_left
    show vince at ls_mid
    hide me
    vince @ p1 grin
    scene car_street
    with fade
    pause
    show me nhprol surprised at ls_right
    show vince p1 grin at ls_left
    show me nhprol
    show vince
    show me nhprol surprised
    show me nhprol
    vince @ p1 grin
    me @ nhprol worried
    vince @ p1 smile
    show me sideways
    vince @ p1 grin
    vince @ p1 grin
    me @ nhprol
    vince @ p1 smirk
    show me nhprol
    show vince p1 grin
    show vince
    show me nhprol worried
    vince @ p1 grin
    show me nhprol sideways
    vince @ p1 grinme @ nhprol
    me 
    me @ nhprol 
    # Missing Vince toothy smile
    show me nhprol smileme @ nhprol sideways 
    show me nhprol
    vince 
    me @ nhprol smile 
    me @ nhprol sideways 
    vince @ p1 smirk 
    # Missing Vince toothy smile
    me nhprol sideways 
    vince 
    me @ nhprol worried 
    show vince p1 grin
    show me nhprolvince 
    scene house_day
    with fade
    pauseshow charlie smilech 
    show charlie smile at ls_left
    show me prol at ls_rightch 
    show charlie
    me @ prol smile 
    show me sidewaysch 
    show charlie smile at three_left
    show me prol worried at ls_mid
    show vince at three_right
    vince 
    hide charlie
    show me prol irritated at ls_left
    show vince p2 at ls_rightshow vince p1 smirkhide me
    hide vince
    show charlie at ls_mid
    ch 
    show me prol worried at ls_right
    show charlie smile at ls_left
    ch 
    hide charlie
    show me prol worried at mid_zoomhide me
    show charlie at ls_left
    show me prol worried at ls_righthide charlie
    hide me
    show vince at ls_midscene living_day
    $ renpy.music.play('sad.mp3', channel=u'music', loop=True, fadein=True)
    with fade
    pause
    show me nhprol worried at ls_left
    show charlie at ls_righthide me
    show charlie at ls_midhide charlie
    show me nhprol worried at mid_zoomscene room_day
    with fade
    pauseshow me nhprol worried at mid_zoomshow me nhprol sidewaysshow me nhprol2
    $ renpy.music.play('funaction.mp3', channel=u'music', loop=True, fadein=True)show me prol2show me prol2 smilescene gladius_day
    with fade
    pause
    show me prol2 smile at ls_mid
    Girl Trouble\show me prol2 surprisedhide me
    q 
    show me prol2 sideways at ls_mid
    me 
    hide me
    window hide
    show elliot_prologue at character_zoom
    $ renpy.pause(3, hard=True)
    window show
    q 
    me q 
    q 
    q 
    hide elliot_prologue
    q 
    show me prol2 sideways at mid_zoomscene house_night
    with fade
    pause
    $ renpy.music.play('main_theme.mp3', channel=u'music', loop=True, fadein=True)#### CHOOSE YOUR LOOK ####
    window hide
    call screen ls_cards
    label dress_choice:
        if dress == :
            
        else:
            window hide
            show dress_15 at outfit_zoom
            pause
            hide dress_15
            window show
            show me prolf at ls_mid
            
    scene store_night
    with fade
    pause
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallhide me
    if dress == :
        show me prolp worried at ls_mid
    else:
        show me prolf surprised at ls_mid
    me 
    cab 
    if dress == :
        show me prolp worried at ls_mid
    else:
        show me prolf worried
    if dress == :
        show me prolp worried at ls_mid
    else:
        show me prolf surprisedscene icebox_entrance
    with fade
    pauseif dress == :
        show me prolp worried at ls_mid
    else:
        show me prolf at ls_midscene icebox_entrance_peepif dress == :
        show me prolp worried at ls_mid
    else:
        show me prolf surprised at ls_mid
    me 
    if dress == :
        show me prolp sideways
    else:
        show me prolf sideways
    me 
    if dress == :
        show me prolp worried
    else:
        show me prolf worriedscene dance
    with fade
    pause
    $ renpy.music.play('funaction.mp3', channel=u'music', loop=True, fadein=True)
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallhide me
    scene bar
    show doneil_prologue at character_zoom
    $ renpy.pause(3, hard=True)
    window show
    q 
    hide doneil_prologue
    if dress == :
        show me prolp surprised
    else:
        show me prolf surprised
    me 
    hide me
    show donovan p1 pursesmirk at ls_left
    show neil fs2 at ls_rightq 
    hide donovan
    hide neil
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallhide me
    if dress == :
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    me 
    if dress == :
        show me prolp smile at ls_left
    else:
        show me prolf smile at ls_left
    show donovan p2 pursesmirk at ls_right
    q 
    if dress == :
        show me prolp
    else:
        show me prolf
    d 
    me 
    if dress == :
        show me prolp surprised
    else:
        show me prolf surprised
    show donovan p2 serioushide me
    hide donovan
    show neil fs2 smirk
    n 
    show neil fs2 smirk at ls_right
    show donovan p2 angry at ls_leftd 
    hide neil
    show donovan p2 pursesmirk at ls_right
    if dress == :
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    d 
    me 
    d 
    if dress == :
        show me prolp smile
    else:
        show me prolf smiled 
    show cliff_prologue at character_zoom
    c 
    hide cliff_prologue
    hide donovan
    show cliff p2 smile at left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    me 
    c 
    show cliff p2 grin
    c @ p2 grin 
    show cliff p2
    hide me
    show donovan p2 pursesmirk at ls_right
    d 
    show donovan p2 blush
    d 
    show cliff p2 smile
    show donovan p2 blush at ls_midhide donovan
    show cliff p2 smile at centershow cliff p3 smile at left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_rightshow cliff p3 smirk
    if dress == :
        show me prolp surprised
    else:
        show me prolf surprised
    me 
    if dress == :
        show me prolp
    else:
        show me prolfme 
    show cliff p3hide me
    show cliff p3 smirk at left
    show donovan p2 surprise
    show neil fs1 smile at ls_righthide cliff
    hide donovan
    hide neil
    if dress == :
        show me prolp sideways at ls_mid
    else:
        show me prolf sideways at ls_mid
    me 
    if dress == :
        show me prolp irritated
    else:
        show me prolf irritated
    me 
    show cliff p3 smirk at left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    c 
    me 
    show cliff p3 smile
    if dress == :
        show me prolp smile
    else:
        show me prolf smile
    me 
    hide cliff
    hide me
    show donovan p2 pursesmirk at ls_left
    show neil fs2 sideways at ls_righthide donovan
    hide neil
    show cliff p3 smirk at ls_mid
    c 
    hide cliff
    if dress == :
        show me prolp surprised at ls_mid
    else:
        show me prolf surprised at ls_mid
    me 
    hide me
    show donovan p2 pursesmirk
    d 
    show donovan p2 pursesmirk at ls_left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    d 
    if dress == :
        show me prolp smile
    else:
        show me prolf smile
    me 
    hide donovan
    hide me
    show cliff p2 smile
    hide cliff
    show donovan p2 at ls_mid
    d 
    hide donovan
    show cliff p2 smile at left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    c 
    hide cliff
    hide me
    show donovan p2 pursesmirk
    d 
    hide donovan
    show cliff p3 at left
    if dress == :
        show me prolp smile at ls_right
    else:
        show me prolf smile at ls_right
    me 
    hide cliff
    show donovan p2 pursesmirk at ls_leftshow donovan p2 pursesmirk at ls_mid
    hide mescene dance
    show julfia_prologue at character_zoomhide julfia_prologue
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallscene bar
    show donovan p2 pursesmirk at ls_left
    if dress == :
        show me prolp smile at ls_right
    else:
        show me prolf smile at ls_right
    me 
    if dress == :
        show me prolp
    else:
        show me prolf
    d show donovan p2 surprise
    me 
    hide me
    show neil fs2 grin at ls_right
    n 
    show donovan p2
    d 
    show neil fs1 sideways
    n 
    show donovan p2 pursesmirk
    show neil fs1
    d 
    hide donovan
    hide neil
    show elliot p1 hat grinhide elliot
    show donovan p2 pursesmirk at ls_left
    if dress == :
        show me prolp surprised at ls_right
    else:
        show me prolf surprised at ls_right
    d 
    hide donovan
    hide me
    show elliot p1 grinhide elliot
    show vincehide vince
    if dress == :
        show me prolp surprised at ls_mid
    else:
        show me prolf surprised at ls_mid
    me 
    hide me
    show donovan p1 surprise
    d 
    hide donovan
    if dress == :
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show elliot p1 beam at ls_righte 
    e 
    if dress == :
        show me prolp sideways
    else:
        show me prolf sidewaysif dress == :
        show me prolp smile
    else:
        show me prolf smile
    show elliot p1 grinscene dance
    show juliushide julius
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    show elliot p1 grin at ls_leftif dress == :
        show me prolp smile
    else:
        show me prolf smileif dress == :
        show me prolp
    else:
        show me prolfif dress == :
        show me prolp sideways
    else:
        show me prolf sidewayshide me
    hide elliot
    show vince p2$ renpy.music.play('suspense.mp3', channel=u'music', loop=True, fadein=True)
    hide vince
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallhide me
    scene bar
    show vince p1 stern at ls_left
    show cliff p3 at ls_rightshow cliff p3 angryhide cliff
    show vince p1 stern at ls_midshow vince p1 stern at ls_left
    show elliot p1 smile at ls_rightvince 
    e @ p1 grin 
    show elliot p1 sideways
    vince @ p2 
    hide elliot
    hide vince
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallhide me
    show vince p2 at ls_left
    show elliot p1 glance at ls_right
    e 
    show vince p2 stern
    show elliot p2 surprised
    c 
    hide vince
    show cliff p3 angry at ls_left
    show elliot p1 glance
    c 
    hide elliot
    hide cliff
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallhide me
    show elliot p2 surprised at ls_midshow elliot p1 grinhide elliot
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    $ renpy.music.play('main_theme.mp3', channel=u'music', loop=True, fadein=True)scene dance
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    hide me
    show julius p2 at ls_midhide julius
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallhide me
    show julius p2 at ls_left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_rightshow julius p1 at ls_left
    me @ prolf smile 
    j j 
    me @ prolf sideways 
    j @ p1 smile 
    me @ prolf smile if dress == :
        show me prolp sideways
    else:
        show me prolf sidewayshide me prolf
    show julius p2 at ls_mid
    j 
    show julius p1 at ls_left
    if dress == :
        show me prolp smile at ls_right
    else:
        show me prolf smile at ls_right
    me 
    if dress == :
        show me prolp
    else:
        show me prolf
    j @ p1 smile
    me 
    j 
    me @ prolf smile 
    show julius p1 smile at left
    if dress == :
        show me prolp at ls_mid
    else:
        show me prolf at ls_midhide me
    show julius p1 smile at ls_mid
    j scene bar
    show cleo at ls_left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_righthide me
    hide cleo
    show sofia at ls_mid
    show sofia at ls_right
    show cleo at ls_lefts 
    cl 
    hide cleo
    show sofia p1 smile at left
    if dress == :
        show me prolp smile at ls_right
    else:
        show me prolf smile at ls_rightshow sofia p1 smirk
    if dress == :
        show me prolp
    else:
        show me prolf
    s 
    if dress == :
        show me prolp smile
    else:
        show me prolf smile
    me 
    if dress == :
        show me prolp sideways
    else:
        show me prolf sidewaysif dress == :
        show me prolp smile
    else:
        show me prolf smile
    me 
    show sofia p1 smile
    if dress == :
        show me prolp
    else:
        show me prolf
    s 
    show sofia p1 surprised
    me 
    show sofia p1 smirk
    if dress == :
        show me prolp surprised
    else:
        show me prolf surprisedif dress == :
        show me prolp worried
    else:
        show me prolf worriedshow sofia
    if dress == :
        show me prolp
    else:
        show me prolf
    me 
    s @ p1 smirk 
    show sofia p1 smile
    if dress == :
        show me prolp smile
    else:
        show me prolf smile
    me 
    show sofia p2 smile
    s me 
    show sofia p2 smirk
    if dress == :
        show me prolp
    else:
        show me prolf
    s show sofia p2 smirk
    if dress == :
        show me prolp sideways
    else:
        show me prolf sideways
    me 
    show sofia p1 smile
    if dress == :
        show me prolp
    else:
        show me prolf
    s 
    show sofias 
    show sofia p1 smirk
    if dress == :
        show me prolp sideways
    else:
        show me prolf sidewaysme 
    hide me
    show sofia p1 smile at center
    s 
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    show sofia p1 smirk at ls_left
    show sofia
    if dress == :
        show me prolp sideways
    else:
        show me prolf sideways
    me 
    show sofia p1 smirk
    if dress == :
        show me prolp
    else:
        show me prolf
    s 
    if dress == :
        show me prolp sideways
    else:
        show me prolf sidewaysshow sofia p2
    s 
    if dress == :
        show me prolp
    else:
        show me prolf
    me 
    s @ p2 smile 
    if dress == :
        show me prolp smile
    else:
        show me prolf smile
    show sofia p2 smirkme 
    if dress == :
        show me prolp
    else:
        show me prolfs if dress == :
        show me prolp smile
    else:
        show me prolf smile
    me 
    show sofia p2 sadshow sofia p2
    if dress == :
        show me prolp
    else:
        show me prolf
    s s @ p2 smile 
    hide sofia
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_small
    hide me
    show vinceif dress == :
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show vince at ls_right
    me 
    show vince p1 smileshow vince
    vince 
    scene dance
    show vince at ls_left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_rightif dress == :
        show me prolp at ls_mid
    else:
        show me prolf at ls_midif dress == :
        show me prolp sideways
    else:
        show me prolf sideways
    vince 
    show vince p1 grin
    me show vince
    if dress == :
        show me prolp
    else:
        show me prolfif dress == :
        show me prolp sideways
    else:
        show me prolf sideways
    me 
    show vince p1 smileshow vince p1 smile at left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    vince 
    show vince p1 grin at left_zoom
    if dress == :
        show me prolp at shrink
    else:
        show me prolf at shrinkscene bar
    show cliff p2 smileshow cliff p2 smile at left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    me 
    c 
    me 
    show cliff p2 grin
    if dress == :
        show me prolp smile
    else:
        show me prolf smile
    c 
    show cliff p2 smileshow cliff p3 smile
    if dress == :
        show me prolp sideways
    else:
        show me prolf sidewaysif dress == :
        show me prolp smile
    else:
        show me prolf smile
    me 
    show cliff p3 grin
    c 
    show cliff p2 smile
    if dress == :
        show me prolp at ls_mid
    else:
        show me prolf at ls_midif dress == :
        show me prolp sideways
    else:
        show me prolf sidewaysme 
    hide me
    show vince p2 smile at ls_left # Missing toothy
    show cliff p2 smile at ls_rightvince 
    hide vince
    show cliff p2 smile at left
    if dress == :
        show me prolp sideways at ls_right
    else:
        show me prolf sideways at ls_rightc 
    if dress == :
        show me prolp
    else:
        show me prolfshow cliff p2 smirk
    if dress == :
        show me prolp sideways
    else:
        show me prolf sideways
    me 
    hide me
    show vince at left # Missing toothy smile
    show cliff p2 smile at righthide vince
    hide cliff
    show neil fs2 at ls_midshow neil fs2 at ls_right
    if dress == :
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    me 
    n 
    me @ prolf sideways 
    show neil fs2 sideways
    n 
    me 
    me show neil fs2
    me 
    me 
    show neil fs2 angry$ renpy.music.play('suspense.mp3', channel=u'music', loop=True, fadein=True)
    n 
    hide neil
    if dress == :
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid$ renpy.music.play('main_theme.mp3', channel=u'music', loop=True, fadein=True)
    if dress == :
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show elliot p1 smile at ls_right
    hide elliot
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallshow gerald_prologue at character_zoomq 
    q hide gerald_prologue
    hide me
    show elliot p1 smile at ls_right
    show gerald p1 smile at left
    e 
    hide elliot
    show gerald p1
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_righthide me
    show elliot p1 grin at ls_right
    e 
    hide elliot
    if dress == :
        show me prolp surprised at ls_right
    else:
        show me prolf surprised at ls_right
    g 
    me 
    hide gerald
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallhide me
    show gerald p1 wink at left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    g 
    hide gerald
    hide me
    show elliot p1 grin at ls_mid
    e 
    e 
    hide elliot
    show gerald p1 at ls_left
    if dress == :
        show me prolp smile at ls_right
    else:
        show me prolf smile at ls_right
    me 
    show gerald p1 smile
    g 
    if dress == :
        show me prolp
    else:
        show me prolf
    me 
    show gerald p1 surprised
    show elliot p2 sidewayshide elliot
    if dress == :
        show me prolp sideways at ls_right
    else:
        show me prolf sideways at ls_right
    me 
    hide me
    show gerald p1
    show elliot p2 smile at ls_right
    e 
    hide gerald
    if dress == :
        show me prolp smile at ls_left
    else:
        show me prolf smile at ls_left
    me 
    hide elliot
    show gerald p2 at ls_left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    g 
    if dress == :
        show me prolp sideways
    else:
        show me prolf sideways
    me 
    hide me
    show gerald p2 smile
    show elliot p1 smile at ls_right
    g 
    hide elliot
    if dress == :
        show me prolp sideways at ls_right
    else:
        show me prolf sideways at ls_right
    me 
    show gerald p2 smile at ls_mid
    hide me
    g 
    $ renpy.music.play('suspense.mp3', channel=u'music', loop=True, fadein=True)
    hide gerald
    if dress == :
        show me prolp worried at ls_left
    else:
        show me prolf worried at ls_left
    show vince p2 stern at ls_righthide me
    show vince p2 angry at ls_mid
    vince 
    hide vince
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallhide me
    show vince p2 angry at ls_left
    show gerald p1 angry at ls_right
    vince 
    hide gerald
    hide vince
    show elliot p2 glance at ls_mid
    e 
    hide elliot
    show vince p1 stern at ls_left
    show gerald p1 at ls_right
    g 
    show vince p2 angry
    show gerald p1 pout
    g 
    show vince p1 stern
    show gerald p1 angry
    g 
    hide vince
    hide gerald
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallhide me
    show gerald p1 smile at ls_midhide gerald
    if dress == :
        show me prolp worried at mid_zoom_small
    else:
        show me prolf worried at mid_zoom_smallhide me
    if dress == :
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show gerald p1 smile at ls_right
    g 
    hide gerald
    if dress == :
        show me prolp at ls_mid
    else:
        show me prolf at ls_midscene dance_empty
    with fade
    pause
    $ renpy.music.play('main_theme.mp3', channel=u'music', loop=True, fadein=True)
    if dress == :
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    hide me
    show vince at ls_mid#Missing toothy smileshow vince at ls_left
    if dress == :
        show me prolp at ls_right
    else:
        show me prolf at ls_right
    vince 
    vince 
    show vince p1 smirk
    if dress == :
        show me prolp smile
    else:
        show me prolf smile
    vince 
    vince scene bar
    show cliff p3 at ls_mid
    $ renpy.music.play('suspense.mp3', channel=u'music', loop=True, fadein=True)show cliff p3 at ls_left
    show vince p1 stern at ls_rightshow vince p2 stern
    vince 
    hide vince
    show cliff p3 angry at ls_mid
    c 
    scene car_street_night
    show vince p1 stern at ls_left
    if dress == :
        show me prolp worried at ls_right
    else:
        show me prolf worried at ls_rightif dress == :
        show me prolp irritated
    else:
        show me prolf irritated
    if dress == :
        show me prolp worried
    else:
        show me prolf worriedscene hospital_hallway
    with fade
    pause
    show elliot p2 sad at ls_left
    show julius p2 card sad teeth at ls_right
    $ renpy.music.play('sad.mp3', channel=u'music', loop=True, fadein=True)hide elliot
    hide julius
    show sofia p2 casual at ls_left
    show donovan uniform at ls_righthide sofia
    show donovan uniform at ls_midhide donovan
    show neil fs1 at ls_midn @ fs1 smirk 
    hide neilif dress == :
        show me prolp at ls_mid
    else:
        show me prolf at ls_midif dress == :
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show neil fs1 smirk at ls_righthide me
    hide neilscene hospital_night
    pause
    window hide
    show charlie sick smile at ls_midch 
    show charlie sick smile at ls_right
    show vince p2 angry at ls_left
    vince ch 
    hide vince
    if dress == :
        show me prolp  worried at ls_left
    else:
        show me prolf worried at ls_left
    me 
    ch 
    if dress == :
        show me prolp
    else:
        show me prolf
    show charlie sick frown
    me if dress == :
        show me prolp smile
    else:
        show me prolf smile
    me 
    hide me
    show charlie sick at ls_mid
    ch 
    show charlie sick at ls_right
    show vince p1 stern at ls_leftch 
    hide vince
    hide charlie
    menu speak_entry:
            if dress == :
                show me prolp worried at ls_mid
            else:
                show me prolf worried at ls_mid
            me 
            if dress == :
                show me prolp sideways at ls_left
            else:
                show me prolf sideways at ls_left
            show charlie sick frown at ls_right
            ch 
            me 
            show charlie sick
            ch 
            hide me
            hide charlie
            show neil fs2 sideways at ls_mid
            n 
            n 
            hide neil
            if dress == :
                show me prolp sideways at ls_left
            else:
                show me prolf sideways at ls_left
            show charlie sick at ls_right
            me 
            me 
            if dress == :
                show me prolp
            else:
                show me prolf
            ch 
            if dress == :
                show me prolp sideways
            else:
                show me prolf sideways
            
            hide me
            hide charlie
        :
            me 
            ch 
            me 
            me 
            ch 
            me 
            ch 
            me 
            mech 
        :
            me 
            ch 
            me 
            ch 
            mevincech 
            me 
            chme 
    if dress == :
        show me prolp at ls_left
    else:
        show me prolf at ls_left
    show charlie sick at ls_right
    ch 
    if dress == :
        show me prolp sideways
    else:
        show me prolf sidewaysif dress == :
        show me prolp irritated
    else:
        show me prolf irritated
    me 
    hide charlie
    show neil fs2 at ls_right
    n 
    if dress == :
        show me prolp sideways
    else:
        show me prolf sidewayshide me
    hide neil
    show vince p2 at ls_mid
    vince hide vince
    show charlie sick smile at ls_mid
    ch 
    ch 
    show charlie sick
    ch 
    show cliff p4 at ls_left
    show charlie sick smile at ls_right
    c 
    show charlie sick
    ch hide charlie
    hide cliff
    $ renpy.music.play('funaction.mp3', channel=u'music', loop=True, fadein=True)
    if dress == :
        show me prolp at ls_mid
    else:
        show me prolf at ls_mid
    me 
    hide me
    show cliff p4 smirk at ls_left
    show vince p1 smile at ls_righthide cliff
    hide vince
    if dress == :
        show me prolp at ls_mid
    else:
        show me prolf at ls_midif dress == :
        show me prolp surprised
    else:
        show me prolf surprised###
    show me prolf irritated
    me 
    me 
    if dress == :
        show me prolp
    else:
        show me prolf
    me me 
    me 
    if dress == :
        show me prolp smile
    else:
        show me prolf smile
    me 
    hide me
    show charlie sick at ls_midshow charlie sick smile
    ch 
    ch 
    if dress == :
        show me prolp smile at ls_left
    else:
        show me prolf smile at ls_left
    show charlie sick smile at ls_rightif dress == :
        show me prolp
    else:
        show me prolf
    ch 
    ch 
    if dress == :
        show me prolp smile
    else:
        show me prolf smile
    me 
    if dress == :
        show me prolp irritated
    else:
        show me prolf irritated
    ch 
    if dress == :
        show me prolp
    else:
        show me prolf
    ch 
    ch 
    hide charlie
    if dress == :
        show me prolp smile at mid_zoom_small
    else:
        show me prolf smile at mid_zoom_smallhide me
    if dress == :
        show me prolp smile at ls_left
    else:
        show me prolf smile at ls_left
    show charlie sick smile at ls_right
    me 
    if dress == :
        show me prolp
    else:
        show me prolf
    ch 
    ch 
    hide me
    show charlie sick smile at ls_mid
    ch 
    scene tbc
    with fade
    pause
            #### PROLOGUE END
    $ next_chapter = next_chapter + 1
    jump next_chapter_menu
