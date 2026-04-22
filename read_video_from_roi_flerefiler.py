"""
Read the input video file, display first frame and ask the user to select a
region of interest.  Will then calculate the mean of each frame within the ROI,
and return the means of each frame, for each color channel, which is written to
file.
"""
import cv2
import numpy as np
import os

# -------------------------------------------------------
# ENDRE DISSE: legg til så mange videofiler du vil
VIDEO_MAPPE = r'C:\Users\lisa\Desktop\6. semester\Sensorer og Instrumetering\Lab\Lab3\kode\data'

VIDEOFILER = [
    #'finger_t_5.mp4',
    'finger_t_63BMP.mp4',
    # 'finger_test2.mp4',  # legg til flere her
    # 'finger_test3.mp4',
]
# -------------------------------------------------------

def prosesser_video(filename, output_filename):
    cap = cv2.VideoCapture(filename, cv2.CAP_FFMPEG)
    if not cap.isOpened():
        print(f"Kunne ikke åpne: {filename}")
        return

    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    mean_signal = np.zeros((num_frames, 3))

    count = 0
    ROI = None
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count == 0:
            window_text = f'{os.path.basename(filename)} - Velg ROI og trykk SPACE eller ENTER'
            ROI = cv2.selectROI(window_text, frame)
            cv2.destroyWindow(window_text)
            print(f"Prosesserer {filename}...")

        cropped_frame = frame[ROI[1]:ROI[1] + ROI[3], ROI[0]:ROI[0] + ROI[2], :]
        mean_signal[count, :] = np.mean(cropped_frame, axis=(0, 1))
        count += 1

    cap.release()
    np.savetxt(output_filename, np.flip(mean_signal, 1))
    print(f"Data lagret til '{output_filename}', fps = {fps}")


# Kjør gjennom alle videofiler
for videofil in VIDEOFILER:
    input_path = os.path.join(VIDEO_MAPPE, videofil)
    output_path = os.path.join(VIDEO_MAPPE, videofil.replace('.mp4', '_data.txt'))
    print(f"\n--- Starter: {videofil} ---")
    prosesser_video(input_path, output_path)

print("\nFerdig med alle filer!")
