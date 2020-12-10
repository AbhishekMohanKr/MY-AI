#All rights are reserved by llAKDll
#You can folow me on GitHub by https://github.com/llAKDll
#You can folow me on SoloLearn by https://www.sololearn.com/Profile/12053438
import wikipedia
import wolframalpha
from googlesearch import search
import webbrowser

def websearch() :
    try:
        fun=input(print("on what would you like to search\n1:wikipedia\n2:google\n3:open youtube"))
        if fun=='wikipedia':
            ques=input(print('enter what would you like to search'))
            results = wikipedia.summary(ques, sentences=2)
        elif fun=='google':
            ques=input(print('enter what would you like to search'))
            for j in search(ques, tld="co.in", num=1, stop=1, pause=2): 
               webbrowser.open(j)
        elif fun=='open youtube':
            webbrowser.open("youtube.com")
    except:
        print("low internet connection")
def calculation():
    try:
        question = input('write problem ')
        app_id = 'LTHYV6-HKR9WV3HEG'
        client = wolframalpha.Client(app_id)
        res = client.query(question) 
        answer = next(res.results).text 
        print(answer) 
    except:
        print("something went wrong")

akd=input(print("what would you like to do\n1:websearch\n2:calculation"))
if akd=='websearch':
    websearch()
elif akd=='calulation':
    calculation()
else:
    print("wrong input")
