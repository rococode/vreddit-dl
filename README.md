## vreddit-dl

Downloads v.redd.it videos as mp4s.

`vdl` file is an executable Python 2 script that can be copied right into your path.

**Note**: `vdl` downloads to the current directory by default, whereas `vdl.py` creates an `./out/` directory and downloads there.

**Note 2**: Actual v.redd.it URLs don't work too well because it should be easier to just link the post itself. If for some reason you find yourself having v.redd.it URLs more easily accessible than the post URL, open an issue and I can make it work.

### Dependencies

```
beautifulsoup4==4.6.3
youtube-dl==2018.11.23
```

(actual version is not a big deal, it only uses basic functionality)

Requirements can also be found in `requirements.txt`.

### Usage

`vdl <url>`

`<url>` can be either a link to a Reddit post or a .mpd link.

For example,

`vdl https://old.reddit.com/r/Animemes/comments/8v27fc/`
