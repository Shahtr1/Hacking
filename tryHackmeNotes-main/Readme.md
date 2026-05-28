# TryHackMe Notes Repository

## Overview

This repository contains structured notes, lab walkthroughs, cheat sheets, and reference material for TryHackMe learning paths and penetration testing topics. It is organized by topic so you can quickly find hands-on exercises, commands, and concepts for web application security, network enumeration, Windows and Linux exploitation, post-exploitation, and more.

## Repository Structure

- `Attacking Kerberos/` - Notes and writeups focused on attacking Kerberos authentication and related Active Directory issues.
- `Buffer Overflow/` - Step-by-step exploit development exercises covering crash analysis, EIP overwrite, bad character identification, shellcode, and more.
- `Comand Injection/` - Command injection concepts, examples, and exploitation strategies.
- `Curl/` - Usage notes for `curl` in web application testing and enumeration.
- `File Inclusion/` - Local and remote file inclusion attack notes, payloads, and detection guidance.
- `Hydra/` - Password cracking and brute-forcing notes using Hydra.
- `Linux commands/` - Common Linux command line usage, file system navigation, process management, and privilege escalation assistance.
- `Linux PrivEsc/` - Linux privilege escalation methodologies, SUID binaries, misconfigurations, and exploit notes.
- `Metasploit/` - Meterpreter and Metasploit framework usage notes, modules, and post-exploitation techniques.
- `MITRE/` - MITRE ATT&CK mapping, tactics, techniques, and defensive context.
- `NMAP/` - Nmap scanning techniques, discovery strategies, service enumeration, and advanced scans.
- `NSLOOKUP & DIG/` - DNS enumeration notes using `nslookup`, `dig`, and related techniques.
- `Post-Exploitation Basics/` - Notes on post-exploitation tasks, data collection, credential harvesting, and persistence.
- `Powershell/` - PowerShell command references, scripting examples, and enumeration techniques.
- `Protocols & Servers/` - Notes on network protocols, service fingerprinting, and server interaction.
- `Reverse SSH/` - Reverse SSH tunneling notes and practical examples.
- `Splunk/` - Splunk fundamentals, searching, dashboards, and detection use cases.
- `SQL Injection/` - SQL injection techniques, payloads, and exploitation examples.
- `SQLMap/` - Automated SQL injection testing using `sqlmap` and payload tuning.
- `SSRF/` - Server-Side Request Forgery notes, payloads, and lab strategies.
- `TELNET & NETCAT/` - Notes for using `telnet`, `netcat`, and network connectivity troubleshooting.
- `Windows AppLocker/` - Application control bypasses and AppLocker evasion techniques.
- `Windows commands/` - Windows command line and PowerShell commands for enumeration and exploitation.
- `Windows PrivEsc/` - Windows privilege escalation concepts, service abuse, and credential discovery.
- `Wireshark/` - Packet capture analysis notes and example workflows.
- `Wordpress/` - WordPress attack surface notes, plugin vulnerabilities, and enumeration.
- `XSS/` - Cross-site scripting types, payloads, exploitation notes, and defense awareness.
- `Yara/` - YARA rule creation notes and malware detection examples.

## How to Use This Repository

1. Browse the folder names to find the topic you want to study.
2. Open the `README.md` or lab notes inside each folder for context and practical steps.
3. Use the included scripts and examples as reference when practicing in TryHackMe labs.
4. Add your own notes or update existing ones after completing exercises.

## Recommended Study Flow

1. Start with fundamentals: `Linux commands/`, `Windows commands/`, and `NMAP/`.
2. Learn exploitation basics: `Buffer Overflow/`, `SQL Injection/`, `File Inclusion/`, and `XSS/`.
3. Practice enumeration and service discovery: `NMAP/`, `NSLOOKUP & DIG/`, `TELNET & NETCAT/`, and `Protocols & Servers/`.
4. Deepen post-exploitation: `Metasploit/`, `Post-Exploitation Basics/`, `Windows PrivEsc/`, and `Linux PrivEsc/`.
5. Explore specialized topics: `Hydra/`, `Kerberos/`, `SSRF/`, `AppLocker/`, `Splunk/`, and `Yara/`.

## Notes and Best Practices

- Keep notes concise but complete: record commands used, results, and lessons learned.
- Preserve lab context: mention the machine name, room name, and specific challenge where possible.
- Use consistent formatting: include sections such as `Objective`, `Commands`, `Findings`, and `Conclusion`.
- Validate commands in a lab environment before relying on them in a report.

## Contribution Guidelines

- Add new topics as new folders when you encounter a subject not already covered.
- Update existing notes when you discover a better technique or clarify an explanation.
- Keep repository structure clean and avoid duplicating content across folders.
- Use meaningful file names for scripts and walkthroughs.

## License

This repository is intended for personal learning and note-taking. If you share or publish these notes, respect the original TryHackMe content and do not distribute answers verbatim.

---

## Quick Navigation

Use the table of contents below to jump to the most common topics:

- `Attacking Kerberos/`
- `Buffer Overflow/`
- `Linux commands/`
- `Linux PrivEsc/`
- `Metasploit/`
- `NMAP/`
- `SQL Injection/`
- `XSS/`
- `Windows commands/`
- `Windows PrivEsc/`

> Tip: If you want a specific lab or note updated next, pick a folder and I can expand that section with summaries and command examples.
