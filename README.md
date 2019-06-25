Class aimed at parsing MSTA readback records that provide a ULONG of a 16 bit string and nothing human
readable.

E.g. there is no way to check if a motor is homed via a simple query:

```
> caget SR03BM01HU02DMC05:G.MSTA
> 18723
```

So instead:
```
from MSTAparser import MSTA

filterwheel = MSTA(18723)
filterwheel.homed
1

#OR 

MSTA(18723).homed
1

```



