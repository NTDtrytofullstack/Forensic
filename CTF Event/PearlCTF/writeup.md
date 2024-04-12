# PearlCTF-2024.

### 1. hungry-cat.

- Bài này là 1 bài memory nhưng khá lỏ , mặc dù lỏ nhưng vẫn mất kha khá tg của mình , mình thử hết tất cả các cách thì `strings` phát ra lun :))) .
  ![1710521354252](image/writeup/1710521354252.png)
  
- Sau khi đọc writeup thì mình biết thêm 1 điều là , có 1 công cụ gọi là `Wayback machine` công cụ này là một kho lưu trữ kỹ thuật số của World Wide Web và những thông tin khác trên Internet, được tạo ra bởi Internet Archive, nó cho phép ta truy cập lại những đường dẫn ko thể truy cập được nữa , ví dụ điển hình là bài này.
![1710922987492](image/writeup/1710922987492.png)
- Mình sử dụng `Autospy` kiếm được 1 cái pastebin như sau nhưng khi mở lên thì ko thể truy cập được nữa.
![1710923052444](image/writeup/1710923052444.png)
- trong trường hợp này hãy sử dụng [web sau](http://web.archive.org) , nhập vào đó đường dẫn sau `http://pastebin.com/HtQgmG4a`.
![1710923190692](image/writeup/1710923190692.png)
- Click vào phần `URL` nhấp vào đường link thì yea serrr vào được cái link đó òi :).
![1710923246962](image/writeup/1710923246962.png)
### 2. pcap-busterz-1.

- Bài này cho mình 1 file `pcap` , mình mở lên thì thấy khá nhiều `TCP` nên mình follow `TCP` thử.
  ![1710521451609](image/writeup/1710521451609.png)
- Thì mình thấy cái này , ban đầu mình nghĩ nó với x và y là tọa độ của mỗi pixel , khi ta kết hợp dữ liệu này lại với nhau sẽ ra được dòng chữ flag hay gì đấy.
- Mình lên `GPT` để nhờ ẻm code hộ chương trình :))) .

```
from PIL import Image, ImageDraw

# Khởi tạo kích thước ảnh và màu nền
width = 100
height = 100
background_color = (255, 255, 255)  # Màu trắng

# Tạo một đối tượng ảnh mới
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Đường dẫn tới file chứa dữ liệu
file_path = "data.txt"

# Đọc dữ liệu từ file
with open(file_path, "r") as file:
    lines = file.readlines()

# Xử lý dữ liệu và vẽ các điểm trên ảnh
for line in lines:
    line = line.strip()  # Loại bỏ dấu xuống dòng và khoảng trắng thừa
    if line:
        # Tách thông tin về tọa độ và màu sắc từ dòng dữ liệu
        x = int(line.split(",")[0].split("=")[1].strip())
        y = int(line.split(",")[1].split("=")[1].strip())
        color = line.split(",")[2].split("=")[1].strip()

        # Xác định màu cho điểm
        pixel_color = (0, 0, 0) if color == "black" else (255, 255, 255)

        # Vẽ điểm trên ảnh
        draw.point((x, y), fill=pixel_color)

# Lưu ảnh
image.save("output.png")
```

- Với `data.txt` là dữ liệu này mà ảnh trên mình copy vào.
- Chạy source thì mình được 1 mã QR.
  ![1710521653387](image/writeup/1710521653387.png)
- Scan nó thì được flag thuii.
- *`FLAG: pearl{QR_rev0lution1ses_mod3rn_data_handl1ng}`*.

### 3. METAFILE.

- Bài này cũng là 1 bài memory, như mọi lần mình check `pslist`.
  ![1710521895682](image/writeup/1710521895682.png)
- Và cũng như mọi bài nó lại chạy 1 đống process , khó mà lần được đâu là hướng đi đúng , thì đành phải mò kiếm những thứ đáng nghi từ những điều nhỏ nhất , mình check `cmdline` xem có process nào chạy 1 file lạ lạ không nha.

```
2852    notepad.exe     "C:\Windows\system32\NOTEPAD.EXE" C:\Users\josh\Music\song.txt
```

- Thì mình thấy mỗi cái này thuii , mình thử dump về xem sao ha.

```
Never Gonna Give You Up


We're no strangers to love
You know the rules and so do I (do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
The flag is an image present on
Your heart's been aching, but you're too shy to say it (say it)
Inside, we both know what's been going on (going on)
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching, but you're too shy to say it (to say it)
Inside, we both know what's been going on (going on)
desktop in front of your eyes
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
But environment is not letting you see it...
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
```

- Cat file thì được bài hát như sau nhưng mà `But environment is not letting you see it...` có dòng này khá là nổi bật. mình check thử envars thử xem có gì ko.

```
2852    notepad.exe     0x1e2a0da1ba0   JOHN_MIGHT_NEED i_gave_up
```

- Mình check ở chỗ `notepad` thì có cái này khá là giống mật khẩu thì khá chắc là sẽ có 1 file nào đó ta cần mở khóa rồi đó, thì khúc này mình khá bí nên cứ theo bản năng xài `filescan` , mấy từ khóa thông dụng như `Desktop` để xem có file nào hữu ích ko nha.

```
0x8989a4549900  \Users\josh\Desktop\bWV0YXZlcnNlb2ZtYWRuZXNz.rar        216
```

- Đây gòi, thấy cái file `rar` này mình vui gần chết , mình dump về thử đổi đuôi nếu nó kêu cầu pass thì phần trăm giải được khá cao ha.
  ![1710523208757](image/writeup/1710523208757.png)
- Yea ser có 1 ảnh và có mk lun nha , nhập mk và xem cái ảnh có gì nào. pass là `i_gave_up` nha.
  ![1710523325589](image/writeup/1710523325589.png)
- Nó cho ta cái ảnh này và tên là 1 đoạn base64 , decode ra thử thì được dòng chữ này `metaverseofmadness` , nó có nhắc đến meta mình nghĩ ngay đến metadata khá liên quan đến `exiftool` nhưng mình vứt lên [APERISOLVE](https://www.aperisolve.com) cho chắc ăn :))) .
  ![1710523464237](image/writeup/1710523464237.png)
- *`FLAG: pearl{3v3ryb0dy_f0rgets_ab0ut_m3tadat4}`*.

### 4. Wifi Broken.

- Bài này khá là khó ấy khi ko biết hoi :)) , chứ khá lỏ , đề kêu ta kiếm mật khẩu và flag sẽ là mật khẩu đấy luôn. Chall cho ta file `.cap` khá lạ chắc là những file như này sẽ giải theo cách này , ta sẽ xài tool `aircrack-ng`.

1. ```
   strong
   ```

- Chạy khá là lâu á thì mình thu được pass là:
  ```
                             KEY FOUND! [ shenoydx ]


    Master Key     : 65 BB E2 8B 45 5B B1 BE 5D 96 78 82 14 CC 4B A1
                     1A 15 BC 85 B0 BA 31 A7 9C 83 9E 9D 47 D2 3E 32

    Transient Key  : FE 71 C4 60 DD E1 B6 2D 3C E2 04 12 78 18 95 6F
                     62 B2 04 9D D4 35 8B A2 DC 7D 85 AB DF 04 77 F8
                     B9 7B 8F FE 44 CC 98 6C 9C 83 98 80 D5 EC 72 98
                     A7 FC D7 23 9B 87 C8 CD BF CF 62 5A 97 41 DB 4B

    EAPOL HMAC     : 00 65 7D DC 8B 14 31 78 37 A8 10 86 BC 5B 70 08
  ```
- *`FLAG: pearl{shenoydx}`*.
### 5. Got-you.
- Chall này vẫn là 1 chall memory nhaaaaa.
```
Prompt : My friend, an avid Valorant fan, downloaded a captivating wallpaper only to find out I have jokingly REGISTERED a password on it . Now, he's turning to you for help in cracking the password so he can see the wallpaper. Can you help him crack the code and grant access to the wallpaper?
```
- Đề đưa ra luôn sẽ là 1 nguồn hint rất hữu ích , cùng phân tích nhé , cụ thể có thể hiểu là victim là 1 `valorant` fan đã tải 1 ảnh nào đó nhưng mà nó có mật khẩu và cụm `REGISTERED` được in hoa nữa, thế thì ta cứ thủ tục check pslist và cmdline xem như nào , sau đó là filescan các file ảnh phổ biến như `.png` hoặc `.jpg` nhaaa.
![1711086725871](image/writeup/1711086725871.png)
![1711086873375](image/writeup/1711086873375.png)
- Có quá nhiều các dữ kiện để phân tích , khá khó nếu thực sự để mò từng cái một , vậy thì ta thử check filescan liệu có 1 file ảnh nào lạ ko nhé.

- Mìnhthử kiếm 1 lần cả 2 định dạng nhưng kết quả không có ảnh nào đáng nghi cạ , đề có nhắc đến là 1 valorant fan :))) , hy vọng ko phải `sen` con , mình sẽ thử filescan với cụm `valorant` xem như nào.
![1711087538494](image/writeup/1711087538494.png)
- Đây gòi , dump nó về và xem nội dung như nào thui nhé.
```
In the sprawling universe of Valorant, hidden beneath the surface of our reality, lies a secret organization known as the "Order of the Eclipse." Founded centuries ago by a clandestine group of scholars and mystics, the Order sought to maintain the delicate balance between the material world and the mysterious realm of the "Radiant."
The Radiant is a dimension of pure energy, inhabited by enigmatic beings known as "Celestials." These Celestials possess unimaginable power, capable of shaping reality itself. However, their influence can also be destructive if left unchecked.
To prevent chaos from engulfing both realms, the Order of the Eclipse developed a technology known as "Radianite." This rare and potent energy source allows individuals to harness the power of the Radiant, granting them extraordinary abilities beyond human comprehension.
As the world evolved, so too did the Order's mission. They recruited individuals from all walks of life, each with their own unique talents and backgrounds, to join their ranks as agents. These agents are tasked with safeguarding the world from threats both mundane and supernatural, using their Radianite-infused abilities to maintain peace and order.
However, not everyone agrees with the Order's methods. https://mega.nz/file/ZjgRDKoY#GJwW9OnSI6LfuJE-syODo4cSHkxcdvMkD_Gt1HmvsLI. A rival organization known as the "Nexus" believes that humanity should embrace the power of the Radiant without restraint, seeking to overthrow the Order and claim dominion over both realms.
Caught in the middle of this ancient conflict are the agents of Valorant, each with their own reasons for fighting. Some seek redemption for past sins, while others are driven by a desire for justice or the thrill of battle. But as they clash in epic showdowns across the globe, they may ultimately hold the fate of the world in their hands.
Among the notable agents of the Order are:
Sova: Hailing from Russia, Sova is a skilled hunter who uses his keen instincts and specialized equipment to track down enemies. Trained in the ways of the wild, he harnesses the power of Radianite to enhance his senses and strike with deadly precision.
Phoenix: A fiery and enigmatic agent, Phoenix wields the power of flame with reckless abandon. With the ability to manipulate fire at will, he leaves a trail of destruction in his wake, incinerating enemies and illuminating the darkest corners of the battlefield.
Jett: A nimble and agile fighter, Jett utilizes her mastery of the wind to outmaneuver her opponents. With swift strikes and unparalleled speed, she dances through danger with grace and finesse, leaving her enemies bewildered and outmatched.
These agents, along with many others, stand ready to defend the world from the forces of darkness and ensure that the balance between the material realm and the Radiant remains intact. But as tensions escalate and ancient secrets are unearthed, they may soon find themselves embroiled in a conflict that could shape the fate of the universe itself.
``` 
![1711090457775](image/writeup/1711090457775.png)
- Đập ngay vào mắt là 1 link mega, tải về 1 file rar nhưng nó yêu cầu pass, bên trong nó là 1 file ảnh , vậy là ta đã kiếm được ảnh đó rồi , việc còn lại là tìm kiếm password như đề đã hint cho ta thôi.
![1711090884608](image/writeup/1711090884608.png)
- Đề có đề cập tới `REGISTERED` mình suy đoán rằng thứ gì đó có thể được lưu trữ trong Windows registry , nên mình sẽ thử xài lệnh này :
```
$ python3 vol.py -f /mnt/d/FORENSICS/challenge/PearlCTF/got-you/dump_2.raw windows.registry.printkey
```
![1711091319060](image/writeup/1711091319060.png)
- Mình thấy được 1 đoạn base64 , mình decode ra thì được pass là `ViperUltimate77` , mình thử nhập pass và file rar đấy nhưng bị sai , vậy là pass này được dùng trong 1 file bị khóa nào đó khác.
- Mình thử kiếm có file zip nào khả nghi không thì ko tìm kiếm được file nào hữu ích cả, thì mình xem lại pslist chỉ có duy nhất `KeePass` là yếu tố duy nhất mình nghĩ đến sẽ cần pass để mở 1 file nào đó , nên mình scan thử có file `.kdbx` nào không nha.
![1711092057341](image/writeup/1711092057341.png)
- Ở đây có 1 file lun này , dump nó về mình nhập pass trên thì được như này.
![1711094801661](image/writeup/1711094801661.png)
- Ta sẽ có 5 user và 5 password khác nhau , mình thử từng cái 1 thì mật khẩu chính xác để mở file rar là `radiant` của user `Chamber`.
![1711094893387](image/writeup/1711094893387.png)
![1711094930642](image/writeup/1711094930642.png)
- Nhập pass là `radiant` vào thì ta có ảnh như trên và có flag lun :>> .
- *`FLAG: pearl{th4y_4r3_s0_d34d}`*
### 6. the-3-fragmenteers.
- Chall này cũng là 1 bài memory với đề như sau: 
```
 My friends got their hands on my system and told me he did something to a file that was important to me. Help me discover what he did.
```
- Đại khái đề là victim đã bị bạn đụng đến 1 file nào đó quan trọng , liên quan đến file thì chỉ có filescan thui , thế thì ngồi mò hết các file xem có file nào đáng nghi ko.
- Mình có nghía qua cmdline thì có cái lệnh powershell này , nhưng mà nó ko có tác dụng gì cả :Đ.
![1711095699638](image/writeup/1711095699638.png)
- Chua đấy , ngồi mò thì mình kiếm được file này Mình dump file đó về , nội dung bên trong là:
![1711097028547](image/writeup/1711097028547.png)
```
Here is the first part https://mega.nz/file/03IiVCpR#nF_fPNIE-vU98nGalpGWfbLNY7nJlBJbyhfcgMSQqyE


By the way u have to solve this riddle to get the file...

In shadows deep, where whispers fade,
Lies a truth in a mirrored glade.
Seek the cipher, in silence bade,
Where echoes of secrets softly cascade.
```
- file text cho ta 1 link mega down về 1 file rar có mật khẩu và hint của mật khẩu đó.
![1711106818375](image/writeup/1711106818375.png)
- để trả lời câu hỏi trên mình lên gpt :Đ , chứ chịu sao biết được.
![1711106904109](image/writeup/1711106904109.png)
- nhập pass là `reflection` nó cho mình 2 file `hint_1.txt` và `xaa.unknown`, nội dụng của file hint là :
```
So u found the first part easily ig...

2nd part might bhi present at the place at opens up when u start the system... 
```
- nội dung file còn lại thì ko biết cụ thể nhưng nhìn header thì nó là file `PDF` nhưng ở phần hint nó bảo `first part` có nghĩa là file pdf này chưa đầy đủ và sẽ có part 2 hoặc part 3 nữa.
- hint bảo đại khái là part 2 sẽ ở nơi khi mà ta khởi động system , thì mình nghĩ ngay đến `Desktop` , cùng check desktop xem có file nào đáng ngờ ko.
![1711107275205](image/writeup/1711107275205.png)
- Đây gòi dump nó về , thì nó cho mình 1 đường link tải về 1 file `xab.unknown` , đây chính là phần dữ liệu tiếp theo của file pdf , và hint nó như sau :
```
You finally reached here....

here you go take the 2nd part --- https://mega.nz/file/N2RljAQL#gaNpJh5mEM60nceL0NC5SEiFvLVbJNdFcpAxL5Lo7gs

and Btw 3rd part is also a text file but the name is base64 encoded
good luck finding it.....
```
- Đại khái hint part 3 là 1 file text có tên là base64 , vào filescan với filter là `.txt` mà kiếm hoi.
![1711107697451](image/writeup/1711107697451.png)
- dump nó về , xem nội dung bên trong và decode base64 name file là được.
- Nội dụng bên trong file bảo là đây là phần cuối cùng rồi ghép tất cả dữ liệu lại là ta sẽ có flag :
```
Ahh... 

You found it, I thought it might be difficult to find this one..
Now u have all the parts, I think you can get the flag...
```
- Nội dung của đoạn base64 là link mega tải về file `xac.unknown` vậy là ta có đầy đủ dữ liệu của file `PDF` rồi , ta lưu tất cả dữ liệu vào 1 file `.pdf` là được. Mình xài lệnh sau:
```
$ cat xa* > file.pdf
```
- ở trang 12 thì ta thu được flag.
![1711108140381](image/writeup/1711108140381.png)\
- *`FLAG: pearl{f1l3_15_n0t_br0k3_c0mpl3t3ly}`*.
### 7. hungry-cat-2.
- Chall này vẫn là 1 bài memory và đề cho hint là :
```
Prompt : The cat got sick after eating the infected food given by my friend. Now the cat is angry and wants. Help my friend find the right food else the cat might scratch him
```
- Đại khái thì con mèo của victim bị bệnh cần ta tìm cách để giúp nó và thường thì ta sẽ search google đúng không và khi check pslist , có rất nhiều process `chrome.exe` chạy cùng 1 lúc đồng thời cũng cố quan điểm trên . Hướng giải của chall này sẽ xoay quanh `chrome` thế thì ta kiếm file history dump nó về và check xem có gì đáng nghi hong thuuiii.
![1711108765410](image/writeup/1711108765410.png)
![1711112990390](image/writeup/1711112990390.png)
- Ở chỗ này có 2 file như nhau , tải cái nào cũng được nhé.
![1711113031384](image/writeup/1711113031384.png)
- 1 link pastebin , nhưng ko truy cập được ta bắt buộc xài `Wayback machine` thì nội dụng nó như sau: 
```
Feedingyourcatproperlyisessentialforitshealthandwell-being.Here'sanextendedlistofinstructionstoensureyou'reprovidingthebestcareforyourfelinefriend:EstablishaFeedingSchedule:Catsthriveonroutine,soestablishaconsistentfeedingschedule.Aimfortwomealsadayforadultcats,andmorefrequentfeedingsforkittens.SelecttheRightFood:Choosehigh-qualitycatfoodthatmeetsthenutritionalneedsofyourcat.Consultwithyourveterinarianforrecommendationsbasedonyourcat'sage,weight,andhealthcondition.MeasurePortions:Avoidoverfeedingorunderfeedingbymeasuringouttheappropriateportionsizesaccordingtothefeedingguidelinesonthecatfoodpackaging.ProvideFreshWater:Alwaysensureyourcathasaccesstofresh,cleanwater.Changethewaterdailytokeepitappealingandfreefromcontaminants.AvoidTableScraps:Humanfoodcanbeharmfultocats,sorefrainfromfeedingthemtablescraps.Sticktocat-specificfoodtomeettheirdietaryrequirements.MonitorEatingHabits:Payattentiontoyourcat'seatinghabits.Asuddenlossofappetiteorincreaseinfoodconsumptioncouldsignalanunderlyinghealthissue.WatchforFoodAllergies:Keepaneyeoutforanysignsoffoodallergiesorintolerances,suchasvomiting,diarrhea,orskinproblems.Ifyoususpectanallergy,consultyourvetforadviceonswitchingtoahypoallergenicdiet.IntroduceNewFoodsGradually:Whenintroducingnewcatfoodortransitioningtoadifferentbrand,dosograduallyoverthecourseofseveraldaystopreventdigestiveupset.StoreFoodProperly:Storecatfoodinacool,dryplaceawayfromsunlightandmoisturetomaintainitsfreshnessandnutritionalintegrity.Sealopenedbagsorcanstightlytopreventspoilage.CleanFeedingDishesRegularly:Washyourcat'sfoodandwaterbowlsregularlywithhot,soapywatertopreventbacteriabuildupandcontamination.https://mega.nz/file/0rxTyKjK#LdrIoTBNdRshXczrnusbxHNqXqYPA-my6kTezWFUOMYConsiderInteractiveFeeders:Interactivefeedersorpuzzletoyscanprovidementalstimulationandslowdownfasteaters,promotinghealthiereatinghabitsandpreventingobesity.MonitorWeight:Regularlyweighyourcatandmonitoritsbodyconditionscoretoensureitmaintainsahealthyweight.Adjustportionsizesaccordinglytopreventobesityorundernourishment.ConsultwithaVeterinarian:Ifyouhaveanyconcernsaboutyourcat'sdietorfeedinghabits,consultwithaveterinarianforpersonalizedadviceandrecommendations.BeMindfulofSpecialNeeds:Catswithspecialdietaryneeds,suchasthosewithmedicalconditionslikediabetesorkidneydisease,mayrequirespecializeddiets.Workcloselywithyourvettomeettheseneeds.AvoidFeedingBeforeVetVisits:Unlessspecificallyinstructedbyyourvet,avoidfeedingyourcatbeforeveterinaryappointmentstoensureaccuratemeasurementsandassessments.Byfollowingtheseinstructions,you'llbeabletoprovideyourcatwithahealthyandbalanceddiet,contributingtoitsoverallwell-beingandlongevity.
```
- Đập ngay vào mắt cái link mega `https:meganzfile0rxTyKjK#LdrIoTBNdRshXczrnusbxHNqXqYPA-my6kTezWFUOMY` , nó cho ta tải về 1 file `flag.png` là 1 cái `QR code` quét cái mã thì nó dẫn mình tới link này `https://youtu.be/dQw4w9WgXcQ?si=vhDYncP8vMvBdz1O` :Đ , rickroll lun có lẽ là flag được nằm ở nơi khác thì xem qua 1 hồi file history thì ở ngay đầu có 1 đoạn base32 như này decode ra thì ra được 1 link pastebin nữa `https://pastebin.com/3ceSY7qf` nó vẫn ko truy cập được và sẽ phải xài wayback.
- Nội dung nó khá dài :
```
In a quaint little neighborhood, nestled between rows of colorful houses, there lived a cat named Whiskers. Whiskers was notorious for his insatiable appetite and his equally fiery temper. His hunger seemed to know no bounds, and his owners often found themselves rushing to refill his food bowl multiple times a day.
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Despite being well-fed, Whiskers was always grumpy and irritable. Any disruption to his routine or delay in his mealtime would send him into a fit of angry meows and sharp claws. https://mega.nz/file/Qjxh2JQQ . He would stalk around the house, tail lashing, demanding to be fed immediately.
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Neighbors learned to steer clear of Whiskers when he was in one of his moods, as even the slightest provocation could set him off. His reputation as the hungry and angry cat of the neighborhood spread far and wide, with some even affectionately referring to him as "Hangry Whiskers."
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Despite his temperamental nature, Whiskers had a soft spot for his owners, and they doted on him, catering to his every whim to keep the peace. But woe betide anyone who dared to cross paths with this hungry and angry feline without a tasty treat in hand.
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
```
- Tiếp tục là 1 file mega , truy cập vào thì nó yêu cầu pass. Và có lẻ đây là lúc xài đến ảnh mà đề bài cho sẵn `you_might_need_it.png`, tên của nó là bạn sẽ cần đến nó thì chắc chắn bức ảnh này sẽ có pass.
![1711113765362](image/writeup/1711113765362.png)
![1711113829875](image/writeup/1711113829875.png)
- nhìn vào ảnh thì ta có thể dễ dàng nhận ra với mỗi pixel đen hoặc trắng sẽ tương ứng với `0` và `1`, ta sẽ viết code python chuyển hóa nó về dạng nhị phân nhaaa.

```
from PIL import Image

file = "./you_might_need_it.png"

image = Image.open(file)
pixel = list(image.getdata())

bit_stream = ""

for p in pixel :
    if p == (0,0,0) : 
        bit_stream += '0'
    else : 
        bit_stream += '1'

key_encoded = ''
for i in range(0,len(bit_stream), 8) :
    key_encoded += chr(int(bit_stream[i:i+8],2))

print(key_encoded)

```
- Code trên sẽ trả ra đoạn base64 sau `eHlrTmNwd05ha2s2aU96MnpaMWFyMGY0bmZ5NFAxTjEzY0kwcmFfcFlvcw==` decode nó ra thì được `xykNcpwNakk6iOz2zZ1ar0f4nfy4P1N13cI0ra_pYos` , đây chính là pass của link mega trên , tải nó về được 1 file ảnh `cat.png` trên đó có lun flag.
![1711114069500](image/writeup/1711114069500.png)
- *`FLAG: pearl{Hungry_c4t_w4nts_m0r3_f00d}`*