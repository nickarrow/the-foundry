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

Before leaving  `iv-noroll:Reach a Milestone|move:starforged/quest/reach_a_milestone` Barille sends out an encoded wideband broadcast. 

![[Message 01 - Barille Black]]

`iv-track-advance:Expose the darkness behind the attacks across Devil's Chain and stop it from spreading|The Starforged (NickArrow)/Progress/Expose the darkness behind the attacks across the sector and stop it from spreading.md|0|2|extreme|1` 

Barille reflects on the little bit of information he has about the so called "horrors" of Reck. The job just stated "terrifying manifestations" not a lot to go on. Need to ask around. And someone has gone missing, let's find anyone in charge.  `iv-move:Gather Information|Wits|1|2|0|9|4|move:starforged/adventure/gather_information` 

*note to self - need to resolve this miss from Gather Information.*

Session outline:
- Get to Reck
- Assist if needed
- Start ship repairs (if possible)
- Begin investigation of [[Investigate and report on the rumored horrors of Reck]]


---

*Moving this block down here so I can test block rendering. Ignore for story purposes.*
```iron-vault-mechanics
move "[Gather Information](datasworn:move:starforged\/adventure\/gather_information)" {
    roll "Wits" action=1 adds=0 stat=2 vs1=9 vs2=4
}
```
