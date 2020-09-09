from import_data import create_spectrogram
from slice_spectrogram import slice_spect


# train mp3 to train Mel spectrogram
create_spectrogram(verbose=1, mode="Train")
# train Mel spectrogram to train slice spectrogram
slice_spect(verbose=1, mode="Train")
# test mp3 to test Mel spectrogram
create_spectrogram(verbose=1, mode="Test")
# test Mel spectrogram to test slice spectrogram
slice_spect(verbose=1, mode="Test")
