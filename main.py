# @K4isszDev - @K4issz.luv on instagram
import time
import sys

def play():
    lyrics = {
        0: {'text': "Paavamadi en nenju ", 'speed': 0.07, 'gap_after': 1.5},
        1: {'text': "chinna erumbaachu", 'speed': 0.07, 'gap_after': 1.5},
        2: {'text': "\nKaala vecchu en kaala ", 'speed': 0.07, 'gap_after': 1.0},
        3: {'text': "mela yeri pochu", 'speed': 0.07, 'gap_after': 1.0},
        4: {'text': "\nNaalaam inge yaaradi ", 'speed': 0.08, 'gap_after': 1.5},
        5: {'text': "needhaan motham paaradi", 'speed': 0.07, 'gap_after': 1.0},
        6: {'text': "\nKaadhal vera yedhadi ", 'speed': 0.07, 'gap_after': 1.0},
        7: {'text': "nee naa mattum dhaanadi", 'speed': 0.07, 'gap_after': 1.0},
        8: {'text': "\nVandarkodi en Vannakilli", 'speed': 0.1, 'gap_after': 0.1},
        9: {'text': "\nEn ullara unnala kaayam", 'speed': 0.1, 'gap_after': 0.6},
        10: {'text': "\nVazhi kandenadi uyir kondenadi", 'speed': 0.07, 'gap_after': 0.5},
        11: {'text': "\nEn anbaana koodu neeyum", 'speed': 0.07, 'gap_after': 0.5},
        12: {'text': "\nNamma serndhu thotta poomaram", 'speed': 0.1, 'gap_after': 0.1},
        13: {'text': "\nMalar malaraa pozhiyum <3 @K4issz.luv", 'speed': 0.07, 'gap_after': None} 
    }

    print('🎧 Now Playing: "Kannadi Poove" - Santhosh Narayanan (2025)')
    time.sleep(1.0)
    for x in range(len(lyrics)):
        line_data = lyrics[x]
        text = line_data['text']
        speed = line_data.get('speed')
        gap_after = line_data.get('gap_after')
        
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)

        if gap_after is not None:
            time.sleep(gap_after)

play()
