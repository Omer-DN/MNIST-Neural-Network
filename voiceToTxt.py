import wave
import os
def convert_wav_to_txt(wav_filename, txt_filename):
    """
    פונקציה שממירה קובץ WAV לטקסט ושומרת אותו בקובץ TXT.
    wav_filename - נתיב לקובץ WAV שיש להמיר
    txt_filename - נתיב לקובץ TXT שיש ליצור ולשמור בו את הטקסט
    """
    try:
        # פתיחת קובץ WAV לקריאה
        with wave.open(wav_filename, 'rb') as wav_file:
            # קריאת מאפייני הקובץ WAV
            channels = wav_file.getnchannels()
            sample_width = wav_file.getsampwidth()
            frame_rate = wav_file.getframerate()
            num_frames = wav_file.getnframes()
            duration = num_frames / float(frame_rate)

            # קריאת נתוני הקול
            frames = wav_file.readframes(num_frames)
            # המרת נתוני הקול לטקסט
            data = frames.hex()

        # שמירת הטקסט לקובץ TXT
        with open(txt_filename, 'w') as txt_file:
            txt_file.write(f"WAV File: {wav_filename}\n")
            txt_file.write(f"Channels: {channels}\n")
            txt_file.write(f"Sample Width: {sample_width}\n")
            txt_file.write(f"Frame Rate: {frame_rate}\n")
            txt_file.write(f"Duration: {duration} seconds\n\n")
            txt_file.write("Hexadecimal Representation of Audio Data:\n")
            txt_file.write(data)

        print(f"Successfully converted {wav_filename} to {txt_filename}")

    except Exception as e:
        print(f"Failed to convert {wav_filename} to TXT: {str(e)}")


# דוגמה לשימוש של הפונקציה:
if __name__ == "__main__":
    wav_path = r'C:\\Users\\USER\\Desktop\\networks\\work\\output1.wav'  # נתיב לקובץ WAV
    txt_path = "output.txt"  # נתיב לקובץ TXT לשמירת הטקסט

    convert_wav_to_txt(wav_path, txt_path)
