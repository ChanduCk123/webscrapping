"""webscrapping using BeautifulSoup module-
   it is the process of extracting some data from a website programmatically.
   in this access some data(top rated movies data) from imdb website and it is stored into excel file
here 1st we install Request&BeautifulSoup module
"""

from bs4 import BeautifulSoup
import requests,openpyxl #used to access data from particular website

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Top Rated Movies"
sheet.append(["Movies Rank","Movie Name","Year of Release","IMDB Rating"])
try:
    source = requests.get("https://www.imdb.com/chart/top/")
    #it is going to access this website & it is going to return response obj & that response obj stored in the source
    source.raise_for_status() #it checks whether the url is valid or not.

    soup = BeautifulSoup(source.text,"html.parser")#html text/content of the response obj/website..parser is default par,it comes along with python 	installation
    #the var soup has stored html content of entire website&we dont want all these info.we want only movie details
    
    movies = soup.find("tbody",class_="lister-list").find_all("tr") #return total movies interms of List
    for movie in movies:
        name = movie.find("td",class_="titleColumn").a.text    #return inside 'a' tag in the form of text        
        rank = movie.find("td",class_="titleColumn").get_text(strip=True).split(".")[0]   #return text of the within td tag
        year = movie.find("td",class_="titleColumn").span.text.strip("()")
        rating = movie.find("td",class_="ratingColumn imdbRating").strong.text
        print(rank,name,year,rating)
        sheet.append([rank,name,year,rating])
except Exception as e:
    print(e)
excel.save("imdb movie ratings.xlsx")
