import pyMRAW
images, info = pyMRAW.load_video("C:\\Users\\vakilim\\Downloads\\Videos\\Videos\\w+p_2+10_50fps_20241108_103342.tif")

"""
import os
import pyMRAW

def mraw_to_tiff(input_mraw_path, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the MRAW video file
    with pyMRAW.MRAWFile(input_mraw_path) as mraw_file:
        # Retrieve the total number of frames
        total_frames = mraw_file.total_frames

        # Loop through each frame in the MRAW file
        for frame_index in range(total_frames):
            # Read the current frame
            frame = mraw_file.read_frame(frame_index)

            # Define the output filename with padding for ordering
            output_filename = os.path.join(output_folder, f"frame_{frame_index:04d}.tiff")

            # Save the frame as a TIFF file
            frame.save(output_filename, format="TIFF")
            
            print(f"Saved {output_filename}")

# Example usage
input_mraw_path = "C:\\Users\\vakilim\\Nextcloud\\Photron\20241108\\s+p_2+10_50fps_20241108_102351.mraw"
output_folder = "C:\\Users\\vakilim\\Nextcloud\\Photron\20241108"

mraw_to_tiff(input_mraw_path, output_folder)
"""