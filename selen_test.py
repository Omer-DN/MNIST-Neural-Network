import pyaudio
import wave
import os


def get_next_filename(base_name, extension):
    """
    הפונקציה מחפשת שם קובץ עוקב פנוי.
    base_name - שם הבסיס של הקובץ
    extension - סיומת הקובץ
    """
    i = 1
    filename = f"{base_name}{i}.{extension}"
    while os.path.exists(filename):
        i += 1
        filename = f"{base_name}{i}.{extension}"
    return filename


def record_audio(output_filename, record_seconds=5, sample_rate=44100, chunk_size=1024):
    """
    הפונקציה מקליטה קול ושומרת אותו לקובץ WAV.
    output_filename - שם הקובץ לשמירה
    record_seconds - זמן ההקלטה בשניות
    sample_rate - קצב הדגימה
    chunk_size - גודל החבילה
    """
    format = pyaudio.paInt16  # פורמט הקלטה
    channels = 2  # ערוצים (סטריאו)

    audio = pyaudio.PyAudio()

    # פתיחת זרם להקלטה
    stream = audio.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk_size)

    print("Recording...")  # הודעה על התחלת ההקלטה

    frames = []

    # הקלטה בלולאה למשך זמן ההקלטה
    for _ in range(0, int(sample_rate / chunk_size * record_seconds)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("Finished recording")  # הודעה על סיום ההקלטה

    # עצירת הזרם וסגירתו
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # שמירת ההקלטה לקובץ WAV
    wave_file = wave.open(output_filename, 'wb')
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(audio.get_sample_size(format))
    wave_file.setframerate(sample_rate)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()


if __name__ == "__main__":
    base_name = "output"
    wav_extension = "wav"

    # קבלת שם הקובץ הבא הזמין בפורמט WAV
    wav_filename = get_next_filename(base_name, wav_extension)

    record_seconds = 5  # זמן ההקלטה בשניות
    # קריאה לפונקציה להקלטת קול
    record_audio(wav_filename, record_seconds)

    print(f"Recorded and saved as {wav_filename}")
