# homework6
  
**電腦視覺特效-第六組**  
  
## Our videos
在此部分有兩個吾組所拍攝的影片：<br>
第一部影片連結：https://www.youtube.com/watch?v=y8fFurI6jO0&feature=youtu.be&fbclid=IwAR1IfEVKWLTf5CdBo7Uj-6ZlPcpIOfGMlh28aO_A9kzUQw1Fj3eLusEcOIU <br><br>
第二部影片連結：https://www.youtube.com/watch?v=gTkzlIeFdwE&feature=youtu.be&fbclid=IwAR3hWKSwmiKKY_zoBq-F3ueMI6Ng_eoi4Be_Ry-lNWccmnfTsGz-scTwXGQ <br><br>

第一部影片將會提供給第二部分的Visual effects with ORB-SLAM所使用，而第二部影片將會提供給第三部分的Visual effects with any post-production software所使用。<br><br>


## Visual effects with ORB-SLAM  
在此部分，吾組首先依照助教於HW6 github所提供的內容，安裝好ORB-SLAM2所需的相關要求，並且下載Monocular Examples中的TUM Dataset的fr1/xyz來進行測試。在確認利用此dataset來跑ORB-SLAM2有跑出確定的結果後，吾組旋即利用利用第一部影片來切frame，並且根據ORB-SLAM2所要求的命名來對切出來的frame命名，並且製作出跑ORB-SLAM2所需rgb.txt，而rgb.txt的格式如下圖所示：<br><br>
<img src="https://github.com/TingWeiHuang22/homework6/blob/master/rgb.txt.png" width="300" height="300"><br><br>
而在製作完rgb.txt並且切出相對應的frames的照片要跑完ORB-SLAM2後，發現在執行的過程中會一直找不出KeyFrame Position(即是Camera Position)，後來經過相關測試後，發現是相機參數沒有調整好才會出現這個問題。而經過吾組多方嘗試參數的調整後，以下附圖的參數：<br><br>
<img src="https://github.com/TingWeiHuang22/homework6/blob/master/param.png" width="300" height="300"><br><br>
即可讓吾組的Dataset在執行ORB-SLAM2時，能夠抓到相對應的KeyFrame Position，如下圖所示：<br><br>
<img src="https://github.com/TingWeiHuang22/homework6/blob/master/keyframes8.png" width="300" height="300"><br><br>
而在執行玩ORB-SLAM2後，即可產生KeyFrameTrajectory.txt，如下圖所示：<br><br>
<img src="https://github.com/TingWeiHuang22/homework6/blob/master/trajectory.png" width="300" height="300"><br><br>
由KeyFrameTrajectory.txt的格式可以得知，它的每一個row共有7個值，第一個值為偵測出有Camera position的圖片名稱，接下來的7的值分別是與相機有關的參數(前三個值是與Camera的位置有關，後4個值吾組推測是與Camera的旋轉資訊有關)。

## Visual effects with any post-production software
在此部分，我們利用After Effect CC這個後製軟體來對第二部影片進行後製，而After Effect這個後製軟體的操作流程則是從以下連結影片所學來的：<br><br>
[連結]：https://www.youtube.com/watch?v=t6hgmRZZ4WE&fbclid=IwAR0viDbbr6cHeuIDEZvv8pUrx8CXnp3iQxAnNtzA4n_uCgFjId-a244jcIo <br><br>
而第二部影片經過後製軟體所做出來的結果影片則是以下連結：https://www.youtube.com/watch?v=3iMWoA4aYBI&feature=youtu.be&fbclid=IwAR0gLJT36D8x7X--BxlecNTpGpJ6LepoBMIye2LPKqFBST38smk_HAqL5s4 <br><br>
而在後製軟體我們所增加的Visual effects主要有三個：第一個是吾組模擬實驗室的地面有出現一個超大蜘蛛、第二個則是模擬在一個電腦螢幕上面新增了有小小兵說Hello的圖案、第三個則是則是模擬有雷姆模型站在電腦主機上面!<br><br>
 
## Compare above methods

## Special effects
