# Andson Li (mostly)
# Daniel Min

# THIS MAKES WAV FILES
# DONT RUN THIS WITH YOUR ACTUAL CODE
from pydub import AudioSegment
import random
import simpleaudio

SECONDS = random.randint(5, 8)

# SONG1 MIXED WITH SONG2
# SONG3 MIXED WITH SONG4
BASE = './wav/'
SONG1 = BASE + 'centimeter.wav'
SONG2 = BASE + 'gurenge.wav'
SONG3 = BASE + 'centimeter.wav'
SONG4 = BASE + 'above.wav'

old1 = AudioSegment.from_wav(SONG1)
old2 = AudioSegment.from_wav(SONG2)
for i in range(1, 177):
    t1 = (i-1) * 1000 #Works in milliseconds
    t2 = (i+(SECONDS-1)) * 1000
    newAudio1 = old1[t1:t2]
    newAudio2 = old2[t1:t2]
    newAudio1.export(f'M{i}.wav', format="wav")
    newAudio2.export(f'Q{i}.wav', format="wav")

old1 = AudioSegment.from_wav(SONG3)
old2 = AudioSegment.from_wav(SONG4)
for i in range(1, 177):
    t1 = (i-1) * 1000 #Works in milliseconds
    t2 = (i+(SECONDS-1)) * 1000
    newAudio1 = old1[t1:t2]
    newAudio2 = old2[t1:t2]
    newAudio1.export(f'T{i}.wav', format="wav")
    newAudio2.export(f'R{i}.wav', format="wav")

for i in range(1, 177):
    old1 = AudioSegment.from_file(f'M{i}.wav', format='wav')
    old2 = AudioSegment.from_file(f'Q{i}.wav', format='wav')
    mixed = old1.overlay(old2)
    mixed.export(f'M{i}.wav', format='wav')

for i in range(1, 177):
    old1 = AudioSegment.from_file(f'T{i}.wav', format='wav')
    old2 = AudioSegment.from_file(f'R{i}.wav', format='wav')
    mixed = old1.overlay(old2)
    mixed.export(f'T{i}.wav', format='wav')


# Each of these lists corresponds to one column of the table used for the minuet
# portion Mozart's Musical Dice Game. The first two elements are set to None
# because, there is no way for a roll of two dice to return a 0 or a 1. Only the
# indices that can be the result of the roll of two dice have a value.
# Each value is the number labelling a possible musical choice for that measure.
mm01 = [None, None, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
mm02 = [None, None, '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
mm03 = [None, None, "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"]
mm04 = [None, None, "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44"]
mm05 = [None, None, "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55"]
mm06 = [None, None, "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66"]
mm07 = [None, None, "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77"]
mm08 = [None, None, "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88"]
mm09 = [None, None, "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
mm10 = [None, None, "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110"]
mm11 = [None, None, "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121"]
mm12 = [None, None, "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132"]
mm13 = [None, None, "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143"]
mm14 = [None, None, "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154"]
mm15 = [None, None, "155", "156", "157", "158", "159", "160", "161", "162", "163", "164", "165"]
mm16 = [None, None, "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176"]

# This table contains all of the columns of the minuet portion of Mozart's
# Musical Dice Game in order.
minuet_table = [mm01, mm02, mm03, mm04, mm05, mm06, mm07, mm08,
            mm09, mm10, mm11, mm12, mm13, mm14, mm15, mm16]

# Each of these lists corresponds to one column of the table used for the trio
# portion Mozart's Musical Dice Game. The first two elements are set to None
# because, there is no way for a roll of two dice to return a 0 or a 1. Only the
# indices that can be the result of the roll of one die have a value.
# Each value is the number labelling a possible musical choice for that measure.
tm01 = [None, None, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
tm02 = [None, None, '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
tm03 = [None, None, "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"]
tm04 = [None, None, "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44"]
tm05 = [None, None, "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55"]
tm06 = [None, None, "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66"]
tm07 = [None, None, "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77"]
tm08 = [None, None, "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88"]
tm09 = [None, None, "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
tm10 = [None, None, "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110"]
tm11 = [None, None, "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121"]
tm12 = [None, None, "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132"]
tm13 = [None, None, "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143"]
tm14 = [None, None, "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154"]
tm15 = [None, None, "155", "156", "157", "158", "159", "160", "161", "162", "163", "164", "165"]
tm16 = [None, None, "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176"]

trio_table = [tm01, tm02, tm03, tm04, tm05, tm06, tm07, tm08,
              tm09, tm10, tm11, tm12, tm13, tm14, tm15, tm16]
# This table contains all of the columns of the trio portion of Mozart's
# Musical Dice Game in order.
# This table contains all of the columns of the trio portion of Mozart's
# Musical Dice Game in order.
# This function takes a string as an argument and constructs a string that names
# one of the wav audio files that contains a measure of music for the minuet
# portion of Mozart's Musical Dice Game.
def minuet_filename(mmid):
    return "M"+mmid+".wav"

# This function takes a string as an argument and constructs a string that names
# one of the wav audio files that contains a measure of music for the trio
# portion of Mozart's Musical Dice Game.
def trio_filename(tmid):
    return "T"+tmid+".wav"

def quad_filename(tmid):
    return "Q"+tmid+".wav"

# This function takes a single interger, named 'num' as its argument. It
# generates the result of rolling 'num' many 6-sided dice.
def roll_dice(num = 1):
    count = 0
    while num >= 1:
        count = count + random.randint(1,6)
        num = num -1
    return count

# Inside this main function you will randomly select 16 measures from the minuet
# table, one from each column of the minuet table, and then randomly select, 16
# measures from the trio table, one from each column of the trio table. Each
# measure is represented by a string numeral, and corresponds to the name of a
# wav audio file that plays the selected measure of music.
# You must then access each of the selected wav files and play them using
# simpleaudio's interface. Make sure you wait for each measure to finish before
# playing the next measure.
def construct_waltz():
    minuetlist = []
    tlist = []
    marker = 0
    roll = 0
    mincount = 0
    while marker < 16:
        k = minuet_table[marker]
        kk = trio_table[marker]

        a = k[roll_dice(2)]
        aa = kk[roll_dice(2)]

        mfilename = minuet_filename(a)
        tfilename = trio_filename(aa)

        temp = [mfilename, tfilename]
        random.shuffle(temp)

        tlist.extend(temp)

        roll = 0
        marker = marker + 1
    return tlist

if __name__ == "__main__":
    wavelist = []
    ulist = construct_waltz()
    print(wavelist)
    for x in range(32):
        wavelist.append(simpleaudio.WaveObject.from_wave_file(ulist[x]))
    for y in range(32):
        wa = wavelist[y]
        play = wa.play()
        play.wait_done()
