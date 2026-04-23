from langdetect import detect

text = input("Enter the text: ")

language = detect(text)

print("Detected Language:", language)