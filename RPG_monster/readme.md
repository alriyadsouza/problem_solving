# RPG Quest Challenge

## Problem Statement

While playing an RPG game, you were assigned to complete one of the hardest quests in this game. There are `n` monsters you'll need to defeat in this quest. Each monster `i` is described with two integer numbers - `power_i` and `bonus_i`. To defeat this monster, you'll need at least `power_i` experience points. If you try fighting this monster without having enough experience points, you lose immediately. You will also gain `bonus_i` experience points if you defeat this monster. You can defeat monsters in any order.

The quest turned out to be very hard - you try to defeat the monsters but keep losing repeatedly. Your friend told you that this quest is impossible to complete. Knowing that, you're interested, what is the maximum possible number of monsters you can defeat? (*Question difficulty level: Hardest*)

### Input

The first line contains an integer, `n`, denoting the number of monsters.  
The next line contains an integer, `e`, denoting your initial experience.  
Each line `i` of the `n` subsequent lines (where `0 ≤ i < n`) contains an integer, `power_i`, which represents power of the corresponding monster.  
Each line `i` of the `n` subsequent lines (where `0 ≤ i < n`) contains an integer, `bonus_i`, which represents bonus for defeating the corresponding monster.

### Sample Cases:

| Input | Output | Output Description |
|-------|--------|---------------------|
| 2<br>123<br>78<br>130<br>10<br>0 | 2 | Initial experience level is 123 points.<br><br>Defeat the first monster having power of 78 and bonus of 10.<br>Experience level is now 123+10=133.<br><br>Defeat the second monster. |
| 3<br>100<br>101<br>100<br>304<br>100<br>1<br>524 | 2 | Initial experience level is 100 points.<br><br>Defeat the second monster having power of 100 and bonus of 1.<br>Experience level is now 100+1=101.<br><br>Defeat the first monster having power of 101 and bonus of 100.<br>Experience level is now 101+100=201.<br><br>The third monster can't be defeated. |
