import streamlit as st
from model import *

st.header("Any songs to Lo-Fi")
x = st.file_uploader("Upload your music")


wv, sr = librosa.load(x.read(), sr=16000)  #Load waveform
print(wv.shape)
speca = prep(wv)                                                    #Waveform to Spectrogram

plt.figure(figsize=(50,1))                                          #Show Spectrogram
plt.imshow(np.flip(speca, axis=0), cmap=None)
plt.axis('off')
plt.show()

abwv = towave(speca, name='FILENAME3', path='songs_gen')           #Convert and save wav

with open("AB.wav", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="AB.wav",
            mime="image/png"
          )