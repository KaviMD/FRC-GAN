step = 2

if step == 1:
    from pytube import YouTube
    # List of Videos from: 
    # * https://docs.google.com/document/d/1dTGhGsim4t1xoeWh1I58DQ6xIg_3JI0-dUdBN9170FM/edit
    # * https://www.youtube.com/playlist?list=PLocx3vY5mUKNP-v3Wm1v01kLMvQ_iWMLe
    with open('videos.txt', 'r') as f:
        videos = f.readlines()
        for video in videos:
            YouTube(video).streams.first().download("data/raw_videos/", skip_existing=True)
            print("Downloaded", video)
    step = 2

if step == 2:
    import cv2
    import glob
    import os.path

    videos = glob.glob("data/raw_videos/*.mp4")

    for video in videos:
        name = video[16:][:-4]
        cap = cv2.VideoCapture(video)
        i = 0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            filename = "data/img/"+name+"."+str(i)+".png"
            if not os.path.isfile(filename):
                if i % 20 == 0:
                    cv2.imwrite(filename,frame)
                    print("Wrote", filename)
            i += 1

        cap.release()
