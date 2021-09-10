# Natas

Natas teaches the basics of serverside web-security.

Each level of natas consists of its own website located at `http://natasX.natas.labs.overthewire.org`, where X is the level number. There is no SSH login. To access a level, enter the username for that level (e.g. natas0 for level 0) and its password.

Each level has access to the password of the next level. Your job is to somehow obtain that next password and level up. All passwords are also stored in `/etc/natas_webpass/`. E.g. the password for `natas5` is stored in the file `/etc/natas_webpass/natas5` and only readable by natas4 and natas5.

Start here:

> Username: natas0
> Password: natas0
> URL:      http://natas0.natas.labs.overthewire.org


## 1. Natas 0 - 1

After successful login, to level 0, the following information is found:
![](images/natas/natas0a.jpg)

Looking at the source code and the password for level 1 is there ie : 
```
<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->
```

## 2. Natas 1 - 2 

> Username: natas1
> Password: gtVrDuiDfck831PqWsLEZy5gyDz1clto
> URL: http://natas1.natas.labs.overthewire.org

In this level, right clicking has been blocked but one can still be able to view the source code by using the shortcut `Ctrl+U`

```
<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->
```

## 3. Natas 2 - 3

> Username: natas2
> Password: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi
> URL: http://natas2.natas.labs.overthewire.org
