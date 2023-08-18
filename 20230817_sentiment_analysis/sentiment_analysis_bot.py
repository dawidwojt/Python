from textblob import TextBlob
from dataclasses import dataclass
from time import sleep

@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, levelone: float, leveltwo: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity

    amazing_threshold: float = leveltwo
    friendly_threshold: float = levelone
    negative_threshold: float = -levelone
    bad_threshold: float = -leveltwo

    if polarity >= amazing_threshold:
        return Mood('😍', polarity)
    elif polarity >= friendly_threshold:
        return Mood('😀', polarity)
    elif polarity <= negative_threshold:
        return Mood('😒', polarity)
    elif polarity <= bad_threshold:
        return Mood('😭', polarity)
    else:
        return Mood('😐', polarity)


def run_analysis():
    print('This is a sentiment analysis bot, it will jugde how positive/negative your sentiment is \n'
          'scale: \n'
          '     -100%    - the most negative\n'
          '     0%       - neutral\n'
          '     100%     - the most positive\n')
    sleep(2)
    print('Enter your sentiment:  ')
    user_input: str = input('You:  ')
    sleep(0.5)
    print('One moment...')
    sleep(2)
    mood: Mood = get_mood(user_input, levelone=0.25, leveltwo=0.75)
    print(f"Bot thinks: {mood.emoji} {mood.sentiment*100}% {mood.emoji}")

if __name__ == '__main__':
    run_analysis()