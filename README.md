# UE Camera Script

A small script for controlling the Unreal Engine camera through the console.

This script offers **_a_** way to capture screenshots that can be stitched into a panorama, but there may be better solutions out there.

## Usage

This script can be used in conjunction with [Universal Unreal Engine 4 Unlocker (UUU v4)](https://opm.fransbouma.com/uuuv4.htm), and likely also works with UUU v5.

For the script to set the camera rotation you'll need the UE DebugCameraController object id, which can be found by opening the console and entering the `ToggleDebugCamera` command, then entering the `GetAll DebugCameraController` command.
This should list out all DebugCameraController objects.

NOTE: Whenever possible it is best to disable unnecessary effects, such as vignetting, inside of the engine itself, instead of attempting to compensate for them after the screenshots were taken.
For example, you could pass `r.Tonemapper.Quality 0` to completely disable tone mapping effects, such as vignetting.

### setting constants

You'll want to set/change some constants such as the game title (used to prefix the output folder name) or to indicate the key (default $) you're using to open the UE console inside of `constants.py`.

### customizing the number of captures and their angles

You may need/want to alter the `points.json` file to customize the number of screenshots and the angles at which they are taken,
but you must adhere to the following format:

```json
[
  { "theta": 0, "phi": -90 },
  { "theta": 0, "phi": -60 },
  { "theta": 90, "phi": -60 }
]
```

### useful console commands

| command | description |
| :- | :- |
| `ToggleDebugCamera`| Toggles the debug camera, allowing you to move around freely |
| `GetAll DebugCameraController`| Returns a list of all DebugCameraController objects |
| `fov`| Sets FOV |
| `r.Tonemapper.Quality`| Sets all tone mapping effects, such as vignetting |

