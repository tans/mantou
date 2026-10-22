# TTS manifest v1

49 行 MiMo `mimo-v2.5-tts`，voice/style 固定于 `lesson-v1.json` 和角色 Bible；输入哈希见逐 WAV JSON。凭据来自本机忽略配置，不写入清单。

机器检查：WAV 可读、PCM16、单声道、24 kHz，实际时长/峰值/SHA-256 见下。完整逐句人工听检尚未完成；媒体格式及音量检查不能代替发音判断。

| 行 | 角色 / Voice | 秒数 | 峰值 dBFS | SHA-256 |
| --- | --- | --- | --- | --- |
| line-001 | narrator / Chloe | 3.840 | -1.65 | `1f03e57b8aafe4f6c257c769532ea925c83e32c04c6e135f091d9b484df27159` |
| line-002 | narrator / Chloe | 4.000 | -0.21 | `ac4bc7bbc79a00d483b1be952ed3dd14ff32cd5e840b58d688d7ae438920b8d4` |
| line-003 | shinchan / Milo | 2.400 | -2.53 | `e7f71d5cc1f07864eaaef2f71c1f3b5b06b1541c20cf4cb3f8808397045d9998` |
| line-004 | nene / Mia | 2.400 | -3.26 | `b9b6e6a571a8c030df0ef1e43c627aa00ba2af45afc70365610fd60a836d4c0b` |
| line-005 | kazama / Dean | 4.800 | -4.68 | `e50bd6029aac1e94a12666997c652cbb05fea59aefba1bcfc145a6afc1f0870d` |
| line-006 | shinchan / Milo | 2.720 | -0.09 | `b9dacd8dac46b9135a648404524e4030e23d0df2ab48c62359295fb71d62e081` |
| line-007 | shinchan / Milo | 2.880 | -1.81 | `b4e6687b7a226f816b85253601ca14723ed9fd35b43e0f13abc2c77d215b5835` |
| line-008 | shinchan / Milo | 2.880 | -0.09 | `f26ad3b9f61a22ac82231aa1f1259be54983f8594e3522dd7b6dea6fbc5969cf` |
| line-009 | nene / Mia | 2.080 | -6.31 | `db79bdf1bd34788d84521823454de9da0189660c83252a58551851833a2e5224` |
| line-010 | shinchan / Milo | 7.360 | -6.38 | `47b0c2696b94c67e8cae8b38a5ac7c0acb49a73df8326da3a6e3a7b57696b0f6` |
| line-011 | kazama / Dean | 3.360 | -0.09 | `f51fb58368359232bf9e5bdc810a5276a9fbf4f1c4e8a52d5d31f0343ead666b` |
| line-012 | narrator / Chloe | 7.360 | -1.66 | `5954018b6e78cac7b170f2f1f40e96063af3127927a2832227f5a8a37341a002` |
| line-013 | shinchan / Milo | 2.400 | -10.63 | `7e52ddde34f7685e5f2bae9e91728e6c104a90cd9321b4d668af5d11b2e09e1c` |
| line-014 | shinchan / Milo | 2.880 | -0.09 | `59219aabb7c53c21617fd032c209809b533091fa27ff3cafa2f767de0ca033c7` |
| line-015 | nene / Mia | 2.880 | -5.20 | `959645569d3a9840471ec125e0e2b757075192b0cf27e952210269d503ab142d` |
| line-016 | narrator / Chloe | 4.320 | -0.10 | `bb13941a4675fb6a644862c75e14b76a8504f981318915ad689a8afd33570b58` |
| line-017 | nene / Mia | 5.440 | -3.10 | `b6fe8af3bb130223ec389b5a84c31171ed189220fafeb28d9907112823358cf2` |
| line-018 | kazama / Dean | 3.520 | -4.87 | `a6016c18646ac51ed9fc6f5c1ae5cdccc386868f37dba2763b51025bcf31793e` |
| line-019 | kazama / Dean | 4.160 | -8.08 | `d177e0a879dd40e05a21825509985dbf5c4a7cd9eb5553ae788f4d5c8c02d977` |
| line-020 | shinchan / Milo | 4.000 | -3.09 | `d13065d832e2d4b2ee66577051178544db67f13ba488c0516066831ccd3c5a32` |
| line-021 | kazama / Dean | 4.160 | -0.09 | `d66c82f2ec833f9a460f69efd0545e7833095c3befb6f206c86519084c8f8d59` |
| line-022 | nene / Mia | 3.680 | -3.59 | `88b8ec9bf9e44df1d4d2cec5146f5476811f2c610789c25d6a0b275353e376ac` |
| line-023 | kazama / Dean | 4.000 | -4.38 | `d77bf693121a6e8c0081f7a1f1044b4ace77e7d88f8ab90f8222fe5ac6ff385b` |
| line-024 | shinchan / Milo | 3.680 | -0.09 | `64b4d59b9d6503be1188205c193a8cb7b4017e7e0b48ae8488ef8af4e5617b77` |
| line-025 | narrator / Chloe | 2.240 | -2.16 | `e3d15ed6e28da02c3b9ce8d02af0df491538c2fc9d0e735e52465bfbffc4e741` |
| line-026 | kazama / Dean | 3.360 | -3.84 | `575f2a99163acc7487162d5e685d3369c8dabce26823c237d3425129db914a4c` |
| line-027 | kazama / Dean | 3.840 | -2.10 | `1e023a01dffb0c1642e01710e16bd0c360e1b571e07d38a402589a084e2e83cf` |
| line-028 | narrator / Chloe | 2.080 | -0.45 | `ef09f6238266d0395245b425a61ef88b136050493f2c0a530c12f198482e87bc` |
| line-029 | nene / Mia | 2.720 | -7.92 | `33aac39813373ce2a03b17cd216454bea1c91f2475eb2080312253becea991b1` |
| line-030 | nene / Mia | 6.880 | -2.44 | `54bf1a67899688acfcd9b46d2c5d8fb01860bc87959e3ce4959fcb6aa9c33edc` |
| line-031 | narrator / Chloe | 1.920 | -2.71 | `45e11e1f0efeed9c45221aa27cb0ad7f8a910961f9b419c8ce5e652cf9abe9c9` |
| line-032 | kazama / Dean | 3.680 | -6.72 | `0a5fe5bbb1be402e41251df7a2f842a7cb5a698491e94477072056f05f4fbc94` |
| line-033 | kazama / Dean | 2.880 | -4.46 | `0da32d5282d81fcb353c7fce1cc96a14bc94353009de47b4b834cf006f23566d` |
| line-034 | narrator / Chloe | 1.920 | -2.50 | `46be9adb2415e9f97413d9e6ed3875c200e9ffd5f247b41f56e19d204dd864db` |
| line-035 | shinchan / Milo | 7.360 | -0.77 | `90166a67af141397440b985042965f7b4d970d64c3978ff6822e048127cdba85` |
| line-036 | shinchan / Milo | 2.080 | -3.72 | `4dbfea4819c8c673ff6731bc26e7e5f1677c09caa84f4fc63ab1bf09e3421643` |
| line-037 | narrator / Chloe | 9.600 | -0.09 | `d3cd17ef770884da0b054cde0a5b23c823d84fbdc37a1321813ce7037d76ccc6` |
| line-038 | narrator / Chloe | 3.520 | -0.09 | `1718a6f9fdef69b9e57ef31fe687948de7c27f53efe5825c1caa1ced14ff110a` |
| line-039 | narrator / Chloe | 4.640 | -1.68 | `c599dbc17c384252459ee0d63c5d2f747ed479caa7c95e1028cb7f5962b96204` |
| line-040 | narrator / Chloe | 3.840 | -2.99 | `e073768315853ea000ba923af40a87e157513d6332ef7d0ae86493f2bec6530f` |
| line-041 | narrator / Chloe | 4.000 | -1.39 | `0740f79d80ff8ab201125eea0db4b6bb726d86043f08df48595be1956b962470` |
| line-042 | nene / Mia | 4.320 | -4.50 | `b62dcd8e1cc74ba0ac51a55aade99ab25a5dff4f825b06c7cb0f2d7a5732958c` |
| line-043 | nene / Mia | 3.040 | -7.25 | `3879f03101664c7c7289a0c1fe9953b98a3ea98cdd7a4d8cc11b63f6391d335e` |
| line-044 | kazama / Dean | 7.200 | -2.39 | `bbc0a05bd8fcc6d3136d887ca68320ff4a35d1f331c028c67bb0072e53f269e0` |
| line-045 | kazama / Dean | 2.720 | -2.57 | `4eef092fc86d006a33db5be47a63bc5ba2b6e8d290eed77b9bd0e6c0edc41e78` |
| line-046 | narrator / Chloe | 3.840 | -4.11 | `5ff76230c07d14dc2cf019f735eddc974c3b0fc0a533ec5fe0caf6335e3c26ff` |
| line-047 | narrator / Chloe | 7.520 | -0.09 | `8b62a4d2a08f10f5058ff821999c8e5d12cb3fd6d5df8d6fea94742eb7d4c2c6` |
| line-048 | narrator / Chloe | 4.160 | -0.09 | `59465ab8cba702fee7117e034cbb1cd0e4bf0c214cb555f1e04a7bbe66e61bc6` |
| line-049 | narrator / Chloe | 4.160 | -0.09 | `00e1291778fa9559e73b3f9a8356a4d86eea16cfc4904ec0b23ded1a7d00a0c4` |
