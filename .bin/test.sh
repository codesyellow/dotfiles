while true; do
  # Detect if YouTube Music is running
  if wmctrl -l | grep -q "youtube-music"; then
    # Apply your music preset
    set_easyeffects_preset "$EASY_EFFECTS_PRESET"
    echo "YouTube Music detected - Applying music preset."

    # Wait until YouTube Music closes
    while wmctrl -l | grep -q "$YOUTUBE_MUSIC_WINDOW_CLASS"; do
      sleep 1
    done
  fi

  # Apply the Loudness Equalizer preset
  set_easyeffects_preset "$LOUDNESS_PRESET"
  echo "YouTube Music closed - Applying Loudness Equalizer."
  sleep 1
done
