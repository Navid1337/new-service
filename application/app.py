from flask import Flask, render_template, request
from application import func
from datetime import datetime, timedelta                    # Används för att hämta dagens datum


app = Flask(__name__)


# Båda endpoints tar oss till samma funktion
@app.route("/")
@app.route("/home")
def home():
    return render_template("homepage.html")


# Formulär
@app.route("/form")
def form():
    today = datetime.now().date()                               # Vi hämtar dagens datum
    tomorrow = today + timedelta(days=1)                        # Vi lägger till 1 dag
    return render_template("form.html", tomorrow=tomorrow)      # Skickar morgondagens datum till till form.html med jinja2


# Formulärets svarssida - alltså hit action="/results" skickar oss.
@app.route("/results", methods=["POST"])                  
def results():
    try: 
        price_class = request.form.get("price_class")           # Hämtar det inmatade värdet för prisklass.
        date = request.form.get("date")                         # Hämtar värdet från date-input-formuläret.
        year, month, day = date.split("-")                      # Delar upp datumsträngen i år, månad och dag
        
        url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json"
        
        df = func.api_url_to_pandas_dataframe(url)              # Konverterar API-data till en pandas-tabell.
        func.slicing_iso_8601(df, "time_start", "Starttid")     # Bearbetar tiderna i iso-8601 till hh:mm som efterfrågat.
        func.slicing_iso_8601(df, "time_end", "Sluttid")
        df_html = df.to_html()                                  # Gör om pandas tabellen till html-kod.

        return render_template("results.html",                  # Skickar pandas-tabellen och användarens val i formuläret till results.html.
                            df_html=df_html,
                            price_class=price_class,
                            date=date,
                           day=day)
    except Exception:                                           # Om man försöker nå morgondagens elpriser innan de har blivit uppdaterade.
        return render_template("404.html")             
        


# Servern kan inte hitta resursen.
@app.errorhandler(404)                                      # Tack Dennis! 
def not_found(e):
    return render_template("404.html")

