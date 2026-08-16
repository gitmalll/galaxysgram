import argparse
import logging
from pathlib import Path
import sys
import ffmpeg

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)


class GalaxyVideoTranscoder:

    def __init__(self, target_bitrate: str = "11M", max_bitrate: str = "12M"):
        self.target_bitrate = target_bitrate
        self.max_bitrate = max_bitrate

    def process_video(self, input_path: str, output_path: str) -> bool:
        """Remove metadata, fix the color space, and encode the video for Instagram."""
        input_file = Path(input_path)
        output_file = Path(output_path)

        if not input_file.exists():
            logging.error(f"Input file doesnt exist: {input_path}")
            return False

        logging.info(f"Processing {input_file.name}")
        logging.info("Cleaning metadata and fixing color profile...")

        try:
            (
                ffmpeg.input(str(input_file))
                .output(
                    str(output_file),
                    # Codec & Frame Rate Configuration
                    vcodec="libx264",
                    r=60,  # Enforce Constant Frame Rate (CFR)
                    # Color Space Normalization
                    pix_fmt="yuv420p",
                    color_primaries="bt709",
                    color_trc="bt709",
                    colorspace="bt709",
                    # Bitrate Control
                    video_bitrate=self.target_bitrate,
                    maxrate=self.max_bitrate,
                    bufsize="16M",
                    # Metadata Extraction Prevention
                    map_metadata=-1,
                    # Audio Configuration
                    acodec="aac",
                    audio_bitrate="128k",
                )
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
            )

            logging.info(
                f"Processing completed. Output saved to: {output_file.name}"
            )
            return True

        except ffmpeg.Error as e:
            logging.error(
                "FFmpeg execution failed due to an encoding error."
            )
            stderr_output = (
                e.stderr.decode("utf-8") if e.stderr else "No stderr logs."
            )
            logging.debug(f"FFmpeg Stderr: {stderr_output}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description="GalaxySgram: Professional CLI Video Transcoder for Instagram Optimization."
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Path to input video file"
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Path to output video file"
    )

    args = parser.parse_args()

    transcoder = GalaxyVideoTranscoder()
    success = transcoder.process_video(args.input, args.output)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()