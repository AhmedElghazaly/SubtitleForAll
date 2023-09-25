import argostranslate.translate
import time


from_lang = "en"
#to_lang = "ar"

subs = []

# Function to translate a subtitle
def translate_subtitle(subtitle_text, to_lang ='ar'):
    translation = argostranslate.translate.translate(subtitle_text, from_lang, to_lang)
    return translation


#handle suptitle file add all contents in subs[[index,time,text],[],...]
def srt_handling(input_file):
    with open(input_file, "r") as file:
        all_lines = file.readlines()
        sub =[]
        n = 0
        for line in all_lines:
            n += 1
            if n == 4:
                subs.append(sub)
                sub = []
                n = 0
            # elif n == 3:
            #     sub.append(line)
            #     subs.append(sub)
            #     sub = []
            else:
                sub.append(line)

    file.close()
    print("translation is begining...")
    for pre_sub in subs:
        post_sub = pre_sub[2].split("\n")[0]
        pre_sub[2] = translate_subtitle(post_sub, "ar") +"\n"
        print(pre_sub[2])

def generat_srt():
    print("generating srt file...")
    with open("[elg]subtitle_ar.srt","w",encoding="utf-8") as file:
        for sub in subs:
            for line in sub:
                file.write(line)
            file.write("\n")
    file.close()

def main(input_file):
    srt_handling(input_file)
    generat_srt()

stime = time.time()
main("ElgSubtitle.srt")
etime = time.time()

print(etime-stime)


  
