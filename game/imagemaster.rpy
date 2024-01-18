# Locations
image bar = "images/bg/bar.webp"
image car_street = "images/bg/car_street.webp"
image dance = "images/bg/dance.webp"
image gladius_day = "images/bg/gladius_day.webp"
image gladius_night = "images/bg/gladius_night.webp"
image hospital_hallway = "images/bg/hospital_hallway.webp"
image house_day = "images/bg/house_day.webp"
image house_night = "images/bg/house_night.webp"
image icebox_entrance = "images/bg/icebox_entrance.webp"
image icebox_entrance_peep = "images/bg/icebox_entrance_peep.webp"
image infirmary_day = "images/bg/infirmary_day.webp"
image infirmary_night = "images/bg/infirmary_night.webp"
image living_day = "images/bg/living_day.webp"
image living_night = "images/bg/living_night.webp"
image room_day = "images/bg/room_day.webp"
image room_night = "images/bg/room_night.webp"
image station = "images/bg/train_station.webp"
image station_street = "images/bg/station_st.webp"
image store_day = "images/bg/store_day.webp"
image store_night = "images/bg/store_night.webp"
image tbc = "images/bg/tbc.webp"
image car_street_night = "images/bg/car_street_night.webp"
image hospital_day = "images/bg/hospital_day.webp"
image hospital_night = "images/bg/hospital_night.webp"
image dance_empty = "images/bg/dance_empty.webp"
image tbc = "images/bg/tbc.webp"


# Characters
image andrew = "images/characters/andrew/andrew.webp"
image bailey = "images/characters/bailey/bailey.webp"
image charlie = "images/characters/charlie/charlie.webp"
image cleo = "images/characters/cleo/cleo.webp"
image cliff = "images/characters/cliff/cliff p2.webp"
image donovan = "images/characters/donovan/donovan p1.webp"
image elliot = "images/characters/elliot/elliot p1 grin.webp"
image gerald = "images/characters/gerald/gerald p1.webp"
image julius = "images/characters/julius/julius p1.webp"
image june = "images/characters/june/june.webp"
image louis = "images/characters/louis/louis.webp"
image me = "images/characters/me/me.webp"
image neil = "images/characters/neil/neil fs1.webp"
image sofia = "images/characters/sofia/sofia p1.webp"
image vera = "images/characters/vera/vera smile.webp"
image vince = "images/characters/vince/vince.webp"

# CGs
image cliff_prologue = "images/cg/cliff_prologue.webp"
image doneil_prologue = "images/cg/doneil_prologue.webp"
image elliot_prologue = "images/cg/elliot_prologue.webp"
image gerald_prologue = "images/cg/gerald_prologue.webp"
image julfia_prologue = "images/cg/julfia_prologue.webp"
image vince_prologue = "images/cg/vince_prologue.webp"

##### Outfits
image card_free = "images/card_free.webp"
image card_heart = "images/card_heart.webp"
image dress_15 = "images/cg/dress15.webp"

transform ls_left:
    xalign 0.263

transform ls_right:
    xalign 1.01

transform ls_mid:
    xalign 0.66

transform three_left:
    xalign -0.1
transform three_right:
    xalign 1.2

transform character_zoom:
    size(1600,900) crop (800, 900, 0, 0)
    linear 5.0 crop (0, 0, 1600, 900)

transform mid_zoom:
    xalign 1.65
    yalign 0.46
    zoom 2.0

transform mid_zoom_small:
    xalign 1.05
    yalign 0.6
    zoom 1.5

transform left_zoom:
    xalign 0.3
    yalign 0.6
    zoom 1.1

transform shrink:
    zoom 0.8
    yalign 1.0

transform outfit_zoom:
    zoom 2.0
    yalign 1.0
    pause 0.5
    linear 6.0 yalign -0.0
