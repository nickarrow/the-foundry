# [[Barille 01 - Beginnings]]
> This is the beginning of a great adventure...

INT. LONG-RANGE TRANSPORT SHIP, RENTED CABIN
[[Barille Black]] is sleeping on a stiff bed, wearing his dark blue suit and tie, loosened at the neck. He has dark curly hair, and the stubble of a beard. `ROLL CHARACTER GOAL` 
```iron-vault-mechanics
oracle name="[Character Oracles \/ Character Goal](datasworn:oracle_rollable:starforged\/character\/goal)" result="Roll twice" roll=91 {
    oracle name="[Character Oracles \/ Character Goal](datasworn:oracle_rollable:starforged\/character\/goal)" result="Gain Riches" roll=38
    oracle name="[Character Oracles \/ Character Goal](datasworn:oracle_rollable:starforged\/character\/goal)" result="Seek Power" roll=72
}
```

> Growing up within the domain of a founder clan, the [[Circle of the Elder Stars]], Barille's childhood was difficult. Not being of notable bloodline meant that he was relegated to the lower ranks of the Circle's caste system. However, his ability to fight, endure, and complete jobs earned him a reputation that helped elevate his status. Working jobs meant that he was able to grow his reputation, which provided access to bigger and better jobs. Barille has since left the Circle, for reasons unknown, and is currently adrift in the sector [[Devil's Chain]], moving from job to job. 
> 
> When Barille left the Circle he made a vow, to [[Establish a new noble house in the Circle of the Elder Stars]]. A house that would surpass all others and become the dominant authority within the faction. 
> 
> Barille is on a transport ship. Not having an FTL capable ship of his own, he has to buy or barter his way to systems or sectors. He is already on a job, a posted job for the [[Risen Union]] (RU). The RU has a reputation of keeping its cards close to the vest, but the jobs pay well, even if they tend to come with little information and lead to more questions than answers. 
> 
> Barille has sworn a vow for this job, to [[Investigate and report on the rumored horrors of Reck]], and he means to see it through. 

Barille is suddenly thrown out of his rented bed aboard the transport ship as the ship rocks violently. Either it is under attack or something catastrophic has happened. The damage is significant.

BARILLE
Good gods. I’m trying to get some sleep TODAY! 

He stumbles to his feat, pushes buttons on the nearby panel trying to access the ship’s systems.

```iron-vault-mechanics
actor name="[[Campaigns\/The Starforged\/Characters\/Barille Black\/Barille Black.md|Barille Black]]" {
    move "[Gather Information](datasworn:move:starforged\/adventure\/gather_information)" {
        roll "Wits" action=2 adds=0 stat=2 vs1=1 vs2=4
    }
}
```

Barille opens crew door to see klaxons flashing, people shouting down the call. He sees a crewman running by.

BARILLE
Hey, what's going on? 

CREWMAN
We're under attack, someone's shooting! 
 
> Yeah, this is not ideal. This is a transport, not a warship. Not wanting to explode, 

Barille reaches into his pocket and flips a black iron coin. He catches it and then says to himself.

BARILLE
On this iron I swear to [[Fend off attackers until the transport can escape]]. 

```iron-vault-mechanics
actor name="[[Campaigns\/The Starforged\/Characters\/Barille Black\/Barille Black.md|Barille Black]]" {
    move "[Swear an Iron Vow](datasworn:move:starforged\/quest\/swear_an_iron_vow)" {
        roll "Heart" action=3 adds=0 stat=3 vs1=4 vs2=9
    }
}
```
> Okay - not sure who these hostiles are, nor why they’d be going after us? Straight up piracy? Maybe if there was more time, I could find out. For now…

Barille pulls up the UI from his hand terminal, and initiates the pre-launch sequence for his snub fighter. Green check marks. Great, let’s get there. Barille takes off to the hanger bay. 

```iron-vault-mechanics
- "Does he get there without issue?" {
    oracle name="[Ask the Oracle \/ 50\/50](datasworn:move.oracle_rollable:starforged\/fate\/ask_the_oracle.fifty_fifty)" result="Yes" roll=30
}
```

The ship rocks a bit, sounds like the transport pilot is making moves, but no major new strikes. Strapped into SN-27, the engines are humming, he punches the launch control and blasts out into the void. 

```iron-vault-mechanics
actor name="[[Campaigns\/The Starforged\/Characters\/Barille Black\/Barille Black.md|Barille Black]]" {
    move "[Enter the Fray](datasworn:move:starforged\/combat\/enter_the_fray)" {
        roll "Snub Fighter \/ Integrity" action=4 adds=0 stat=4 vs1=4 vs2=9
    }
}
```
With a roll of the controls, Barille sees the immediate forces. Looks like a large frigate with at least 3 fighters circling. The transport ship is putting on a significant burn, and there are no other friendlies. 

BARILLE
Let’s see how good their scans are. 

Barille shields the engines, blocks EM, and goes ballistic with a burst of RCS to set up an ambush for the returning fighters. 

```iron-vault-mechanics
actor name="[[Campaigns\/The Starforged\/Characters\/Barille Black\/Barille Black.md|Barille Black]]" {
    move "[Gain Ground](datasworn:move:starforged\/combat\/gain_ground)" {
        roll "Shadow" action=5 adds=0 stat=1 vs1=3 vs2=4
    }
}
```

They have no idea. This seems like a small time raid, and under normal circumstances, it would have been successful. Not today fellas.

> Barille fires at the lead ship, his engine, and ship coming alive simultaneously. 

```iron-vault-mechanics
actor name="[[Campaigns\/The Starforged\/Characters\/Barille Black\/Barille Black.md|Barille Black]]" {
    move "[Strike](datasworn:move:starforged\/combat\/strike)" {
        add 1 "ambush"
        roll "Edge" action=2 adds=1 stat=1 vs1=4 vs2=9
        burn from=7 to=2
    }
}
```

BARILLE BLACK
Yeaaaaaaaaaahh! 

> The first ship erupts, and before the others can react, the second one does too. These guys weren’t expecting a fight. Barille can’t quite get a shot on the third, which starts burning away. And then the frigate starts firing. Alarms are going off, missiles inbound, and this thing seems to have lots of guns. Barille burns and rolls the ship to evade. 
> IN A BAD SPOT



Okay, let's play out a session to test all of the new inline features. First let's  `iv-noroll:Begin a Session|move:starforged/session/begin_a_session` - Barille is walking along the busy market streets of...  `iv-entity-create:Settlement|Reprise|The Starforged (NickArrow)/Locations/Planets/Reprise.md` *The generate entity command with imbedded links is neato!* Okay, wait, why is Barille here?  `iv-oracle:Inciting Incident|53|Locate a downed spacer on an uninhabited planet|oracle_rollable:starforged/campaign_launch/inciting_incident` Okay, so he is looking for information, maybe a clue that will help out somehow. 

First thing, let's do  `iv-move:Gather Information|Wits|2|2|0|4|10|move:starforged/adventure/gather_information` Miss. Yikes. What could the unwelcome truth be?  `iv-oracle:Action + Theme|19|Arrive Creation|oracle_rollable:starforgedsupp/templates/actiontheme`  - Okay that makes me think that this is a goldrush of sorts. The rumors of this downed spacer have created a ton of competition from treasure hunters and the like, looking to hit paydirt. This means that there are going to be lots of false leads, and competition along the way. But why? `iv-oracle:Descriptor+Focus|33|Conspicuous Technology|oracle_rollable:starforgedsupp/templates/descriptorfocus` Okay that this some sort of lost technology, maybe from the Exodus. Barille flips is black iron coin and to swear  `iv-move:Swear an Iron Vow|Heart|5|3|0|7|7|move:starforged/quest/swear_an_iron_vow` A match!  `iv-meter:Momentum|2|4` 

All these poor sods, amateurs, this sort of tracking is what Barille does best! And a little competition is just going to make it more fun. Barille thinks about the vow he made when he took this job,  `iv-track-create:Find and recovery the lost tech for the RU|The Starforged (NickArrow)/Progress/Find and recovery the lost tech for the RU.md` - In fact, so much excitement over the treasure hunt, he could use this to his advantage. Barille finds the nearest pub that looks like a rumor mill, and decides to buy a few drinks and send the fledgling treasure hunters in the wrong direction.  `iv-move:Compel|Shadow|4|1|0|10|6|move:starforged/adventure/compel` so.... that didn't work.  `iv-noroll:Pay the Price|move:starforged/fate/pay_the_price` means that he walked into the wrong pub. He was trying to plant information, but then realizes he's low-key surrounded. Looks like he's about to get jumped for information. 

"Guys, guys... what if we just split the reward money? eh? Any takers?"  `iv-move:Enter the Fray|Wits|4|2|0|5|10|move:starforged/combat/enter_the_fray`  `iv-meter:Momentum|4|6` They chuckle and then throw a beer bottle - Barille sees it happen and dodges over the bar as the barfight begins!   `iv-initiative:Position|out of combat|in a bad spot` and this fight is going to be easy rank  `iv-track-create:Escape the barfight|The Starforged (NickArrow)/Progress/Escape the barfight.md` Barille decides to leap back over the bar, maybe they were expecting a pushover?  `iv-move:Clash|Iron|4|2|1|8|3|move:starforged/combat/clash|adds=1(Brawler asset)` He tackles a smaller guy, and they definitely weren't expecting it `iv-track-advance:Escape the barfight|The Starforged (NickArrow)/Progress/Escape the barfight.md|0|12|troublesome|1` and then is kicked swiftly in the ribs by a massive beast of person  `iv-meter:Health|5|4` 

Okay fella's let's dance! Barille spins himself around and flips back onto his feat, he circles away from the front attackers - eyeing the door to leave on the far side of the room.  `iv-move:React Under Fire|Wits|2|2|0|2|3|move:starforged/combat/react_under_fire` Only a three attackers, but one is big. Barille thinks he can take them.  `iv-meter:Momentum|6|7` and  `iv-initiative:Position|in a bad spot|in control` A spin kick at the nearest guy,  `iv-move:Strike|Iron|2|2|0|5|7|move:starforged/combat/strike|burn=7:2` with a little help from momentum  `iv-track-advance:Escape the barfight|The Starforged (NickArrow)/Progress/Escape the barfight.md|12|36|troublesome|2`  `iv-initiative:Position|in control|in a bad spot` he is able to take two of them down. But the big guy draws a pistol. Wow, this just got real. Barille kicks a chair in an attempt to knock the gun away,  `iv-move:React Under Fire|Iron|6|2|0|9|9|move:starforged/combat/react_under_fire` , suddenly it all goes dark. Yeah, there was a forth guy... and he just clubbed Barille who is now unconscious. 

Hello world!