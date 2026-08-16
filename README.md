# GalaxySgram

Samsung videos look amazing on your phone, but turn into blurry, stuttering garbage when uploaded to Instagram? Meta's compression algorithm is aggressive. This script fixes it.

## What's the problem?

Samsung phones record video with variable frame rates, proprietary HDR metadata, and huge bitrates. When you upload raw files directly, Instagram's servers get confused and smash your video quality to pieces.

## What does this do?

- **Strips useless Samsung metadata** so Meta's encoder doesn't freak out.
- **Forces BT.709 color profile** so your video colors don't look washed out.
- **Locks frame rate to constant 60 FPS** to eliminate playback stutter.
- **Caps bitrate at 11–12 Mbps** (the exact sweet spot Instagram likes).

No corporate bloat, no ads, no fancy GUI—just a straightforward Python script using FFmpeg.

## Prerequisites

1. **Python 3.8+**
2. **FFmpeg** installed on your system:
   - **Windows:** `winget install Gyan.FFmpeg`
   - **macOS:** `brew install ffmpeg`
   - **Linux:** `sudo apt install ffmpeg`

## How to use

1. Clone & install dependencies:
   ```bash
   git clone [https://github.com/your-username/galaxysgram.git](https://github.com/your-username/galaxysgram.git)
   cd galaxysgram
   pip install -r requirements.txt

   Run the script: python app.py -i my_samsung_video.mp4 -o ig_ready.mp4


Done. Upload ig_ready.mp4 to Instagram without it looking like it was filmed on a potato.

### LICENSE

Distributed under the WTFPL (Do What The Fuck You Want To Public License). See LICENSE for details.
