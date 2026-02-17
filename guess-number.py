"""
Guess Number Game By While Loop
"""
import random

def start_game():
    secret = random.randint(1, 100)
    attempts = 0

    print("🎯 بازی حدس عدد شروع شد!")
    print("یک عدد بین 1 تا 100 حدس بزن.")

    while True:
        guess = input("حدس شما: ")

        if not guess.isdigit():
            print("⚠️ لطفا فقط عدد وارد کن")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("📉 عدد بزرگ‌تره")
        elif guess > secret:
            print("📈 عدد کوچک‌تره")
        else:
            print(f"✅ درست حدس زدی! عدد {secret} بود")
            print(f"تعداد تلاش: {attempts}")
            break


if __name__ == "__main__":
    start_game()