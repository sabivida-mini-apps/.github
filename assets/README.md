# Assets

The organisation's avatar, profile banner and the repositories' social previews.

All of them are made from SabiVida's approved mark (`src/mark-source.png`). The mark is used as it is: never redrawn, only recoloured white. They share the brand blue `#003893` with yellow `#F7D116` accents. Text is set in Manrope. The yellow bar and the app-tile grid mark this as SabiVida's developer side, distinct from the main SabiVida profile.

| File | Use |
| --- | --- |
| `avatar.png` / `avatar.svg` | Organisation profile picture (1024 × 1024) |
| `banner.png` / `banner.svg` | Top of the organisation profile |
| `social-<repository>.png` / `.svg` | Each repository's social preview (1280 × 640) and README header |

To regenerate the images, run `src/build.py` from `src/`. You need Python 3, HarfBuzz's `hb-view`, `rsvg-convert` and Manrope (`MANROPE_TTF=/path/to/Manrope.ttf`). Text is drawn as HarfBuzz outlines, so the output doesn't depend on the system's installed fonts.
