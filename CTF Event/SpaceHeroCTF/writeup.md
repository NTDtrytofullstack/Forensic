# SpaceHero CTF 2024.
### I.Petey the Panther's Guide to the Galaxy.
- bài này cho mình 1 ảnh `.jpg`.
![1713376872582](image/writeup/1713376872582.png)
- Mình binwalk thì thấy bên trong nó có 1 folder secrets và bên trong folder là 1 đống ảnh, mình extract nó ra để xem nội dung của mấy cái ảnh như thế nào.
```
$ binwalk A_Real_Space_Hero.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
1891          0x763           Certificate in DER format (x509 v3), header length: 4, sequence length: 1573
3471          0xD8F           Certificate in DER format (x509 v3), header length: 4, sequence length: 1746
5224          0x1468          Certificate in DER format (x509 v3), header length: 4, sequence length: 1455
6888          0x1AE8          Certificate in DER format (x509 v3), header length: 4, sequence length: 1730
8622          0x21AE          Certificate in DER format (x509 v3), header length: 4, sequence length: 1710
10336         0x2860          Certificate in DER format (x509 v3), header length: 4, sequence length: 1421
13067         0x330B          TIFF image data, big-endian, offset of first image directory: 8
256834        0x3EB42         Zip archive data, at least v1.0 to extract, name: secrets/
256872        0x3EB68         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 164, name: secrets/piece_0.png
257044        0x3EC14         Zip archive data, at least v2.0 to extract, compressed size: 106, uncompressed size: 120, name: secrets/piece_1.png
257199        0x3ECAF         Zip archive data, at least v2.0 to extract, compressed size: 152, uncompressed size: 182, name: secrets/piece_10.png
257401        0x3ED79         Zip archive data, at least v2.0 to extract, compressed size: 144, uncompressed size: 170, name: secrets/piece_100.png
257596        0x3EE3C         Zip archive data, at least v2.0 to extract, compressed size: 135, uncompressed size: 145, name: secrets/piece_101.png
257782        0x3EEF6         Zip archive data, at least v2.0 to extract, compressed size: 89, uncompressed size: 121, name: secrets/piece_102.png
257922        0x3EF82         Zip archive data, at least v2.0 to extract, compressed size: 129, uncompressed size: 148, name: secrets/piece_103.png
258102        0x3F036         Zip archive data, at least v2.0 to extract, compressed size: 114, uncompressed size: 124, name: secrets/piece_104.png
258267        0x3F0DB         Zip archive data, at least v2.0 to extract, compressed size: 150, uncompressed size: 198, name: secrets/piece_105.png
258468        0x3F1A4         Zip archive data, at least v2.0 to extract, compressed size: 146, uncompressed size: 183, name: secrets/piece_106.png
258665        0x3F269         Zip archive data, at least v2.0 to extract, compressed size: 215, uncompressed size: 233, name: secrets/piece_107.png
258931        0x3F373         Zip archive data, at least v2.0 to extract, compressed size: 90, uncompressed size: 191, name: secrets/piece_108.png
259072        0x3F400         Zip archive data, at least v2.0 to extract, compressed size: 143, uncompressed size: 177, name: secrets/piece_109.png
259266        0x3F4C2         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_11.png
259391        0x3F53F         Zip archive data, at least v2.0 to extract, compressed size: 161, uncompressed size: 186, name: secrets/piece_110.png
259603        0x3F613         Zip archive data, at least v2.0 to extract, compressed size: 117, uncompressed size: 153, name: secrets/piece_111.png
259771        0x3F6BB         Zip archive data, at least v2.0 to extract, compressed size: 151, uncompressed size: 169, name: secrets/piece_112.png
259973        0x3F785         Zip archive data, at least v2.0 to extract, compressed size: 124, uncompressed size: 188, name: secrets/piece_113.png
260148        0x3F834         Zip archive data, at least v2.0 to extract, compressed size: 147, uncompressed size: 197, name: secrets/piece_114.png
260346        0x3F8FA         Zip archive data, at least v2.0 to extract, compressed size: 89, uncompressed size: 121, name: secrets/piece_115.png
260486        0x3F986         Zip archive data, at least v2.0 to extract, compressed size: 129, uncompressed size: 148, name: secrets/piece_116.png
260666        0x3FA3A         Zip archive data, at least v2.0 to extract, compressed size: 144, uncompressed size: 153, name: secrets/piece_117.png
260861        0x3FAFD         Zip archive data, at least v2.0 to extract, compressed size: 89, uncompressed size: 121, name: secrets/piece_118.png
261001        0x3FB89         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 150, name: secrets/piece_119.png
261175        0x3FC37         Zip archive data, at least v2.0 to extract, compressed size: 188, uncompressed size: 196, name: secrets/piece_12.png
261413        0x3FD25         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 192, name: secrets/piece_120.png
261556        0x3FDB4         Zip archive data, at least v2.0 to extract, compressed size: 111, uncompressed size: 129, name: secrets/piece_121.png
261718        0x3FE56         Zip archive data, at least v2.0 to extract, compressed size: 136, uncompressed size: 165, name: secrets/piece_122.png
261905        0x3FF11         Zip archive data, at least v2.0 to extract, compressed size: 115, uncompressed size: 158, name: secrets/piece_123.png
262071        0x3FFB7         Zip archive data, at least v2.0 to extract, compressed size: 101, uncompressed size: 117, name: secrets/piece_124.png
262223        0x4004F         Zip archive data, at least v2.0 to extract, compressed size: 124, uncompressed size: 161, name: secrets/piece_125.png
262398        0x400FE         Zip archive data, at least v2.0 to extract, compressed size: 113, uncompressed size: 150, name: secrets/piece_126.png
262562        0x401A2         Zip archive data, at least v2.0 to extract, compressed size: 207, uncompressed size: 232, name: secrets/piece_127.png
262820        0x402A4         Zip archive data, at least v2.0 to extract, compressed size: 116, uncompressed size: 165, name: secrets/piece_128.png
262987        0x4034B         Zip archive data, at least v2.0 to extract, compressed size: 120, uncompressed size: 134, name: secrets/piece_129.png
263158        0x403F6         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_13.png
263283        0x40473         Zip archive data, at least v2.0 to extract, compressed size: 140, uncompressed size: 163, name: secrets/piece_130.png
263474        0x40532         Zip archive data, at least v2.0 to extract, compressed size: 118, uncompressed size: 171, name: secrets/piece_131.png
263643        0x405DB         Zip archive data, at least v2.0 to extract, compressed size: 190, uncompressed size: 202, name: secrets/piece_132.png
263884        0x406CC         Zip archive data, at least v2.0 to extract, compressed size: 142, uncompressed size: 156, name: secrets/piece_133.png
264077        0x4078D         Zip archive data, at least v2.0 to extract, compressed size: 116, uncompressed size: 165, name: secrets/piece_134.png
264244        0x40834         Zip archive data, at least v2.0 to extract, compressed size: 138, uncompressed size: 167, name: secrets/piece_135.png
264433        0x408F1         Zip archive data, at least v2.0 to extract, compressed size: 139, uncompressed size: 152, name: secrets/piece_136.png
264623        0x409AF         Zip archive data, at least v2.0 to extract, compressed size: 108, uncompressed size: 142, name: secrets/piece_137.png
264782        0x40A4E         Zip archive data, at least v2.0 to extract, compressed size: 135, uncompressed size: 165, name: secrets/piece_138.png
264968        0x40B08         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_139.png
265094        0x40B86         Zip archive data, at least v2.0 to extract, compressed size: 122, uncompressed size: 164, name: secrets/piece_14.png
265266        0x40C32         Zip archive data, at least v2.0 to extract, compressed size: 142, uncompressed size: 171, name: secrets/piece_140.png
265459        0x40CF3         Zip archive data, at least v2.0 to extract, compressed size: 132, uncompressed size: 191, name: secrets/piece_141.png
265642        0x40DAA         Zip archive data, at least v2.0 to extract, compressed size: 177, uncompressed size: 203, name: secrets/piece_142.png
265870        0x40E8E         Zip archive data, at least v2.0 to extract, compressed size: 196, uncompressed size: 230, name: secrets/piece_143.png
266117        0x40F85         Zip archive data, at least v2.0 to extract, compressed size: 148, uncompressed size: 213, name: secrets/piece_144.png
266316        0x4104C         Zip archive data, at least v2.0 to extract, compressed size: 150, uncompressed size: 156, name: secrets/piece_145.png
266517        0x41115         Zip archive data, at least v2.0 to extract, compressed size: 129, uncompressed size: 134, name: secrets/piece_146.png
266697        0x411C9         Zip archive data, at least v2.0 to extract, compressed size: 213, uncompressed size: 282, name: secrets/piece_147.png
266961        0x412D1         Zip archive data, at least v2.0 to extract, compressed size: 109, uncompressed size: 145, name: secrets/piece_148.png
267121        0x41371         Zip archive data, at least v2.0 to extract, compressed size: 206, uncompressed size: 231, name: secrets/piece_149.png
267378        0x41472         Zip archive data, at least v2.0 to extract, compressed size: 106, uncompressed size: 120, name: secrets/piece_15.png
267534        0x4150E         Zip archive data, at least v2.0 to extract, compressed size: 127, uncompressed size: 141, name: secrets/piece_150.png
267712        0x415C0         Zip archive data, at least v2.0 to extract, compressed size: 173, uncompressed size: 210, name: secrets/piece_151.png
267936        0x416A0         Zip archive data, at least v2.0 to extract, compressed size: 150, uncompressed size: 193, name: secrets/piece_152.png
268137        0x41769         Zip archive data, at least v2.0 to extract, compressed size: 83, uncompressed size: 121, name: secrets/piece_153.png
268271        0x417EF         Zip archive data, at least v2.0 to extract, compressed size: 152, uncompressed size: 177, name: secrets/piece_154.png
268474        0x418BA         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 140, name: secrets/piece_155.png
268648        0x41968         Zip archive data, at least v2.0 to extract, compressed size: 173, uncompressed size: 197, name: secrets/piece_156.png
268872        0x41A48         Zip archive data, at least v2.0 to extract, compressed size: 134, uncompressed size: 159, name: secrets/piece_157.png
269057        0x41B01         Zip archive data, at least v2.0 to extract, compressed size: 145, uncompressed size: 170, name: secrets/piece_158.png
269253        0x41BC5         Zip archive data, at least v2.0 to extract, compressed size: 144, uncompressed size: 156, name: secrets/piece_159.png
269448        0x41C88         Zip archive data, at least v2.0 to extract, compressed size: 106, uncompressed size: 120, name: secrets/piece_16.png
269604        0x41D24         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 165, name: secrets/piece_160.png
269778        0x41DD2         Zip archive data, at least v2.0 to extract, compressed size: 235, uncompressed size: 293, name: secrets/piece_161.png
270064        0x41EF0         Zip archive data, at least v2.0 to extract, compressed size: 155, uncompressed size: 180, name: secrets/piece_162.png
270270        0x41FBE         Zip archive data, at least v2.0 to extract, compressed size: 170, uncompressed size: 182, name: secrets/piece_163.png
270491        0x4209B         Zip archive data, at least v2.0 to extract, compressed size: 113, uncompressed size: 143, name: secrets/piece_164.png
270655        0x4213F         Zip archive data, at least v2.0 to extract, compressed size: 181, uncompressed size: 215, name: secrets/piece_165.png
270887        0x42227         Zip archive data, at least v2.0 to extract, compressed size: 154, uncompressed size: 184, name: secrets/piece_166.png
271092        0x422F4         Zip archive data, at least v2.0 to extract, compressed size: 154, uncompressed size: 210, name: secrets/piece_167.png
271297        0x423C1         Zip archive data, at least v2.0 to extract, compressed size: 138, uncompressed size: 162, name: secrets/piece_168.png
271486        0x4247E         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_169.png
271612        0x424FC         Zip archive data, at least v2.0 to extract, compressed size: 106, uncompressed size: 120, name: secrets/piece_17.png
271768        0x42598         Zip archive data, at least v2.0 to extract, compressed size: 146, uncompressed size: 216, name: secrets/piece_170.png
271965        0x4265D         Zip archive data, at least v2.0 to extract, compressed size: 141, uncompressed size: 164, name: secrets/piece_171.png
272157        0x4271D         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_172.png
272283        0x4279B         Zip archive data, at least v2.0 to extract, compressed size: 149, uncompressed size: 177, name: secrets/piece_173.png
272483        0x42863         Zip archive data, at least v2.0 to extract, compressed size: 242, uncompressed size: 271, name: secrets/piece_174.png
272776        0x42988         Zip archive data, at least v2.0 to extract, compressed size: 79, uncompressed size: 102, name: secrets/piece_175.png
272906        0x42A0A         Zip archive data, at least v2.0 to extract, compressed size: 93, uncompressed size: 245, name: secrets/piece_176.png
273050        0x42A9A         Zip archive data, at least v2.0 to extract, compressed size: 96, uncompressed size: 165, name: secrets/piece_177.png
273197        0x42B2D         Zip archive data, at least v2.0 to extract, compressed size: 98, uncompressed size: 166, name: secrets/piece_178.png
273346        0x42BC2         Zip archive data, at least v2.0 to extract, compressed size: 98, uncompressed size: 167, name: secrets/piece_179.png
273495        0x42C57         Zip archive data, at least v2.0 to extract, compressed size: 106, uncompressed size: 120, name: secrets/piece_18.png
273651        0x42CF3         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_180.png
273777        0x42D71         Zip archive data, at least v2.0 to extract, compressed size: 169, uncompressed size: 194, name: secrets/piece_181.png
273997        0x42E4D         Zip archive data, at least v2.0 to extract, compressed size: 126, uncompressed size: 131, name: secrets/piece_182.png
274174        0x42EFE         Zip archive data, at least v2.0 to extract, compressed size: 185, uncompressed size: 219, name: secrets/piece_183.png
274410        0x42FEA         Zip archive data, at least v2.0 to extract, compressed size: 110, uncompressed size: 123, name: secrets/piece_184.png
274571        0x4308B         Zip archive data, at least v2.0 to extract, compressed size: 151, uncompressed size: 249, name: secrets/piece_185.png
274773        0x43155         Zip archive data, at least v2.0 to extract, compressed size: 145, uncompressed size: 153, name: secrets/piece_186.png
274969        0x43219         Zip archive data, at least v2.0 to extract, compressed size: 112, uncompressed size: 261, name: secrets/piece_187.png
275132        0x432BC         Zip archive data, at least v2.0 to extract, compressed size: 139, uncompressed size: 189, name: secrets/piece_188.png
275322        0x4337A         Zip archive data, at least v2.0 to extract, compressed size: 137, uncompressed size: 149, name: secrets/piece_189.png
275510        0x43436         Zip archive data, at least v2.0 to extract, compressed size: 138, uncompressed size: 162, name: secrets/piece_19.png
275698        0x434F2         Zip archive data, at least v2.0 to extract, compressed size: 134, uncompressed size: 198, name: secrets/piece_190.png
275883        0x435AB         Zip archive data, at least v2.0 to extract, compressed size: 154, uncompressed size: 173, name: secrets/piece_191.png
276088        0x43678         Zip archive data, at least v2.0 to extract, compressed size: 139, uncompressed size: 217, name: secrets/piece_192.png
276278        0x43736         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 129, name: secrets/piece_193.png
276452        0x437E4         Zip archive data, at least v2.0 to extract, compressed size: 162, uncompressed size: 216, name: secrets/piece_194.png
276665        0x438B9         Zip archive data, at least v2.0 to extract, compressed size: 174, uncompressed size: 214, name: secrets/piece_195.png
276890        0x4399A         Zip archive data, at least v2.0 to extract, compressed size: 187, uncompressed size: 210, name: secrets/piece_196.png
277128        0x43A88         Zip archive data, at least v2.0 to extract, compressed size: 169, uncompressed size: 204, name: secrets/piece_197.png
277348        0x43B64         Zip archive data, at least v2.0 to extract, compressed size: 180, uncompressed size: 235, name: secrets/piece_198.png
277579        0x43C4B         Zip archive data, at least v2.0 to extract, compressed size: 145, uncompressed size: 176, name: secrets/piece_199.png
277775        0x43D0F         Zip archive data, at least v2.0 to extract, compressed size: 106, uncompressed size: 120, name: secrets/piece_2.png
277930        0x43DAA         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 192, name: secrets/piece_20.png
278072        0x43E38         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_200.png
278198        0x43EB6         Zip archive data, at least v2.0 to extract, compressed size: 138, uncompressed size: 236, name: secrets/piece_201.png
278387        0x43F73         Zip archive data, at least v2.0 to extract, compressed size: 153, uncompressed size: 185, name: secrets/piece_202.png
278591        0x4403F         Zip archive data, at least v2.0 to extract, compressed size: 138, uncompressed size: 208, name: secrets/piece_203.png
278780        0x440FC         Zip archive data, at least v2.0 to extract, compressed size: 108, uncompressed size: 123, name: secrets/piece_204.png
278939        0x4419B         Zip archive data, at least v2.0 to extract, compressed size: 146, uncompressed size: 192, name: secrets/piece_205.png
279136        0x44260         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 160, name: secrets/piece_206.png
279290        0x442FA         Zip archive data, at least v2.0 to extract, compressed size: 125, uncompressed size: 268, name: secrets/piece_207.png
279466        0x443AA         Zip archive data, at least v2.0 to extract, compressed size: 118, uncompressed size: 184, name: secrets/piece_208.png
279635        0x44453         Zip archive data, at least v2.0 to extract, compressed size: 137, uncompressed size: 149, name: secrets/piece_209.png
279823        0x4450F         Zip archive data, at least v2.0 to extract, compressed size: 152, uncompressed size: 180, name: secrets/piece_21.png
280025        0x445D9         Zip archive data, at least v2.0 to extract, compressed size: 140, uncompressed size: 234, name: secrets/piece_210.png
280216        0x44698         Zip archive data, at least v2.0 to extract, compressed size: 108, uncompressed size: 123, name: secrets/piece_211.png
280375        0x44737         Zip archive data, at least v2.0 to extract, compressed size: 242, uncompressed size: 272, name: secrets/piece_212.png
280668        0x4485C         Zip archive data, at least v2.0 to extract, compressed size: 88, uncompressed size: 127, name: secrets/piece_213.png
280807        0x448E7         Zip archive data, at least v2.0 to extract, compressed size: 238, uncompressed size: 292, name: secrets/piece_214.png
281096        0x44A08         Zip archive data, at least v2.0 to extract, compressed size: 140, uncompressed size: 166, name: secrets/piece_215.png
281287        0x44AC7         Zip archive data, at least v2.0 to extract, compressed size: 190, uncompressed size: 255, name: secrets/piece_216.png
281528        0x44BB8         Zip archive data, at least v2.0 to extract, compressed size: 119, uncompressed size: 154, name: secrets/piece_217.png
281698        0x44C62         Zip archive data, at least v2.0 to extract, compressed size: 183, uncompressed size: 243, name: secrets/piece_218.png
281932        0x44D4C         Zip archive data, at least v2.0 to extract, compressed size: 142, uncompressed size: 176, name: secrets/piece_219.png
282125        0x44E0D         Zip archive data, at least v2.0 to extract, compressed size: 109, uncompressed size: 123, name: secrets/piece_22.png
282284        0x44EAC         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 166, name: secrets/piece_220.png
282458        0x44F5A         Zip archive data, at least v2.0 to extract, compressed size: 203, uncompressed size: 266, name: secrets/piece_221.png
282712        0x45058         Zip archive data, at least v2.0 to extract, compressed size: 127, uncompressed size: 193, name: secrets/piece_222.png
282890        0x4510A         Zip archive data, at least v2.0 to extract, compressed size: 113, uncompressed size: 139, name: secrets/piece_223.png
283054        0x451AE         Zip archive data, at least v2.0 to extract, compressed size: 102, uncompressed size: 116, name: secrets/piece_224.png
283207        0x45247         Zip archive data, at least v2.0 to extract, compressed size: 188, uncompressed size: 205, name: secrets/piece_225.png
283446        0x45336         Zip archive data, at least v2.0 to extract, compressed size: 152, uncompressed size: 184, name: secrets/piece_226.png
283649        0x45401         Zip archive data, at least v2.0 to extract, compressed size: 134, uncompressed size: 166, name: secrets/piece_227.png
283834        0x454BA         Zip archive data, at least v2.0 to extract, compressed size: 119, uncompressed size: 181, name: secrets/piece_228.png
284004        0x45564         Zip archive data, at least v2.0 to extract, compressed size: 102, uncompressed size: 116, name: secrets/piece_229.png
284157        0x455FD         Zip archive data, at least v2.0 to extract, compressed size: 122, uncompressed size: 141, name: secrets/piece_23.png
284329        0x456A9         Zip archive data, at least v2.0 to extract, compressed size: 178, uncompressed size: 200, name: secrets/piece_230.png
284558        0x4578E         Zip archive data, at least v2.0 to extract, compressed size: 116, uncompressed size: 144, name: secrets/piece_231.png
284725        0x45835         Zip archive data, at least v2.0 to extract, compressed size: 120, uncompressed size: 177, name: secrets/piece_232.png
284896        0x458E0         Zip archive data, at least v2.0 to extract, compressed size: 144, uncompressed size: 173, name: secrets/piece_233.png
285091        0x459A3         Zip archive data, at least v2.0 to extract, compressed size: 119, uncompressed size: 156, name: secrets/piece_234.png
285261        0x45A4D         Zip archive data, at least v2.0 to extract, compressed size: 150, uncompressed size: 203, name: secrets/piece_235.png
285462        0x45B16         Zip archive data, at least v2.0 to extract, compressed size: 216, uncompressed size: 306, name: secrets/piece_236.png
285729        0x45C21         Zip archive data, at least v2.0 to extract, compressed size: 116, uncompressed size: 158, name: secrets/piece_237.png
285896        0x45CC8         Zip archive data, at least v2.0 to extract, compressed size: 170, uncompressed size: 182, name: secrets/piece_238.png
286117        0x45DA5         Zip archive data, at least v2.0 to extract, compressed size: 98, uncompressed size: 167, name: secrets/piece_239.png
286266        0x45E3A         Zip archive data, at least v2.0 to extract, compressed size: 152, uncompressed size: 183, name: secrets/piece_24.png
286468        0x45F04         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 192, name: secrets/piece_240.png
286611        0x45F93         Zip archive data, at least v2.0 to extract, compressed size: 154, uncompressed size: 161, name: secrets/piece_241.png
286816        0x46060         Zip archive data, at least v2.0 to extract, compressed size: 128, uncompressed size: 149, name: secrets/piece_242.png
286995        0x46113         Zip archive data, at least v2.0 to extract, compressed size: 222, uncompressed size: 250, name: secrets/piece_243.png
287268        0x46224         Zip archive data, at least v2.0 to extract, compressed size: 128, uncompressed size: 133, name: secrets/piece_244.png
287447        0x462D7         Zip archive data, at least v2.0 to extract, compressed size: 186, uncompressed size: 207, name: secrets/piece_245.png
287684        0x463C4         Zip archive data, at least v2.0 to extract, compressed size: 154, uncompressed size: 185, name: secrets/piece_246.png
287889        0x46491         Zip archive data, at least v2.0 to extract, compressed size: 188, uncompressed size: 204, name: secrets/piece_247.png
288128        0x46580         Zip archive data, at least v2.0 to extract, compressed size: 152, uncompressed size: 199, name: secrets/piece_248.png
288331        0x4664B         Zip archive data, at least v2.0 to extract, compressed size: 141, uncompressed size: 176, name: secrets/piece_249.png
288523        0x4670B         Zip archive data, at least v2.0 to extract, compressed size: 116, uncompressed size: 165, name: secrets/piece_25.png
288689        0x467B1         Zip archive data, at least v2.0 to extract, compressed size: 204, uncompressed size: 224, name: secrets/piece_250.png
288944        0x468B0         Zip archive data, at least v2.0 to extract, compressed size: 129, uncompressed size: 146, name: secrets/piece_251.png
289124        0x46964         Zip archive data, at least v2.0 to extract, compressed size: 152, uncompressed size: 158, name: secrets/piece_252.png
289327        0x46A2F         Zip archive data, at least v2.0 to extract, compressed size: 140, uncompressed size: 160, name: secrets/piece_253.png
289518        0x46AEE         Zip archive data, at least v2.0 to extract, compressed size: 180, uncompressed size: 207, name: secrets/piece_254.png
289749        0x46BD5         Zip archive data, at least v2.0 to extract, compressed size: 149, uncompressed size: 154, name: secrets/piece_255.png
289949        0x46C9D         Zip archive data, at least v2.0 to extract, compressed size: 193, uncompressed size: 247, name: secrets/piece_256.png
290193        0x46D91         Zip archive data, at least v2.0 to extract, compressed size: 145, uncompressed size: 175, name: secrets/piece_257.png
290389        0x46E55         Zip archive data, at least v2.0 to extract, compressed size: 216, uncompressed size: 247, name: secrets/piece_258.png
290656        0x46F60         Zip archive data, at least v2.0 to extract, compressed size: 98, uncompressed size: 167, name: secrets/piece_259.png
290805        0x46FF5         Zip archive data, at least v2.0 to extract, compressed size: 140, uncompressed size: 151, name: secrets/piece_26.png
290995        0x470B3         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 192, name: secrets/piece_260.png
291138        0x47142         Zip archive data, at least v2.0 to extract, compressed size: 89, uncompressed size: 223, name: secrets/piece_261.png
291278        0x471CE         Zip archive data, at least v2.0 to extract, compressed size: 114, uncompressed size: 149, name: secrets/piece_262.png
291443        0x47273         Zip archive data, at least v2.0 to extract, compressed size: 144, uncompressed size: 210, name: secrets/piece_263.png
291638        0x47336         Zip archive data, at least v2.0 to extract, compressed size: 170, uncompressed size: 204, name: secrets/piece_264.png
291859        0x47413         Zip archive data, at least v2.0 to extract, compressed size: 105, uncompressed size: 118, name: secrets/piece_265.png
292015        0x474AF         Zip archive data, at least v2.0 to extract, compressed size: 110, uncompressed size: 155, name: secrets/piece_266.png
292176        0x47550         Zip archive data, at least v2.0 to extract, compressed size: 150, uncompressed size: 242, name: secrets/piece_267.png
292377        0x47619         Zip archive data, at least v2.0 to extract, compressed size: 98, uncompressed size: 166, name: secrets/piece_268.png
292526        0x476AE         Zip archive data, at least v2.0 to extract, compressed size: 138, uncompressed size: 207, name: secrets/piece_269.png
292715        0x4776B         Zip archive data, at least v2.0 to extract, compressed size: 167, uncompressed size: 190, name: secrets/piece_27.png
292932        0x47844         Zip archive data, at least v2.0 to extract, compressed size: 136, uncompressed size: 188, name: secrets/piece_270.png
293119        0x478FF         Zip archive data, at least v2.0 to extract, compressed size: 197, uncompressed size: 209, name: secrets/piece_271.png
293367        0x479F7         Zip archive data, at least v2.0 to extract, compressed size: 238, uncompressed size: 252, name: secrets/piece_272.png
293656        0x47B18         Zip archive data, at least v2.0 to extract, compressed size: 79, uncompressed size: 102, name: secrets/piece_273.png
293786        0x47B9A         Zip archive data, at least v2.0 to extract, compressed size: 143, uncompressed size: 151, name: secrets/piece_274.png
293980        0x47C5C         Zip archive data, at least v2.0 to extract, compressed size: 132, uncompressed size: 166, name: secrets/piece_275.png
294163        0x47D13         Zip archive data, at least v2.0 to extract, compressed size: 154, uncompressed size: 203, name: secrets/piece_276.png
294368        0x47DE0         Zip archive data, at least v2.0 to extract, compressed size: 114, uncompressed size: 152, name: secrets/piece_277.png
294533        0x47E85         Zip archive data, at least v2.0 to extract, compressed size: 140, uncompressed size: 207, name: secrets/piece_278.png
294724        0x47F44         Zip archive data, at least v2.0 to extract, compressed size: 140, uncompressed size: 168, name: secrets/piece_279.png
294915        0x48003         Zip archive data, at least v2.0 to extract, compressed size: 130, uncompressed size: 149, name: secrets/piece_28.png
295095        0x480B7         Zip archive data, at least v2.0 to extract, compressed size: 146, uncompressed size: 171, name: secrets/piece_280.png
295292        0x4817C         Zip archive data, at least v2.0 to extract, compressed size: 150, uncompressed size: 176, name: secrets/piece_281.png
295493        0x48245         Zip archive data, at least v2.0 to extract, compressed size: 146, uncompressed size: 154, name: secrets/piece_282.png
295690        0x4830A         Zip archive data, at least v2.0 to extract, compressed size: 170, uncompressed size: 177, name: secrets/piece_283.png
295911        0x483E7         Zip archive data, at least v2.0 to extract, compressed size: 140, uncompressed size: 148, name: secrets/piece_284.png
296102        0x484A6         Zip archive data, at least v2.0 to extract, compressed size: 199, uncompressed size: 221, name: secrets/piece_285.png
296352        0x485A0         Zip archive data, at least v2.0 to extract, compressed size: 79, uncompressed size: 102, name: secrets/piece_286.png
296482        0x48622         Zip archive data, at least v2.0 to extract, compressed size: 132, uncompressed size: 191, name: secrets/piece_287.png
296665        0x486D9         Zip archive data, at least v2.0 to extract, compressed size: 174, uncompressed size: 210, name: secrets/piece_288.png
296890        0x487BA         Zip archive data, at least v2.0 to extract, compressed size: 181, uncompressed size: 191, name: secrets/piece_289.png
297122        0x488A2         Zip archive data, at least v2.0 to extract, compressed size: 133, uncompressed size: 139, name: secrets/piece_29.png
297305        0x48959         Zip archive data, at least v2.0 to extract, compressed size: 174, uncompressed size: 242, name: secrets/piece_290.png
297530        0x48A3A         Zip archive data, at least v2.0 to extract, compressed size: 143, uncompressed size: 170, name: secrets/piece_291.png
297724        0x48AFC         Zip archive data, at least v2.0 to extract, compressed size: 185, uncompressed size: 217, name: secrets/piece_292.png
297960        0x48BE8         Zip archive data, at least v2.0 to extract, compressed size: 112, uncompressed size: 136, name: secrets/piece_293.png
298123        0x48C8B         Zip archive data, at least v2.0 to extract, compressed size: 167, uncompressed size: 197, name: secrets/piece_294.png
298341        0x48D65         Zip archive data, at least v2.0 to extract, compressed size: 143, uncompressed size: 152, name: secrets/piece_295.png
298535        0x48E27         Zip archive data, at least v2.0 to extract, compressed size: 168, uncompressed size: 265, name: secrets/piece_296.png
298754        0x48F02         Zip archive data, at least v2.0 to extract, compressed size: 173, uncompressed size: 194, name: secrets/piece_297.png
298978        0x48FE2         Zip archive data, at least v2.0 to extract, compressed size: 162, uncompressed size: 196, name: secrets/piece_298.png
299191        0x490B7         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_299.png
299317        0x49135         Zip archive data, at least v2.0 to extract, compressed size: 106, uncompressed size: 120, name: secrets/piece_3.png
299472        0x491D0         Zip archive data, at least v2.0 to extract, compressed size: 188, uncompressed size: 242, name: secrets/piece_30.png
299710        0x492BE         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 192, name: secrets/piece_300.png
299853        0x4934D         Zip archive data, at least v2.0 to extract, compressed size: 115, uncompressed size: 153, name: secrets/piece_301.png
300019        0x493F3         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 118, name: secrets/piece_302.png
300173        0x4948D         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 118, name: secrets/piece_303.png
300327        0x49527         Zip archive data, at least v2.0 to extract, compressed size: 133, uncompressed size: 167, name: secrets/piece_304.png
300511        0x495DF         Zip archive data, at least v2.0 to extract, compressed size: 93, uncompressed size: 246, name: secrets/piece_305.png
300655        0x4966F         Zip archive data, at least v2.0 to extract, compressed size: 79, uncompressed size: 102, name: secrets/piece_306.png
300785        0x496F1         Zip archive data, at least v2.0 to extract, compressed size: 112, uncompressed size: 158, name: secrets/piece_307.png
300948        0x49794         Zip archive data, at least v2.0 to extract, compressed size: 122, uncompressed size: 174, name: secrets/piece_308.png
301121        0x49841         Zip archive data, at least v2.0 to extract, compressed size: 151, uncompressed size: 253, name: secrets/piece_309.png
301323        0x4990B         Zip archive data, at least v2.0 to extract, compressed size: 112, uncompressed size: 118, name: secrets/piece_31.png
301485        0x499AD         Zip archive data, at least v2.0 to extract, compressed size: 168, uncompressed size: 247, name: secrets/piece_310.png
301704        0x49A88         Zip archive data, at least v2.0 to extract, compressed size: 195, uncompressed size: 208, name: secrets/piece_311.png
301950        0x49B7E         Zip archive data, at least v2.0 to extract, compressed size: 180, uncompressed size: 209, name: secrets/piece_312.png
302181        0x49C65         Zip archive data, at least v2.0 to extract, compressed size: 132, uncompressed size: 162, name: secrets/piece_313.png
302364        0x49D1C         Zip archive data, at least v2.0 to extract, compressed size: 126, uncompressed size: 222, name: secrets/piece_314.png
302541        0x49DCD         Zip archive data, at least v2.0 to extract, compressed size: 141, uncompressed size: 162, name: secrets/piece_315.png
302733        0x49E8D         Zip archive data, at least v2.0 to extract, compressed size: 124, uncompressed size: 249, name: secrets/piece_316.png
302908        0x49F3C         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 118, name: secrets/piece_317.png
303062        0x49FD6         Zip archive data, at least v2.0 to extract, compressed size: 180, uncompressed size: 191, name: secrets/piece_318.png
303293        0x4A0BD         Zip archive data, at least v2.0 to extract, compressed size: 149, uncompressed size: 170, name: secrets/piece_319.png
303493        0x4A185         Zip archive data, at least v2.0 to extract, compressed size: 181, uncompressed size: 214, name: secrets/piece_32.png
303724        0x4A26C         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 192, name: secrets/piece_320.png
303867        0x4A2FB         Zip archive data, at least v2.0 to extract, compressed size: 115, uncompressed size: 226, name: secrets/piece_321.png
304033        0x4A3A1         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 110, name: secrets/piece_322.png
304176        0x4A430         Zip archive data, at least v2.0 to extract, compressed size: 132, uncompressed size: 166, name: secrets/piece_323.png
304359        0x4A4E7         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 188, name: secrets/piece_324.png
304533        0x4A595         Zip archive data, at least v2.0 to extract, compressed size: 134, uncompressed size: 191, name: secrets/piece_325.png
304718        0x4A64E         Zip archive data, at least v2.0 to extract, compressed size: 148, uncompressed size: 169, name: secrets/piece_326.png
304917        0x4A715         Zip archive data, at least v2.0 to extract, compressed size: 188, uncompressed size: 190, name: secrets/piece_327.png
305156        0x4A804         Zip archive data, at least v2.0 to extract, compressed size: 130, uncompressed size: 145, name: secrets/piece_328.png
305337        0x4A8B9         Zip archive data, at least v2.0 to extract, compressed size: 156, uncompressed size: 182, name: secrets/piece_329.png
305544        0x4A988         Zip archive data, at least v2.0 to extract, compressed size: 85, uncompressed size: 121, name: secrets/piece_33.png
305679        0x4AA0F         Zip archive data, at least v2.0 to extract, compressed size: 143, uncompressed size: 173, name: secrets/piece_330.png
305873        0x4AAD1         Zip archive data, at least v2.0 to extract, compressed size: 110, uncompressed size: 126, name: secrets/piece_331.png
306034        0x4AB72         Zip archive data, at least v2.0 to extract, compressed size: 206, uncompressed size: 243, name: secrets/piece_332.png
306291        0x4AC73         Zip archive data, at least v2.0 to extract, compressed size: 96, uncompressed size: 112, name: secrets/piece_333.png
306438        0x4AD06         Zip archive data, at least v2.0 to extract, compressed size: 194, uncompressed size: 199, name: secrets/piece_334.png
306683        0x4ADFB         Zip archive data, at least v2.0 to extract, compressed size: 112, uncompressed size: 118, name: secrets/piece_335.png
306846        0x4AE9E         Zip archive data, at least v2.0 to extract, compressed size: 182, uncompressed size: 206, name: secrets/piece_336.png
307079        0x4AF87         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_337.png
307205        0x4B005         Zip archive data, at least v2.0 to extract, compressed size: 192, uncompressed size: 267, name: secrets/piece_338.png
307448        0x4B0F8         Zip archive data, at least v2.0 to extract, compressed size: 148, uncompressed size: 171, name: secrets/piece_339.png
307647        0x4B1BF         Zip archive data, at least v2.0 to extract, compressed size: 127, uncompressed size: 216, name: secrets/piece_34.png
307824        0x4B270         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 192, name: secrets/piece_340.png
307967        0x4B2FF         Zip archive data, at least v2.0 to extract, compressed size: 89, uncompressed size: 223, name: secrets/piece_341.png
308107        0x4B38B         Zip archive data, at least v2.0 to extract, compressed size: 79, uncompressed size: 102, name: secrets/piece_342.png
308237        0x4B40D         Zip archive data, at least v2.0 to extract, compressed size: 110, uncompressed size: 157, name: secrets/piece_343.png
308398        0x4B4AE         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 188, name: secrets/piece_344.png
308572        0x4B55C         Zip archive data, at least v2.0 to extract, compressed size: 116, uncompressed size: 165, name: secrets/piece_345.png
308739        0x4B603         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_346.png
308865        0x4B681         Zip archive data, at least v2.0 to extract, compressed size: 127, uncompressed size: 224, name: secrets/piece_347.png
309043        0x4B733         Zip archive data, at least v2.0 to extract, compressed size: 107, uncompressed size: 117, name: secrets/piece_348.png
309201        0x4B7D1         Zip archive data, at least v2.0 to extract, compressed size: 157, uncompressed size: 221, name: secrets/piece_349.png
309409        0x4B8A1         Zip archive data, at least v2.0 to extract, compressed size: 104, uncompressed size: 158, name: secrets/piece_35.png
309563        0x4B93B         Zip archive data, at least v2.0 to extract, compressed size: 104, uncompressed size: 119, name: secrets/piece_350.png
309718        0x4B9D6         Zip archive data, at least v2.0 to extract, compressed size: 129, uncompressed size: 174, name: secrets/piece_351.png
309898        0x4BA8A         Zip archive data, at least v2.0 to extract, compressed size: 105, uncompressed size: 213, name: secrets/piece_352.png
310054        0x4BB26         Zip archive data, at least v2.0 to extract, compressed size: 139, uncompressed size: 171, name: secrets/piece_353.png
310244        0x4BBE4         Zip archive data, at least v2.0 to extract, compressed size: 179, uncompressed size: 245, name: secrets/piece_354.png
310474        0x4BCCA         Zip archive data, at least v2.0 to extract, compressed size: 107, uncompressed size: 117, name: secrets/piece_355.png
310632        0x4BD68         Zip archive data, at least v2.0 to extract, compressed size: 157, uncompressed size: 170, name: secrets/piece_356.png
310840        0x4BE38         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_357.png
310966        0x4BEB6         Zip archive data, at least v2.0 to extract, compressed size: 216, uncompressed size: 266, name: secrets/piece_358.png
311233        0x4BFC1         Zip archive data, at least v2.0 to extract, compressed size: 145, uncompressed size: 166, name: secrets/piece_359.png
311429        0x4C085         Zip archive data, at least v2.0 to extract, compressed size: 119, uncompressed size: 139, name: secrets/piece_36.png
311598        0x4C12E         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 192, name: secrets/piece_360.png
311741        0x4C1BD         Zip archive data, at least v2.0 to extract, compressed size: 157, uncompressed size: 180, name: secrets/piece_361.png
311949        0x4C28D         Zip archive data, at least v2.0 to extract, compressed size: 112, uncompressed size: 124, name: secrets/piece_362.png
312112        0x4C330         Zip archive data, at least v2.0 to extract, compressed size: 121, uncompressed size: 139, name: secrets/piece_363.png
312284        0x4C3DC         Zip archive data, at least v2.0 to extract, compressed size: 152, uncompressed size: 182, name: secrets/piece_364.png
312487        0x4C4A7         Zip archive data, at least v2.0 to extract, compressed size: 116, uncompressed size: 251, name: secrets/piece_365.png
312654        0x4C54E         Zip archive data, at least v2.0 to extract, compressed size: 89, uncompressed size: 108, name: secrets/piece_366.png
312794        0x4C5DA         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 122, name: secrets/piece_367.png
312948        0x4C674         Zip archive data, at least v2.0 to extract, compressed size: 151, uncompressed size: 168, name: secrets/piece_368.png
313150        0x4C73E         Zip archive data, at least v2.0 to extract, compressed size: 164, uncompressed size: 172, name: secrets/piece_369.png
313365        0x4C815         Zip archive data, at least v2.0 to extract, compressed size: 109, uncompressed size: 123, name: secrets/piece_37.png
313524        0x4C8B4         Zip archive data, at least v2.0 to extract, compressed size: 142, uncompressed size: 168, name: secrets/piece_370.png
313717        0x4C975         Zip archive data, at least v2.0 to extract, compressed size: 124, uncompressed size: 142, name: secrets/piece_371.png
313892        0x4CA24         Zip archive data, at least v2.0 to extract, compressed size: 146, uncompressed size: 154, name: secrets/piece_372.png
314089        0x4CAE9         Zip archive data, at least v2.0 to extract, compressed size: 141, uncompressed size: 168, name: secrets/piece_373.png
314281        0x4CBA9         Zip archive data, at least v2.0 to extract, compressed size: 166, uncompressed size: 267, name: secrets/piece_374.png
314498        0x4CC82         Zip archive data, at least v2.0 to extract, compressed size: 168, uncompressed size: 188, name: secrets/piece_375.png
314717        0x4CD5D         Zip archive data, at least v2.0 to extract, compressed size: 186, uncompressed size: 262, name: secrets/piece_376.png
314954        0x4CE4A         Zip archive data, at least v2.0 to extract, compressed size: 108, uncompressed size: 144, name: secrets/piece_377.png
315113        0x4CEE9         Zip archive data, at least v2.0 to extract, compressed size: 171, uncompressed size: 261, name: secrets/piece_378.png
315335        0x4CFC7         Zip archive data, at least v2.0 to extract, compressed size: 140, uncompressed size: 185, name: secrets/piece_379.png
315526        0x4D086         Zip archive data, at least v2.0 to extract, compressed size: 136, uncompressed size: 208, name: secrets/piece_38.png
315712        0x4D140         Zip archive data, at least v2.0 to extract, compressed size: 119, uncompressed size: 162, name: secrets/piece_380.png
315882        0x4D1EA         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 120, name: secrets/piece_381.png
316036        0x4D284         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 120, name: secrets/piece_382.png
316190        0x4D31E         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 120, name: secrets/piece_383.png
316344        0x4D3B8         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 120, name: secrets/piece_384.png
316498        0x4D452         Zip archive data, at least v2.0 to extract, compressed size: 192, uncompressed size: 200, name: secrets/piece_385.png
316741        0x4D545         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 120, name: secrets/piece_386.png
316895        0x4D5DF         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 120, name: secrets/piece_387.png
317049        0x4D679         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 120, name: secrets/piece_388.png
317203        0x4D713         Zip archive data, at least v2.0 to extract, compressed size: 135, uncompressed size: 144, name: secrets/piece_389.png
317389        0x4D7CD         Zip archive data, at least v2.0 to extract, compressed size: 98, uncompressed size: 167, name: secrets/piece_39.png
317537        0x4D861         Zip archive data, at least v2.0 to extract, compressed size: 116, uncompressed size: 161, name: secrets/piece_390.png
317704        0x4D908         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 120, name: secrets/piece_391.png
317858        0x4D9A2         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 120, name: secrets/piece_392.png
318012        0x4DA3C         Zip archive data, at least v2.0 to extract, compressed size: 135, uncompressed size: 158, name: secrets/piece_393.png
318198        0x4DAF6         Zip archive data, at least v2.0 to extract, compressed size: 119, uncompressed size: 161, name: secrets/piece_394.png
318368        0x4DBA0         Zip archive data, at least v2.0 to extract, compressed size: 103, uncompressed size: 120, name: secrets/piece_395.png
318522        0x4DC3A         Zip archive data, at least v2.0 to extract, compressed size: 171, uncompressed size: 201, name: secrets/piece_396.png
318744        0x4DD18         Zip archive data, at least v2.0 to extract, compressed size: 138, uncompressed size: 162, name: secrets/piece_397.png
318933        0x4DDD5         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_398.png
319059        0x4DE53         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_399.png
319185        0x4DED1         Zip archive data, at least v2.0 to extract, compressed size: 106, uncompressed size: 120, name: secrets/piece_4.png
319340        0x4DF6C         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 192, name: secrets/piece_40.png
319482        0x4DFFA         Zip archive data, at least v2.0 to extract, compressed size: 89, uncompressed size: 223, name: secrets/piece_41.png
319621        0x4E085         Zip archive data, at least v2.0 to extract, compressed size: 79, uncompressed size: 102, name: secrets/piece_42.png
319750        0x4E106         Zip archive data, at least v2.0 to extract, compressed size: 110, uncompressed size: 157, name: secrets/piece_43.png
319910        0x4E1A6         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 188, name: secrets/piece_44.png
320083        0x4E253         Zip archive data, at least v2.0 to extract, compressed size: 124, uncompressed size: 217, name: secrets/piece_45.png
320257        0x4E301         Zip archive data, at least v2.0 to extract, compressed size: 155, uncompressed size: 185, name: secrets/piece_46.png
320462        0x4E3CE         Zip archive data, at least v2.0 to extract, compressed size: 128, uncompressed size: 150, name: secrets/piece_47.png
320640        0x4E480         Zip archive data, at least v2.0 to extract, compressed size: 98, uncompressed size: 166, name: secrets/piece_48.png
320788        0x4E514         Zip archive data, at least v2.0 to extract, compressed size: 127, uncompressed size: 247, name: secrets/piece_49.png
320965        0x4E5C5         Zip archive data, at least v2.0 to extract, compressed size: 110, uncompressed size: 164, name: secrets/piece_5.png
321124        0x4E664         Zip archive data, at least v2.0 to extract, compressed size: 143, uncompressed size: 174, name: secrets/piece_50.png
321317        0x4E725         Zip archive data, at least v2.0 to extract, compressed size: 124, uncompressed size: 168, name: secrets/piece_51.png
321491        0x4E7D3         Zip archive data, at least v2.0 to extract, compressed size: 189, uncompressed size: 218, name: secrets/piece_52.png
321730        0x4E8C2         Zip archive data, at least v2.0 to extract, compressed size: 79, uncompressed size: 102, name: secrets/piece_53.png
321859        0x4E943         Zip archive data, at least v2.0 to extract, compressed size: 93, uncompressed size: 246, name: secrets/piece_54.png
322002        0x4E9D2         Zip archive data, at least v2.0 to extract, compressed size: 81, uncompressed size: 160, name: secrets/piece_55.png
322133        0x4EA55         Zip archive data, at least v2.0 to extract, compressed size: 101, uncompressed size: 185, name: secrets/piece_56.png
322284        0x4EAEC         Zip archive data, at least v2.0 to extract, compressed size: 79, uncompressed size: 102, name: secrets/piece_57.png
322413        0x4EB6D         Zip archive data, at least v2.0 to extract, compressed size: 149, uncompressed size: 242, name: secrets/piece_58.png
322612        0x4EC34         Zip archive data, at least v2.0 to extract, compressed size: 98, uncompressed size: 167, name: secrets/piece_59.png
322760        0x4ECC8         Zip archive data, at least v2.0 to extract, compressed size: 119, uncompressed size: 149, name: secrets/piece_6.png
322928        0x4ED70         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 192, name: secrets/piece_60.png
323070        0x4EDFE         Zip archive data, at least v2.0 to extract, compressed size: 110, uncompressed size: 226, name: secrets/piece_61.png
323230        0x4EE9E         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 110, name: secrets/piece_62.png
323372        0x4EF2C         Zip archive data, at least v2.0 to extract, compressed size: 132, uncompressed size: 166, name: secrets/piece_63.png
323554        0x4EFE2         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 188, name: secrets/piece_64.png
323727        0x4F08F         Zip archive data, at least v2.0 to extract, compressed size: 111, uncompressed size: 246, name: secrets/piece_65.png
323888        0x4F130         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 170, name: secrets/piece_66.png
324061        0x4F1DD         Zip archive data, at least v2.0 to extract, compressed size: 146, uncompressed size: 253, name: secrets/piece_67.png
324257        0x4F2A1         Zip archive data, at least v2.0 to extract, compressed size: 189, uncompressed size: 213, name: secrets/piece_68.png
324496        0x4F390         Zip archive data, at least v2.0 to extract, compressed size: 171, uncompressed size: 199, name: secrets/piece_69.png
324717        0x4F46D         Zip archive data, at least v2.0 to extract, compressed size: 106, uncompressed size: 120, name: secrets/piece_7.png
324872        0x4F508         Zip archive data, at least v2.0 to extract, compressed size: 118, uncompressed size: 148, name: secrets/piece_70.png
325040        0x4F5B0         Zip archive data, at least v2.0 to extract, compressed size: 145, uncompressed size: 170, name: secrets/piece_71.png
325235        0x4F673         Zip archive data, at least v2.0 to extract, compressed size: 171, uncompressed size: 218, name: secrets/piece_72.png
325456        0x4F750         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 110, name: secrets/piece_73.png
325598        0x4F7DE         Zip archive data, at least v2.0 to extract, compressed size: 188, uncompressed size: 259, name: secrets/piece_74.png
325836        0x4F8CC         Zip archive data, at least v2.0 to extract, compressed size: 81, uncompressed size: 160, name: secrets/piece_75.png
325967        0x4F94F         Zip archive data, at least v2.0 to extract, compressed size: 119, uncompressed size: 188, name: secrets/piece_76.png
326136        0x4F9F8         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 110, name: secrets/piece_77.png
326278        0x4FA86         Zip archive data, at least v2.0 to extract, compressed size: 179, uncompressed size: 251, name: secrets/piece_78.png
326507        0x4FB6B         Zip archive data, at least v2.0 to extract, compressed size: 98, uncompressed size: 167, name: secrets/piece_79.png
326655        0x4FBFF         Zip archive data, at least v2.0 to extract, compressed size: 140, uncompressed size: 164, name: secrets/piece_8.png
326844        0x4FCBC         Zip archive data, at least v2.0 to extract, compressed size: 92, uncompressed size: 192, name: secrets/piece_80.png
326986        0x4FD4A         Zip archive data, at least v2.0 to extract, compressed size: 116, uncompressed size: 153, name: secrets/piece_81.png
327152        0x4FDF0         Zip archive data, at least v2.0 to extract, compressed size: 105, uncompressed size: 118, name: secrets/piece_82.png
327307        0x4FE8B         Zip archive data, at least v2.0 to extract, compressed size: 105, uncompressed size: 118, name: secrets/piece_83.png
327462        0x4FF26         Zip archive data, at least v2.0 to extract, compressed size: 132, uncompressed size: 166, name: secrets/piece_84.png
327644        0x4FFDC         Zip archive data, at least v2.0 to extract, compressed size: 125, uncompressed size: 222, name: secrets/piece_85.png
327819        0x5008B         Zip archive data, at least v2.0 to extract, compressed size: 156, uncompressed size: 184, name: secrets/piece_86.png
328025        0x50159         Zip archive data, at least v2.0 to extract, compressed size: 194, uncompressed size: 231, name: secrets/piece_87.png
328269        0x5024D         Zip archive data, at least v2.0 to extract, compressed size: 121, uncompressed size: 171, name: secrets/piece_88.png
328440        0x502F8         Zip archive data, at least v2.0 to extract, compressed size: 205, uncompressed size: 214, name: secrets/piece_89.png
328695        0x503F7         Zip archive data, at least v2.0 to extract, compressed size: 75, uncompressed size: 117, name: secrets/piece_9.png
328819        0x50473         Zip archive data, at least v2.0 to extract, compressed size: 136, uncompressed size: 187, name: secrets/piece_90.png
329005        0x5052D         Zip archive data, at least v2.0 to extract, compressed size: 170, uncompressed size: 209, name: secrets/piece_91.png
329225        0x50609         Zip archive data, at least v2.0 to extract, compressed size: 187, uncompressed size: 219, name: secrets/piece_92.png
329462        0x506F6         Zip archive data, at least v2.0 to extract, compressed size: 144, uncompressed size: 168, name: secrets/piece_93.png
329656        0x507B8         Zip archive data, at least v2.0 to extract, compressed size: 185, uncompressed size: 245, name: secrets/piece_94.png
329891        0x508A3         Zip archive data, at least v2.0 to extract, compressed size: 123, uncompressed size: 149, name: secrets/piece_95.png
330064        0x50950         Zip archive data, at least v2.0 to extract, compressed size: 105, uncompressed size: 118, name: secrets/piece_96.png
330219        0x509EB         Zip archive data, at least v2.0 to extract, compressed size: 105, uncompressed size: 118, name: secrets/piece_97.png
330374        0x50A86         Zip archive data, at least v2.0 to extract, compressed size: 116, uncompressed size: 171, name: secrets/piece_98.png
330540        0x50B2C         Zip archive data, at least v2.0 to extract, compressed size: 98, uncompressed size: 167, name: secrets/piece_99.png
371868        0x5AC9C         End of Zip archive, footer length: 22
```
- Khi mà xem vài ảnh đầu thì mình chắc chắn rằng nó sẽ là 1 Mã QR code, nhưng vấn đề là ta cần ghép 400 cái ảnh lại thôi.

![1713377044421](image/writeup/1713377044421.png) ![1713377064085](image/writeup/1713377064085.png) ![1713377076874](image/writeup/1713377076874.png) ![1713377105376](image/writeup/1713377105376.png) ![1713377108792](image/writeup/1713377108792.png)![1713377110947](image/writeup/1713377110947.png)

- Mình có nhờ Chat để có thể giải quyết vấn đề này và đây là script :
```
from PIL import Image

# Kích thước của mỗi tấm ảnh 
piece_width = 20
piece_height = 20

# Kích thước của ảnh QR hoàn chỉnh (400x400 pixel)
qr_width = 400
qr_height = 400

# Tạo một ảnh mới để chứa tất cả các tấm ảnh
qr_image = Image.new('RGB', (qr_width, qr_height))

# Lặp qua từng tấm ảnh và ghép vào ảnh QR
for i in range(400):
    # Load tấm ảnh
    piece_path = f'piece_{i}.png'
    piece_image = Image.open(piece_path)
    
    # Tính toán vị trí để ghép tấm ảnh vào ảnh QR
    row = i // 20  # Số dòng, mỗi dòng có 20 tấm ảnh
    col = i % 20   # Số cột
    
    # Tính toán vị trí bắt đầu của tấm ảnh trong ảnh QR
    x_offset = col * piece_width
    y_offset = row * piece_height
    
    # Ghép tấm ảnh vào ảnh QR
    qr_image.paste(piece_image, (x_offset, y_offset))

# Lưu ảnh QR hoàn chỉnh
qr_image.save('qr_code.png')

print("Ghép ảnh QR thành công!")
```
- Sau khi ghép lại thì được 1 cái mã QR hoàn chỉnh như sau , quét nó thì ta có flag.
![1713377205217](image/writeup/1713377205217.png)
- *`FLAG: shctf{s0_l0ng_4nd_th4nks_f0r_4ll_th3_flags}`*.
### II. A Window into Space.
- Chall này cho ta 1 file `.pcapng` , mình vào wireshark mở nó ra thì thấy rất nhiều TCP nên quyết định filter mỗi tcp.
![1713377441351](image/writeup/1713377441351.png)
- Sau khi check 1 vài dòng thì mình nhận ra được điều khả nghi đó là ở byte này, flag được dấu ở byte này việc của ta là ghép nó lại là xong, hãy xài filter này `tcp && frame.len == 44 && tcp.window_size_value != 0` để xem tiện hơn.
![1713377653885](image/writeup/1713377653885.png)
- Để leak dữ liệu này ra mình sẽ xai `Tshark` với command sau:
```
$ tshark -r space.pcapng -Y "tcp && frame.len == 44 && tcp.window_size_value != 0" -T fields -e "tcp.window_size_value"

115
104
99
116
102
123
49
95
115
104
48
117
108
100
95
116
114
121
95
104
49
100
49
110
103
95
49
110
95
116
104
51
95
99
104
51
99
107
115
117
109
95
110
51
120
116
95
116
49
109
101
95
48
56
49
55
125
```
- Data trên là dạng Dec vứt lên `kt.gy` là ra flag.
![1713377818138](image/writeup/1713377818138.png)
- *`FLAG: shctf{1_sh0uld_try_h1d1ng_1n_th3_ch3cksum_n3xt_t1me_0817}`*.
### III. Space Frisbee.
- Chall này cho mình 1 file âm thanh, thế là mình vứt nó ngay vào `Audacity` thì thấy cái này.
![1713377911290](image/writeup/1713377911290.png)
- Khỏi lói cũng biết nó sẽ là Morse hoặc là Binary thui , nhưng mà thực sự Nếu xét là mã Morse thì sẽ rất khó xác định, Vậy chỉ có thể là Binary và đây sẽ là cách xác định :
![1713378245059](image/writeup/1713378245059.png)
- Với `Khoản trắng = '0'` cái kia là ngược lại thì Giả dụ như sau , Khoản trắng đầu tiên sẽ là 1 số 0, và phân Ô Xanh kế bên nó có độ dài gấp 3 lần ô trắng nó sẽ tương đương với 3 số 1, Cứ như thế Khoản trắng tiếp theo sẽ tương ứng với 2 số 0. 
- Sau khi Tập hợp đủ dữ liệu sẽ như thế này :
![1713378457678](image/writeup/1713378457678.png)
- *`FLAG: shctf{1ts_d3f1n1t3ly_n0t_4_sp0rt}`*.