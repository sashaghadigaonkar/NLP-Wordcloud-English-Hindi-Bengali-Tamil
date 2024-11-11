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


text_input = """கீதா என்றும் அழைக்கப்படும் பகவத் கீதை 700 வசனங்களைக் கொண்ட ஒரு இந்து வேதமாகும்.
மகாபாரதப் போரின் தொடக்கத்தில் ஸ்ரீ கிருஷ்ணருக்கும் பாண்டவ இளவரசன் அர்ஜுனுக்கும் இடையே நடந்த உரையாடல்தான் கீதா. """
tokens,comment_words = process_text(text_input)

wordcloud = WordCloud(font_path='/content/arialuni.ttf',width=800, height=800,
                      background_color='white',
                      stopwords=STOPWORDS,regexp = r"[\u0900-\u097F\u0980-\u09FF\u0B80-\u0BFF]+",min_font_size=10).generate(comment_words)


plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

word_counts = Counter(tokens)

sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

for word, count in sorted_word_counts.items():
    print(f"{word}: {count}")