#grafiskā saskarne
import tkinter as tk
from tkinter import ttk


from selenium import webdriver 
from selenium.webdriver.common.by import By # izmantoju, lai atrastu mājaslapas elementa atrašanās vietu
from selenium.webdriver.support.ui import WebDriverWait # izmantoju, lai programma gaida līdz ielādējas mājas lapa, pretējā gadījumā, pēc 20 sekundēm aizvērsies
from selenium.webdriver.support import expected_conditions as EC 
# EC nepieciešams, lai programma turpinātos tad, kad izpildās nosacījums
# (programma sagaidīs, līdz var atrast mājaslapā pareizo logu, pēc tam aizvērsies, citādi tā turpinātu gaidīt visu iestatīto laiku)

def scrape_movie_information(url):
    driver = webdriver.Chrome()  # iestatu Google Chrome draiveri
    driver.get(url)

    movie_list = [] #saraksts, kurā tiks ielikts filmu info

    try:
        # vispirms atrod to mājaslapas daļu (konteineri), kas satur filmu logus
        container = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="article-ajax-content-2958"]'))
        )

        # šis norāda, kā atrast filmas logus (kāds ir viņu ceļs pēc xpath)
        movie_elements = container.find_elements(By.XPATH, './/div[@class="schedule-card schedule__item schedule-card--label schedule-card--top-label"]')

        for movie_element in movie_elements: #cikls, kurš iziet cauri filmas logu, atlasot visu informāciju, kuru vēlos attēlot
            movie_name = movie_element.find_element(By.XPATH, './/p[@class="schedule-card__title bold"]').text
            start_time = movie_element.find_element(By.XPATH, './/time[@class="schedule-card__time bold"]').text
            language = movie_element.find_element(By.XPATH, './/p[@class="schedule-card__option-title bold h-hidden-xs h-hidden-sm h-hidden-md"]').text
            seats_available = movie_element.find_element(By.XPATH, './/p[@class="schedule-card__option-title bold"]').text
            hall_number = movie_element.find_element(By.XPATH, './/p[@class="schedule-card__hall bold"]').text

            # saglabāju iegūto informāciju par katru filmu sarakstā
            movie_list.append({
                "Filmas nosaukums": movie_name,
                "Sākuma laiks": start_time,
                "Valoda": language,
                "Brīvas sēdvietas": seats_available,
                "Zāles numurs": hall_number
            })

    finally: # aizver pārlūku
        driver.quit()

    return movie_list

def show_movies_by_time_interval(start_time, end_time): # šī funkcija ļauj izvēlēties laika intervālu, kurā lietotājs gatavs ierasties uz filmu
    selected_movies = [movie for movie in all_movies if start_time <= movie["Sākuma laiks"] <= end_time] #

    # parāda filmas sākumu un beigu laiku
    root = tk.Tk()
    root.title(f'Filmas - Laika intervāls: {start_time} līdz {end_time}')

    # parāda filmas atsevišķā teksta logā
    text_widget = tk.Text(root, wrap=tk.WORD, width=50, height=20)
    text_widget.pack()

    for movie in selected_movies:
        text_widget.insert(tk.END, f"Filmas nosaukums: {movie['Filmas nosaukums']}\n")
        text_widget.insert(tk.END, f"Sākuma laiks: {movie['Sākuma laiks']}\n")
        text_widget.insert(tk.END, f"Valoda: {movie['Valoda']}\n")
        text_widget.insert(tk.END, f"Brīvas sēdvietas: {movie['Pieejamie sēdvietas']}\n")
        text_widget.insert(tk.END, f"Zāles numurs: {movie['Zāles numurs']}\n")
        text_widget.insert(tk.END, "-"*30 + "\n")

    root.mainloop()

# mājaslapa, kuru vērs vaļā selenium
website_url = 'https://www.apollokino.lv/schedule'
all_movies = scrape_movie_information(website_url)

# sakārtots saraksts, ar viesiem filmu sākuma laikiem
all_start_times = sorted(set(movie["Sākuma laiks"] for movie in all_movies))

# izveido grafisko saskarni
root = tk.Tk()
root.geometry("500x200")
root.title("Apollo kino")

selected_start_time = tk.StringVar()
selected_start_time.set(all_start_times[0])  # noklusējuma sākuma laiks

selected_end_time = tk.StringVar()
selected_end_time.set(all_start_times[-1])  # noklusējuma beigu laiks

# drop-down logs, kurā izvēlēties, sākumu laika periodam, kurā vēlētos apmeklēt kinoteātri
start_time_dropdown = ttk.Combobox(root, textvariable=selected_start_time, values=all_start_times, width=20)
start_time_dropdown.pack(pady=10)

# vēl viens logs, šoreiz lai izvēlētos vēlāko ierašanās brīdi
end_time_dropdown = ttk.Combobox(root, textvariable=selected_end_time, values=all_start_times, width=20)
end_time_dropdown.pack(pady=10)

# nospiežot šo pogu, tiks parādītas visas filmas, kuras sākas izvēlētajā laika periodā
show_movies_button = tk.Button(root, text="Rādīt filmas", command=lambda: show_movies_by_time_interval(selected_start_time.get(), selected_end_time.get()))
show_movies_button.pack(pady=10)

root.mainloop()