### vreddit-dl

Downloads v.reddit.com videos as mp4s.

`vdl` file is an executable Python 2 script that can be copied right into your path.

**Note**: `vdl` downloads to the current directory by default, whereas `vdl.py` creates an `./out/` directory and downloads there.

### Dependencies

```
beautifulsoup4==4.6.3
youtube-dl==2018.11.23
```

(actual version is not a big deal, it only uses basic functionality)

Requirements can also be found in `requirement.txt`.

## Usage

`vdl <url>`

`<url>` can be either a link to a Reddit post or a .mpd link.

For example,

`vdl httpshttps://old.reddit.com/r/Animemes/comments/8v27fc/`
