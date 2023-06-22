import time

def run_timer():
    start_time = time.time()

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        minutes = int(elapsed_time / 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time * 1000) % 1000)

        timer_text = f"{minutes:02d}:{seconds:02d}:{milliseconds:03d}"
        print(timer_text, end="\r", flush=True)

        time.sleep(0.01)  # Adjust the delay if needed

run_timer()
