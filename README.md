# Camera Latency

In one terminal window, run the time display loooping script:  
`python time_loop.py`

In a separate window, SSH to the camera or compute resource and run the Canopy Deepstream application with log statements showing in the console.

While recording a TV screen in slow motion, run `display_image.py` to have an image show on the screen.

View the recorded slow-motion video to see the timestamp when the image first appears and compare to the timestamp when the Canopy Deepstream logs output the first detection.