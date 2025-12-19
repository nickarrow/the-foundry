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

