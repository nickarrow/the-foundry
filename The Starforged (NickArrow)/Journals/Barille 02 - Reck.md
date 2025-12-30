# [[Barille 02 - Reck]]

`iv-noroll:Begin a Session|move:starforged/session/begin_a_session`  `iv-meter:Momentum|5|6` 

EXT. SNUB FIGHTER 27 REENTRY TO ACKRISS-2

The 27 bursts through the purple and green clouds of [[Ackriss-2]]. Scans are showing a toxic atmosphere and remnants of ash. Likely from regular volcanic eruptions. 

```
BARILLE BLACK
This is SN27 on approach, anyone down there?

NO RESPONSE
```

> [[Reck]] itself is built into the rock cliffs of a large canyon. The rock providing a natural shield from the harsh atmosphere. A settlement supporting thousands, out in the frontier of the Expanse. 

Barille circles the settlement, and sees an impact crater and wreckage. It looks like the attacking frigate crashed into the settlement on the south side. Not good. Smoke is coming out of the wreckage. 

Barille eyes what looks like a landing port nearby. The auto-landing sequence takes over, and Barille tries to ping the transport ship. 

```
BARILLE BLACK
Hey, did you make it down here? Any injured. This is Barille. 

COMMS OFFICER
Reading you Barille, yeah, we’re all in one piece. That was you in the fighter right? 

BARILLE BLACK
Yeah, any idea who that was?

COMMS OFFICER
They transmitted a pretty long message, something about the Ascendancy of the Awakened Worlds? That mean anything to you?

BARILLE BLACK
Nope. Never heard of them. Trouble is, the suicided into Reck, so I guess we can’t ask them. I can't raise anyone down there, trouble?

COMMS OFFICER
Yeah, the impact shook the entire canyon and its been pretty much disaster mode down here. Reck is pretty wild on a good day, but the suicide attack has everyone either panicked or fighting fires. 

BARILLE BLACK
Got it. Thanks for the info. Barille out. 
```

> So we have a name. `iv-entity-create:Faction|Ascendancy of the Awakened Worlds|The Starforged (NickArrow)/Factions/Ascendancy of the Awakened Worlds.md` A bit of a mouthful, and clearly not the most inconspicuous bunch. 

Barille check's to see if the landing has an automated repair system. Negative. Okay, can I send a message? 

```
BARILLE BLACK - Typing via hand terminal
*Landing bay 17, SN27 - Barille Black, requesting repairs.* 

Yeah, I'm going to need to talk to someone. 
```

 > Okay, so that’s fine. Need to start investigating for the [[Risen Union]] anyway. Let's go for a walk. 

Before leaving Barille sends out an encoded wideband broadcast.  `iv-noroll:Reach a Milestone|move:starforged/quest/reach_a_milestone` 

![[Message 01 - Barille Black]]

`iv-track-advance:Expose the darkness behind the attacks across Devil's Chain and stop it from spreading|The Starforged (NickArrow)/Progress/Expose the darkness behind the attacks across the sector and stop it from spreading.md|0|2|extreme|1` 

Barille get's out of his fighter and sets off. He reflects on the little bit of information he has about the so called "horrors" of Reck. The job just stated "terrifying manifestations" not a lot to go on. Need to ask around. And someone has gone missing, let's find anyone in charge.  `iv-move:Gather Information|Wits|1|2|0|9|4|move:starforged/adventure/gather_information` 

> What is the dire threat or unwelcome truth?  `iv-oracle:Action + Theme|68|Journey Opportunity|oracle_rollable:starforgedsupp/templates/actiontheme` Reck is a frontier settlement with an *obvious social stratification*. It looks like there may be a bit of a revolution happening, and Barille just found himself smack in the middle of it. Good luck getting your ship repaired any time soon, and also...  `iv-oracle:Pay the Price|98|Your vehicle suffers damage, Your action causes collateral damage or has an unintended effect|move.oracle_rollable:starforged/fate/pay_the_price.pay_the_price` 
> 
> Looks like my message has attracted the wrong kind of attention. 

A sudden crash and screeching of metal is heard from behind Barille, in the landing bay. He runs back to see the large grapple hook digging into the side of the 27. `iv-meter:Snub Fighter / Integrity|2|1` 

There's also a small group of folk that have gathered, scavengers or otherwise and two big guys step in front of Barille. 

```
BARILLE BLACK
Hey friends, seems like you have gone and put a hook into my ship. 

SCAVENGER 1
I think you mean our ship. You picked the wrong day to show up, we control the entire east ward now. 

BARILLE BLACK
Yeah, that's fine. *Barille pulls out a cigarette and lites it* You can have the east ward, but I'm going to need my ship. How about, you ungrapple it and we don't have to turn this into a... thing.
```

`iv-move:Compel|Heart|5|3|0|4|5|move:starforged/adventure/compel`  `iv-meter:Momentum|6|7` 

```
SCAVENGER 1
Huh. I figured you we're just going to try and pull a gun and... look if you stay out of our way, you can keep this ship. Looks pretty beat up anyway. Just remember, the east ward is ours.

BARILLE BLACK
Got it. And who is "Us" exactly? 

SCAVENGER 1
We're with "Murad", and she owns it. Got that!

BARILLE BLACK
Understood. *Takes a long drag on the *cigarette*, congrats to her. 
```

`iv-noroll:Take a Break|move:starforged/session/take_a_break` 

Session outline:
- Get to Reck
- Assist if needed
- Start ship repairs (if possible)
- Begin investigation of [[Investigate and report on the rumored horrors of Reck]]


---

Example Code blocks

Move code block
```iron-vault-mechanics
move "[Gather Information](datasworn:move:starforged\/adventure\/gather_information)" {
    roll "Wits" action=1 adds=0 stat=2 vs1=9 vs2=4
}
```


Oracle code block
```iron-vault-mechanics
oracle name="[Character Oracles \/ First Look](datasworn:oracle_rollable:starforged\/character\/first_look)" result="Slight" roll=74
```

Multi-oracle code block
```iron-vault-mechanics
oracle-group name="NPC: Kayla “Rover” Dykstra" {
    oracle name="[Character Oracles \/ Character Name \/ Given Name](datasworn:oracle_rollable:starforged\/character\/name\/given_name)" result="Kayla" roll=50
    oracle name="[Character Oracles \/ Character Name \/ Callsign](datasworn:oracle_rollable:starforged\/character\/name\/callsign)" result="Rover" roll=73
    oracle name="[Character Oracles \/ Character Name \/ Family Name](datasworn:oracle_rollable:starforged\/character\/name\/family_name)" result="Dykstra" roll=84
    oracle name="[Character Oracles \/ First Look](datasworn:oracle_rollable:starforged\/character\/first_look)" result="Scruffy" roll=68
    oracle name="[Character Oracles \/ Initial Disposition](datasworn:oracle_rollable:starforged\/character\/initial_disposition)" result="Unfriendly" roll=85
}
```

Progress track code block
```iron-vault-mechanics
track name="[[The Starforged (NickArrow)\/Progress\/Testproress.md|testproress]]" status="added"
```

Entity creation
```iron-vault-mechanics
oracle-group name="Creature: New Creature" {
    oracle name="[Creature Oracles \/ Environment](datasworn:oracle_rollable:starforged\/creature\/environment)" result="Land" roll=19
    oracle name="[Basic form](datasworn:oracle_rollable:starforged\/creature\/basic_form\/land)" result="Amorphous \/ elemental" roll=4
    oracle name="[Creature Oracles \/ Scale](datasworn:oracle_rollable:starforged\/creature\/scale)" result="Medium (person-sized)" roll=43
    oracle name="[Creature Oracles \/ Creature First Look](datasworn:oracle_rollable:starforged\/creature\/first_look)" result="Prominent wings or fins" roll=84
}
```



Example inline mechanics
Barille pulls up the UI from his hand terminal, and initiates the pre-launch sequence for his snub fighter. Green check marks. Great, let’s get there. Barille takes off to the hanger bay. Does he get there without issue? `iv-oracle:50/50|30|Yes|move.oracle_rollable:starforged/fate/ask_the_oracle.fifty_fifty` The ship rocks a bit, sounds like the transport pilot is making moves, but no major new strikes. 

Barille jumps into the 27 (SN-27 snub fighter), the engines are already humming. He punches the launch control and blasts out into the void.

`iv-move:Enter the Fray|Snub Fighter / Integrity|5|4|0|10|3|move:starforged/combat/enter_the_fray`  `iv-track-create:Fend off attackers until the transport can escape|The Starforged (NickArrow)/Progress/Barille/Fend off attackers until the transport can escape.md` `iv-initiative:Position|in control|in control` With a roll of the controls, Barille immediately sees the hostiles. Looks like a large frigate with at least 3 fighters circling. The transport ship is putting on a significant burn, and there are no other friendlies. Not great odds, but Barille might be able to catch them by surprise. 

```
BARILLE
Let’s see how good their scans are. 
```

Barille shields the engines, blocks EM, and goes ballistic with a burst of RCS to set up an ambush for the returning fighters.  `iv-move:Gain Ground|Shadow|5|1|0|3|4|move:starforged/combat/gain_ground` They have no idea. 

> This seems like a small time raid, and under normal circumstances, it would have been successful. Not today fellas. Barille fires the 27's railguns at the lead ship, his engine, and ship coming alive simultaneously.   `iv-move:Strike|Edge|3|1|1|9|6|move:starforged/combat/strike|burn=7:2|adds=1(ambush)`  `iv-initiative:Position|in control|in a bad spot` 

The first ship erupts, and before the others can react, Barille's fires again hitting the second target. These guys definitely didn't see him, but now they do. Barille can’t quite get a shot on the third, which starts burning away.... And then the frigate starts firing. Alarms are going off, missiles inbound, and this thing seems to have lots of guns. Barille burns and rolls the ship to evade.

```
BARILLE BLACK
ahhhhHHHHHHH! 
```

`iv-move:React Under Fire|Edge|3|1|0|9|5|move:starforged/combat/react_under_fire` Barille dodges the ballistic rounds, but there's no answer for the missiles. Barille is burning hard, but one catches him and detonates.  `iv-meter:Snub Fighter / Integrity|4|2`  `iv-move:Withstand Damage|Snub Fighter / Integrity|4|2|0|4|2|move:starforged/suffer/withstand_damage`  `iv-meter:Momentum|2|3`  `iv-initiative:Position|in a bad spot|in control` The hit is brutal, engine and navigation damage, but still flying. We're still being shot at, but the burn has put some distance between Barille and the attackers. 

Really needing to stay away from that frigate. A check of on the transport ship, and yup, they are making atmo at [[Ackriss-2]]. If Barille leaves the fight now, they'll likely just pursue the transport ship to the surface. They didn't see me before, let's try that trick again. Cutting engines, and turning up EM damping. Let's disappear and see what they do.  `iv-move:Gain Ground|Shadow|4|1|0|1|2|move:starforged/combat/gain_ground`  `iv-meter:Momentum|3|5`  `iv-track-advance:Fend off attackers until the transport can escape|The Starforged (NickArrow)/Progress/Barille/Fend off attackers until the transport can escape.md|24|32|dangerous|1` It is quiet for 30 seconds and they have no idea.

```
BARILLE BLACK
Is this really going to work again? Hahaha, suckers. I guess they're not used to anyone fighting back. Let's put a round in your drive cone. 
```

`iv-progress:Fend off attackers until the transport can escape|8|2|10|The Starforged (NickArrow)/Progress/Barille/Fend off attackers until the transport can escape.md`  `iv-oracle:Take Decisive Action|99|It gets complicated: The true nature of a foe or objective is revealed|move.oracle_rollable:starforged/combat/take_decisive_action.take_decisive_action` After another 30 seconds, the frigate starts to burn towards the planet. As they pivot, Barille lines up the shot and fires. A direct hit, and they are out of commission... except they aren't? `iv-oracle:Action + Theme|75|Create World|oracle_rollable:starforgedsupp/templates/actiontheme` Their ship should be out of commission, but somehow it is still accelerating? The third fighter is nowhere on scans and something is very wrong. 