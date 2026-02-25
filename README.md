# fcp-marker-trimmer
Removes Markers placed outside asset-clip range for performance optimization on larger Projects.

Each time you execute Blade on a clip, FCP copies all Marker-related information to the new Clip. That's why it gets exponentially slow when there are (many) Markers already placed on your big Project clips and user executes Blade actions. For example, when removing silent parts of your video.

This package solves such technical problem.
