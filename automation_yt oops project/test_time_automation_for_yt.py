from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from voicerecog_module import *
from selenium.webdriver.common.by import By
from difflib import SequenceMatcher
import time
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')
path=Service("C:\Program Files\BraveSoftware\Brave-Browser\Application\112.1.50.119")
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
# Load the YouTube homepage
f = open("C:\\Users\\utkar\\OneDrive\\vscode\\automation_yt oops project\\test_topics.txt", "r")
topics=f.read()
sep=(input("enter the separator :-"))[0]
search_list=list(topics.split(sep))
start_index=input("input start topic no. or say start from begin :- ") 
if start_index.isdigit()==True:
    start_index=int(start_index)
else:
    start_index=1
i=start_index-1
driver = webdriver.Chrome(service=path,options=options)
for search_term in search_list[i:]:
    print(start_index,"out of",len(search_list))
    start_index+=1
    driver.get("https://www.youtube.com")
    search_box = driver.find_element(By.NAME,"search_query")
    search_box.send_keys(search_term)
    
    search_box.send_keys(Keys.RETURN)
    search_box.clear()
    videos = driver.find_elements(By.XPATH,"//div[@id='contents']//ytd-video-renderer")
    title_similarity_scores = {}
    top_video_element = None
    for video in videos:
                title_element = video.find_element(By.XPATH,".//a[@id='video-title']")
                title = title_element.get_attribute("title")
                similarity_score = SequenceMatcher(None, search_term.lower(), title.lower()).ratio()
                title_similarity_scores[title] = similarity_score

                if len(title_similarity_scores) > 0:
                    sorted_titles = sorted(title_similarity_scores, key=title_similarity_scores.get, reverse=True)
                    top_video_title = sorted_titles[0]
                    top_video_element = None
                    for video in videos:
                        title_element = video.find_element(By.XPATH,".//a[@id='video-title']")
                        title = title_element.get_attribute("title")
                        if title == top_video_title:
                            top_video_element = video
                            break
                        
                    top_video_element.click()
                    time.sleep(2)
                    top_video_element.send_keys("f")
                    #driver.find_element(By.XPATH,"//*[@id='movie_player']/div[33]/div[2]/div[2]/button[9]").click()
                    break
    print("listening")    
# Listen for voice commands
    while True:
        try:
            command=voice()
    # Respond to voice commands
            if "search for" in command:
                search_term = command.replace("search for ", "")
                search_box = driver.find_element(By.NAME,"search_query")
                search_box.send_keys(search_term)
                search_box.send_keys(Keys.RETURN)
                search_box.clear()
                videos = driver.find_elements(By.XPATH,"//div[@id='contents']//ytd-video-renderer")
                title_similarity_scores = {}
                top_video_element = None
                for video in videos:
                    title_element = video.find_element(By.XPATH,".//a[@id='video-title']")
                    title = title_element.get_attribute("title")
                    similarity_score = SequenceMatcher(None, search_term.lower(), title.lower()).ratio()
                    title_similarity_scores[title] = similarity_score
                
                    if len(title_similarity_scores) > 0:
                        sorted_titles = sorted(title_similarity_scores, key=title_similarity_scores.get, reverse=True)
                        top_video_title = sorted_titles[0]
                        top_video_element = None
                        for video in videos:
                            title_element = video.find_element(By.XPATH,".//a[@id='video-title']")
                            title = title_element.get_attribute("title")
                            if title == top_video_title:
                                top_video_element = video
                                break
                        if top_video_element:
                            top_video_element.click()
                            break
                        else:
                            Speech("Failed to select video. Please try again.")
                            break
                    else:
                        Speech("No videos found. Please try again with a different search term.")
                
                    try:
                        top_video_element.click()
                    except TypeError:
                        Speech("retry ")
            
            if "pause" in command:
                pause_button = driver.find_element(By.CSS_SELECTOR,"#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button")
                pause_button.click()
            elif "play" in command:
                if "next video" in command:
                    seek_forward_button = driver.find_element(By.CSS_SELECTOR,"#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > a.ytp-next-button.ytp-button")
                    seek_forward_button.click()
                else:
                    play_button = driver.find_element(By.CSS_SELECTOR,"#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button")
                    play_button.click()
            elif "next video" in command:
                
                #driver.find_element(By.CSS_SELECTOR,"#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > a.ytp-next-button.ytp-button").click()
                break
            elif "mute" in command:
                driver.find_element(By.CSS_SELECTOR,"#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > span > button").click()
            elif "exit" in command or 'later' in command :
                exit()
        except TypeError:
            pass
# Quit the browser and release the microphone resources
driver.quit()
f.close()