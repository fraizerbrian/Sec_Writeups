# WIFI ATTACKS





-----------------------------------------------------------
# Writeups
## Challenge Name : WPA Crack
 
Challenge Category : Machines

Challenge Level : Medium

Challenge Description : You are conducting a WIFI pentest, Handshake has been captured and your task is to crack it

Flag format is just the password 

 Link:https://hubchallenges.s3-eu-west-1.amazonaws.com/Machines/wpa943050264305852656243865.cap

**Solution**

First step let's download the link.

we will be using aircrack-ng to crack and use the rockyou.txt wordlist for this.

```
aircrack-ng wpa943050264305852656243865.cap -w /usr/share/wordlists/rockyou.txt
```

we get the key which is the flag

> flag : biscotte
