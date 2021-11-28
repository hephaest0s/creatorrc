# Creatorrc
Create torrc files optimized for speed, security, or avoiding captchas

## Why?
[Tor](https://torproject.org) uses a torrc file to specify some of the Tor-software routing behavior.
With creatorrc, you can choose to optimize your torrc for speed, for security and for avoiding capchas.
Creattorc will create a tor_config.txt file in your working directory containing lines to add to your torrc file.

```shell
sudo python creatorrc.py
```
*Creatorrc does not work in [Tails](https://tails.boum.org/), yet.

### Overview
#### Sector - secure-tor
Sector excludes questionable relays, like ones running on Windows XP or an old version of the Tor software. It also chooses guards that are close to home because, "No reason for a Rio client to connect to a Moskow guard."

#### Speetor - Speed up large file exchange
Speetor selects the fastest 1000 relays as guards, the fastest 1000 exists as exit, and excludes the slowest 4000 relays so they don't become middle relays. This probably does more for throughput than for latency.

Up/downloading large files over Tor probably reduces your anonymity, and reducing the set of nodes you choose from based on their speed certainly has some negative impact on your anonymity.

#### Evator - evade captchas while browsing tor
Evator selects slow-ish exit nodes, which are likely not used by many Tor (ab)users. This reduces the chance that you will be asked to fill out a captcha while browsing the traditional internet.

Evator negatively affects your anonymity.

### Why would I ever change my torrc in a way that could reduce my anonymity?
I believe Sector increases your anonymity, but I could be wrong. Please tell me why if you think Sector makes you less secure!

As for speetor and evator, unfortunately, in this world at this moment, you have to trade security/anonymity if you want more usability.
If you feel you are better off with potentially less security/anonymity but more download speed or less captchas, then this tool enables you to decide that for yourself.


### Supported command line arguments:

- -h or --help: show help message, exit.
- --sector	Secure Tor configuration.
- --speetor	If speed is what you need.
- --evator	For evading captchas when browsing traditional websites.


### Contact

[hephaestos@riseup.net](mailto:hephaestos@riseup.net) - PGP/GPG Fingerprint: 8764 EF6F D5C1 7838 8D10 E061 CF84 9CE5 42D0 B12B
