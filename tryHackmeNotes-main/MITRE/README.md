# MITRE

> Shahrukh Tramboo | March 24th, 2022

--------------------------------------

**Basic Terminology**

-	APT is an acronym for Advanced Persistent Threat.
 	This can be considered a team/group (threat group), or even country (nation-state group), that engages in long-term attacks against organizations and/or countries.

-	TTP is an acronym for Tactics, Techniques, and Procedures,

	The Tactic is the adversary's goal or objective.
	The Technique is how the adversary achieves the goal or objective.
	The Procedure is how the technique is executed.

------------------------------------------

**ATT&CK® Framework**

 In 2013, MITRE began to address the need to record and document common TTPs (Tactics, Techniques, and Procedures) that APT (Advanced Persistent Threat) groups used against enterprise Windows networks.

 This started with an internal project known as FMX (Fort Meade Experiment).

 Within this project, selected security professionals were tasked to emulated adversarial TTPs against a network, and data was collected from the attacks on this network. The gathered data helped construct the beginning pieces of what we know today as the ATT&CK® framework.

 ---------------------------------------------

**CAR Knowledge Base**

The official definition of CAR is "The MITRE Cyber Analytics Repository (CAR) is a knowledge base of analytics developed by MITRE 


**CAR-2020-09-001: Scheduled Task - FileAccess**

In order to gain persistence, privilege escalation, or remote execution, an adversary may use the Windows Task Scheduler to schedule a command to be run at a specified time, date, and even host.
Task Scheduler stores tasks as files in two locations - C:\Windows\Tasks (legacy) or C:\Windows\System32\Tasks. 
Accordingly, this analytic looks for the creation of task files in these two locations.







 