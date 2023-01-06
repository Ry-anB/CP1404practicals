"""CP1404 Prac 10 - Wiki"""
import wikipedia

subject = input("Enter a page or search phrase: ")
while subject != "":
    try:
        page = wikipedia.page(subject, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    subject = input("Enter a page or search phrase: ")
