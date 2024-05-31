from moviepy.editor import VideoFileClip

def convert_mp4_to_avi(input_path, output_path):
    # Load the video file
    clip = VideoFileClip(input_path)
    
    # Write the video file in AVI format
    clip.write_videofile(output_path, codec='mjpeg')

# Example usage
input_path = "C:\\Users\\vakilim\\Downloads\\a7.mp4"
output_path = "C:\\Users\\vakilim\\Downloads\\a7_edited.avi"
convert_mp4_to_avi(input_path, output_path)


"""
import ffmpeg

def convert_mp4_to_avi(input_file, output_file):
    try:
        # Run ffmpeg command to convert mp4 to avi without compression
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec='copy', acodec='copy')  # 'copy' codec means no re-encoding
            .run(overwrite_output=True)
        )
        print(f"Conversion successful: {input_file} to {output_file}")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode()}")

# Example usage
input_mp4 = "C:\\Users\\vakilim\\Downloads\\a7.mp4"
output_avi = "C:\\Users\\vakilim\\Downloads\\a7_edited.avi"
convert_mp4_to_avi(input_mp4, output_avi)
"""