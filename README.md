# Tokyo Night Islands

Tokyo Night for JetBrains IDEs, built as child themes of the bundled
Islands Dark theme. The plugin inherits the current platform look
(rounded islands, spacing, component styling) from Islands Dark and
applies the Tokyo Night palette on top. It ships three variants, each
with a matching editor color scheme:

- Tokyo Night: the classic Night palette.
- Tokyo Night Storm: the same accents on lighter blue-grey backgrounds.
- Tokyo Night Moon: folke's Moon palette with its own accent set.

Requires a JetBrains IDE 2025.3 or later. I personally use and test it in GoLand and JetBrains 2026.2.

## Build

```
./gradlew buildPlugin
```

The installable zip lands in `build/distributions/`. Install it via
Settings > Plugins > gear icon > Install Plugin from Disk, then select
the "Tokyo Night" theme under Settings > Appearance & Behavior >
Appearance.

## Test

```
./gradlew runIde
```

This starts a sandboxed IntelliJ IDEA Community with the plugin
installed.

## Design notes

- The theme sets `parentTheme: Islands Dark` and overrides only colors.
  JetBrains maintains the structural styling in the parent, which keeps
  this theme working across platform updates.
- Window frame, main toolbar, and status bar use `#101014`, darker than
  the island background `#1a1b26`. The contrast ratio is about 1.11:1,
  below the 1.20:1 that the Islands guidelines suggest. Reaching 1.20:1
  against the canonical Tokyo Night editor background needs a near-black
  frame; the current value trades guideline compliance for palette
  fidelity.
- The editor scheme relies on `DEFAULT_*` attribute inheritance for
  language-specific keys. Go-specific attributes get tuned after a
  visual pass in GoLand.

## Credits

Colors are based on [Tokyo Night by
enkia](https://github.com/enkia/tokyo-night-vscode-theme) and the
[tokyonight.nvim palette by
folke](https://github.com/folke/tokyonight.nvim).
