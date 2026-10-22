# 最终采用配音清单 · 导出v6

以下49个脚本行使用配置显式选择的WAV；旧候选不删除。Xiaomi MiMo mimo-v2.5-tts，旁白Mia、小新Milo、风间Dean、妮妮Mia。风格按每行meta与角色库记录。

机器格式/音量检查已执行；ASR复核记录另存 audio/asr-review-v4.json；49/49在忽略标点、大小写、数字书写及neighbours/neighbors差异后逐词匹配，无剩余机器转写差异。逐句完整人工听检仍待完成。

| 行 | 角色/voice | 采用文件 | 秒数 | 峰值dBFS | SHA-256 |
| --- | --- | --- | --- | --- | --- |
| line-001 | narrator/Mia | `audio/tts/line-001-v3.wav` | 3.040 | -5.46 | `c9b96507e421f5035e3762cd10f77f45bcec7c1e035c8ad61fb4d442c87ecb22` |
| line-002 | narrator/Mia | `audio/tts/line-002-v3.wav` | 2.880 | -7.49 | `2bd3df47cecf5010aff77afc87dbb6c757338ec93cb32f63e237c7b80d19a566` |
| line-003 | shinchan/Milo | `audio/tts/line-003-v1.wav` | 2.400 | -2.53 | `e7f71d5cc1f07864eaaef2f71c1f3b5b06b1541c20cf4cb3f8808397045d9998` |
| line-004 | nene/Mia | `audio/tts/line-004-v1.wav` | 2.400 | -3.26 | `b9b6e6a571a8c030df0ef1e43c627aa00ba2af45afc70365610fd60a836d4c0b` |
| line-005 | kazama/Dean | `audio/tts/line-005-v1.wav` | 4.800 | -4.68 | `e50bd6029aac1e94a12666997c652cbb05fea59aefba1bcfc145a6afc1f0870d` |
| line-006 | shinchan/Milo | `audio/tts/line-006-v1.wav` | 2.720 | -0.09 | `b9dacd8dac46b9135a648404524e4030e23d0df2ab48c62359295fb71d62e081` |
| line-007 | shinchan/Milo | `audio/tts/line-007-v2.wav` | 2.560 | -5.76 | `00d6d06c8a52eaa4396c43250fa7b7508160bdaf272c5ea12b34b5b4d1307037` |
| line-008 | shinchan/Milo | `audio/tts/line-008-v1.wav` | 2.880 | -0.09 | `f26ad3b9f61a22ac82231aa1f1259be54983f8594e3522dd7b6dea6fbc5969cf` |
| line-009 | nene/Mia | `audio/tts/line-009-v1.wav` | 2.080 | -6.31 | `db79bdf1bd34788d84521823454de9da0189660c83252a58551851833a2e5224` |
| line-010 | shinchan/Milo | `audio/tts/line-010-v2.wav` | 3.200 | -1.98 | `b4efef9a8c4f43cdd3a9a06dd56ac3e3dbc922412cbb24aeb9d69eba2326c924` |
| line-011 | kazama/Dean | `audio/tts/line-011-v1.wav` | 3.360 | -0.09 | `f51fb58368359232bf9e5bdc810a5276a9fbf4f1c4e8a52d5d31f0343ead666b` |
| line-012 | narrator/Mia | `audio/tts/line-012-v3.wav` | 6.080 | -1.21 | `671b8c069030c76fd0858729189f75b2398d25360c5856b66846f6d9aca2c10c` |
| line-013 | shinchan/Milo | `audio/tts/line-013-v1.wav` | 2.400 | -10.63 | `7e52ddde34f7685e5f2bae9e91728e6c104a90cd9321b4d668af5d11b2e09e1c` |
| line-014 | shinchan/Milo | `audio/tts/line-014-v1.wav` | 2.880 | -0.09 | `59219aabb7c53c21617fd032c209809b533091fa27ff3cafa2f767de0ca033c7` |
| line-015 | nene/Mia | `audio/tts/line-015-v1.wav` | 2.880 | -5.20 | `959645569d3a9840471ec125e0e2b757075192b0cf27e952210269d503ab142d` |
| line-016 | narrator/Mia | `audio/tts/line-016-v4.wav` | 5.440 | -0.09 | `e16ea3a9194d6d8bbf82369449c8c13caa6d899436d7d27a3f51b3b0c08fd086` |
| line-017 | nene/Mia | `audio/tts/line-017-v1.wav` | 5.440 | -3.10 | `b6fe8af3bb130223ec389b5a84c31171ed189220fafeb28d9907112823358cf2` |
| line-018 | kazama/Dean | `audio/tts/line-018-v1.wav` | 3.520 | -4.87 | `a6016c18646ac51ed9fc6f5c1ae5cdccc386868f37dba2763b51025bcf31793e` |
| line-019 | kazama/Dean | `audio/tts/line-019-v1.wav` | 4.160 | -8.08 | `d177e0a879dd40e05a21825509985dbf5c4a7cd9eb5553ae788f4d5c8c02d977` |
| line-020 | shinchan/Milo | `audio/tts/line-020-v1.wav` | 4.000 | -3.09 | `d13065d832e2d4b2ee66577051178544db67f13ba488c0516066831ccd3c5a32` |
| line-021 | kazama/Dean | `audio/tts/line-021-v3.wav` | 4.000 | -3.10 | `febbc3cb71990ebc24c14e68006aa40b114b15ca44432513163cda65cb51ca4a` |
| line-022 | nene/Mia | `audio/tts/line-022-v1.wav` | 3.680 | -3.59 | `88b8ec9bf9e44df1d4d2cec5146f5476811f2c610789c25d6a0b275353e376ac` |
| line-023 | kazama/Dean | `audio/tts/line-023-v1.wav` | 4.000 | -4.38 | `d77bf693121a6e8c0081f7a1f1044b4ace77e7d88f8ab90f8222fe5ac6ff385b` |
| line-024 | shinchan/Milo | `audio/tts/line-024-v1.wav` | 3.680 | -0.09 | `64b4d59b9d6503be1188205c193a8cb7b4017e7e0b48ae8488ef8af4e5617b77` |
| line-025 | narrator/Mia | `audio/tts/line-025-v3.wav` | 1.120 | -5.58 | `1f17cd800e5cd7e019a333411a233885e4e4797265f223d17a987c4165938c8b` |
| line-026 | kazama/Dean | `audio/tts/line-026-v1.wav` | 3.360 | -3.84 | `575f2a99163acc7487162d5e685d3369c8dabce26823c237d3425129db914a4c` |
| line-027 | kazama/Dean | `audio/tts/line-027-v1.wav` | 3.840 | -2.10 | `1e023a01dffb0c1642e01710e16bd0c360e1b571e07d38a402589a084e2e83cf` |
| line-028 | narrator/Mia | `audio/tts/line-028-v3.wav` | 1.440 | -2.44 | `42a5dafabc117d2460b35ce2310243c8b18d9df3c80cbf75e1465490482b3a43` |
| line-029 | nene/Mia | `audio/tts/line-029-v1.wav` | 2.720 | -7.92 | `33aac39813373ce2a03b17cd216454bea1c91f2475eb2080312253becea991b1` |
| line-030 | nene/Mia | `audio/tts/line-030-v2.wav` | 1.760 | -1.50 | `493689b3fa8532bcf3fcd0e1dea06e04f7f69d95e993af4e784d9cde38584459` |
| line-031 | narrator/Mia | `audio/tts/line-031-v4.wav` | 2.080 | -4.65 | `db5090fec0c5527952b0d1c8474e3e4117aedfbb1886b03bbbb9a47d7c2bc218` |
| line-032 | kazama/Dean | `audio/tts/line-032-v1.wav` | 3.680 | -6.72 | `0a5fe5bbb1be402e41251df7a2f842a7cb5a698491e94477072056f05f4fbc94` |
| line-033 | kazama/Dean | `audio/tts/line-033-v1.wav` | 2.880 | -4.46 | `0da32d5282d81fcb353c7fce1cc96a14bc94353009de47b4b834cf006f23566d` |
| line-034 | narrator/Mia | `audio/tts/line-034-v3.wav` | 1.600 | -4.41 | `fe15df917fae857090aa89abb92da19cb41e3c15462883209e8faa7de01faed9` |
| line-035 | shinchan/Milo | `audio/tts/line-007-v2.wav` | 2.560 | -5.76 | `00d6d06c8a52eaa4396c43250fa7b7508160bdaf272c5ea12b34b5b4d1307037` |
| line-036 | shinchan/Milo | `audio/tts/line-036-v1.wav` | 2.080 | -3.72 | `4dbfea4819c8c673ff6731bc26e7e5f1677c09caa84f4fc63ab1bf09e3421643` |
| line-037 | narrator/Mia | `audio/tts/line-037-v3.wav` | 4.960 | -1.70 | `e8231f31680ce49891138c8ab660e79aff911e4abed56ff1cf84f6f30ccd76f6` |
| line-038 | narrator/Mia | `audio/tts/line-038-v3.wav` | 2.880 | -5.50 | `7118a0d1a53d1b73c602cd44084aa089e50753fce5b0b19f6259b194f73a481b` |
| line-039 | narrator/Mia | `audio/tts/line-039-v3.wav` | 2.880 | -4.42 | `7f24189c0f0e8e7bf882d270f84200a36c8962779d7a32ba138b5f6021797c50` |
| line-040 | narrator/Mia | `audio/tts/line-040-v3.wav` | 2.560 | -3.95 | `0027b6d43fbdd7b9f966f57278cff476efacced3e5f410430a583c5be8da4cf4` |
| line-041 | narrator/Mia | `audio/tts/line-041-v3.wav` | 2.560 | -2.12 | `e123c7ba6f0e9a3897a68ddfc0b44827314ed1fa95a53666d40d2d8f8fcc5163` |
| line-042 | nene/Mia | `audio/tts/line-042-v1.wav` | 4.320 | -4.50 | `b62dcd8e1cc74ba0ac51a55aade99ab25a5dff4f825b06c7cb0f2d7a5732958c` |
| line-043 | nene/Mia | `audio/tts/line-043-v1.wav` | 3.040 | -7.25 | `3879f03101664c7c7289a0c1fe9953b98a3ea98cdd7a4d8cc11b63f6391d335e` |
| line-044 | kazama/Dean | `audio/tts/line-044-v2.wav` | 3.040 | -4.05 | `1cec3a7d3cef5973fa2c2b9ad52dd9fdf6e42f645cafab2ca7d829c290eb4ffe` |
| line-045 | kazama/Dean | `audio/tts/line-045-v1.wav` | 2.720 | -2.57 | `4eef092fc86d006a33db5be47a63bc5ba2b6e8d290eed77b9bd0e6c0edc41e78` |
| line-046 | narrator/Mia | `audio/tts/line-046-v3.wav` | 2.880 | -2.93 | `66118694934f8a88794ad21fd7a3cbb79830975a537142b243c48f3a093a3ff6` |
| line-047 | narrator/Mia | `audio/tts/line-047-v3.wav` | 2.720 | -2.73 | `f4e6ac34ee734b5d66d4dd53905653929d121ab79283a298ac2506e647d8c1e5` |
| line-048 | narrator/Mia | `audio/tts/line-048-v3.wav` | 2.720 | -2.73 | `09fa256b46324d2593c4631eef722762748d1da4ca69a96787383ab106d5ae97` |
| line-049 | narrator/Mia | `audio/tts/line-049-v3.wav` | 3.040 | -5.44 | `54d03dbea7b21a3c47005bd72cde2182fdb60b79dd295ef101f78e6176f68c81` |
