from textblob import TextBlob

text = input("Enter the text: ")
corrected_text = TextBlob(text).correct()
print("Corrected text:", corrected_text)
#sentiment of the text 
print("Sentiment:", corrected_text.sentiment)