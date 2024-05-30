 # UNIVERSAL WIN95 ACTIVATOR
 Windows 95 Product Key generator written in Python. Pointless? Maybe... but it gets the job done! 

 ## The WIN95 Product Key algorithm
 I've caught myself hitting the hard wall of ignorance a while back ago, while trying to setup and boot into a W95 vm.
 Never in the last two decades I have found myself lost in the art of bypassing Microsoft's extremely flawed activation systems but,
 since i was nowhere being alive back in 1995, nor have I ever owned/used a copy of W95, I needed help.
 Since search engines nowadays are practically useless when it comes to, well, their job of finding what you're looking for, I went to
 [blackbox.ai](https://blackbox.ai/) looking for a concise answer, and it answered with this:

 ```blackbox's answer
...For CD Keys, which are 10-digit keys in the format XXX-XXXXXXX, the first segment (also called the site) must be three
digits long, but it can't be any random number. The combinations 333, 444, 555, 666, 777, 888, and 999 are invalid.
The second segment's digit sum must be divisible by 7, and additionally, the last digit of this segment cannot be 0 or
greater than or equal to 8.

For OEM Keys, which are in the format XXXXX-OEM-XXXXXXX-XXXXX, the first segment represents a date, with the first three
digits being the Julian date and the last two being the printing year. The date can be anything between 001 and 366,
and the year cannot be lower than 95 or above 03. The second segment is always "OEM". The third segment's digit sum must
also be divisible by 7, with the additional requirement that the first digit of this segment must be 0.
The fourth segment is irrelevant as long as it's the correct length...
 ```

 So, having what I was looking for, I did what every sane individual would do:
 ~~googling for working keys~~ (too easy)
 ~~calculating a valid key based on the provided algorithm~~ (who tf knows math?!)
 created three overcomplicated scripts that do the job for me!

## How to use
As I said before, UWAct is split into three python scripts:

+ No.1 > keygen.py,
  which is the service that calculates valid keys following W95's Product Key algo

+ No.2 > gui.py,
  pretty self explainatory, gui is the dedicated, TkInter-based GUI for UWAct

+ No.3 > uwact,
  disguised as a shell script, this too has python under its hood. Imports argparse and
  lets you choose between using the terminal directly (running `./path/to/uwact`), or
  UWAct's GUI (by appending `-g` or `--gui` to the aforementioned command)

 ## What's the point of this?
 Well, activating Windows 95, I guess... in 2024... prolly in a vm cause i dont think W95
is still supported by the latest Python build :|

To be fair, that was my use case scenario, which is not only pretty niche but overall
completely dumb, as Windows 95 codes are easily accessible online, can be replicated
fairly easily and aren't really useful anymore in your day-to-day life (hell, i reckon
they've never really been more than an hassle even back in the day!)
