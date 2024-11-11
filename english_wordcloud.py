
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
import string

def process_text(text):
    comment_words = ''
    stopwords = set(STOPWORDS)


    translator = str.maketrans('  ','  ', string.punctuation)
    text = text.translate(translator)
    tokens = text.split()

    tokens = [token.lower() for token in tokens if token.lower() not in stopwords]

    comment_words += " ".join(tokens) + " "

    return tokens, comment_words


text_input = """The Bhagavad Gita, also referred to as Gita is a Hindu scripture comprising of 700 verses.
 Gita is a conversation between Lord Shri Krishna and Pandava prince Arjuna during the onset of Mahabharata war.
  Lord Krishna takes upon himself to respond to the ethical confusion shown by Arjuna due to the debacle with his cousins, and informs Prince Arjuna of his mandates
 and roles as a prince and fighter, elaborating on the teachings by Samkhya, Karma Yoga, Yoga, Moksha, and Inana Yoga, which are so evident in the Bhagavad Gita."""

tokens,comment_words = process_text(text_input)

wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=STOPWORDS,regexp = r"[a-zA-Z0-9\u0900-\u097F\u0900-\u097F\u0980-\u09FF]+",min_font_size=10).generate(comment_words)


plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

word_counts = Counter(tokens)

sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

for word, count in sorted_word_counts.items():
    print(f"{word}: {count}")