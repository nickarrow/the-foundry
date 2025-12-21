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



Okay this is a test of the new inline mechanics. Barille fires at the lead ship, his engine, and ship coming alive simultaneously  `iv-move:Enter the Fray|Edge|3|1|0|3|3|move:starforged/combat/enter_the_fray` A strong hit with a match!! Let's go!!! Barille check's his radar, how many enemy ships are out there? `iv-oracle:Number|76|Many|oracle_rollable:sundered_isles/misc/magnitude/number` Oh boy... and Barille is flying solo. Even though he got the drop on them, this isn't good. Well, let's see if we can put some distance between them and us  `iv-move:Gain Ground|Wits|5|2|0|9|10|move:starforged/combat/gain_ground` ... Barille hits the booster but then sees just as many in front of him as behind. 

Was this a trap? Let's try a move with momentum  `iv-move:Strike|Edge|3|1|0|5|9|move:starforged/combat/strike|burn=8:2`  How about oracles inserted inline into text? Will this work?  `iv-oracle:Likely|97|No|move.oracle_rollable:starforged/fate/ask_the_oracle.likely` Ha! I beat the odds! How about the disposition of these attackers?  `iv-oracle:Initial Disposition|64|Desperate|oracle_rollable:starforged/character/initial_disposition` Yup. This is going to get messy. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur luctus consequat consectetur. Nullam commodo ante nec ultrices sollicitudin.  `iv-move:Battle|Heart|1|3|0|9|9|move:starforged/combat/battle` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur luctus consequat consectetur. Nullam commodo  `iv-oracle:Creature First Look|30|Distinctive smell|oracle_rollable:starforged/creature/first_look`  ante nec ultrices sollicitudin.  `iv-noroll:Begin a Session|move:starforged/session/begin_a_session`  this is what we did. Aliquam eget dictum elit, et blandit orci. Donec dignissim eleifend mi, id pharetra ligula dignissim ac. `iv-oracle:Shipwreck Details|70|Ruined supplies or provisions|oracle_rollable:sundered_isles/shipwreck/details|cursed=7`  Cras elementum nisi non mi rutrum fringilla.  `iv-noroll:Set a Flag|move:starforged/session/set_a_flag`  `iv-noroll:Set a Flag|move:starforged/session/set_a_flag` Nunc commodo augue ante, eu rutrum est pretium eget.  `iv-move:Compel|Shadow|6|1|0|2|3|move:starforged/adventure/compel`Aenean ornare porta porttitor.  `iv-noroll:Set a Flag|move:starforged/session/set_a_flag` 



`iv-move:Gather Information|Wits|3|2|2|9|1|move:starforged/adventure/gather_information|adds=1(Using my special asset bonus),1(Second add to show this works)` Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean quis eros eget justo sagittis imperdiet. Nulla nec cursus lectus. Suspendisse libero sapien, luctus in ornare a, iaculis in nibh.  

`iv-move:Enter the Fray|Heart|2|3|0|6|9|move:starforged/combat/enter_the_fray|burn=8:2`  Quisque condimentum consectetur purus at bibendum. Duis sollicitudin finibus mauris, vel semper enim ornare nec.  `iv-oracle:Combat Action|42|Leverage the terrain or surroundings|oracle_rollable:starforged/misc/combat_action` Maecenas et mi eu urna molestie rhoncus at vel ligula. Nulla gravida ante nisi, id pulvinar diam sodales et.  `iv-progress:Investigate and report on the rumored horrors of Reck|0|5|3`  Nam id justo at diam euismod eleifend ac eget arcu.
