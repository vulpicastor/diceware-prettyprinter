# diceware-prettyprinter

Pretty prints the EFF random passphrase word lists

## Usage

First, get the EFF word lists:

```
$ curl -O "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt" \
       -O "https://www.eff.org/files/2016/09/08/eff_short_wordlist_1.txt" \
       -O "https://www.eff.org/files/2016/09/08/eff_short_wordlist_2_0.txt"
```

Then, perform the conversion:

```
$ for f in eff_*.txt; do ./diceware-prettyprinter.py "$f" > "pretty-$f"; done
```

Finally, feed into your favorite printer:

```
$ for f in pretty-eff_*.txt; do lpr -P FavPrinter -o sides=two-sided-long-edge "$f"; done
```

Voila! Now you have paper-based word lists for random password generation.
