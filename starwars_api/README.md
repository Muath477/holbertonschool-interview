# Star Wars API

Print every character of a Star Wars movie using the Star Wars API.

## Files

| File | Description |
| --- | --- |
| `0-starwars_characters.js` | Takes a movie ID, gets the film from `/films/<id>/`, then fetches each character URL with `request` and prints the names in the same order as the film's `characters` list |

## Requirements

- Ubuntu 14.04 LTS, Node 10
- First line of every file: `#!/usr/bin/node`
- Code style checked with `semistandard`
- The `request` module (`npm install request --global` and `export NODE_PATH=/usr/lib/node_modules`)

## Example

```
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
...
Bib Fortuna
```
