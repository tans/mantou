# Unit 5 采用镜头清单 v7

全部10个采用任务由供应商GET确认succeeded，实际seed/steps/尺寸/时间字段见provider-job-records-v1.json。原始返回音轨保留在源片；合成仅用独立无音轨派生片。

| 镜头 | task ID | 原片 | 原片SHA-256 | 静音派生SHA-256 | 底部裁切px | 末帧延长s |
| --- | --- | --- | --- | --- | --- | --- |
| shot-01 | job_3db1bfe39f604167998863e5ba242388 | renders/shot-01-minixm-8188-v2.mp4 | `6d315f4a7708528ec80f20f51d12deed0d4d39bef5f27febd999bcc52d239254` | `f32b0639410bd7e2ed942a986df037e4a3cbbf6943f9d6c487b750cae36e8341` | 0 | 0.000000 |
| shot-02 | job_700e1888dca24277819679868ae584d8 | renders/shot-02-minixm-8188-v2.mp4 | `0086808183924c6532a78a59a2c168f2a3d3600eac59e39c791a5a0c0ec59d81` | `2f2a544ed85dda5b35ca4bc994ede659fae19f69cb0a9dcb32f5d43f9cc062f5` | 0 | 0.000000 |
| shot-03 | job_325a2980993b4e5bb039f30b9cd54d89 | renders/shot-03-minixm-8188-v2.mp4 | `89bb87d0a5e7b6ba21cf18e76ea54bc9f4c1204ddef6222298a94f4cc06a262c` | `b909d37531f45c29deac0a4ce3fae1aff5723af19444675ebd51ff856497f78d` | 0 | 3.208333 |
| shot-04 | job_f5e4bbff0bd24580a8f0c9e22acae3b9 | renders/shot-04-minixm-8188-v2.mp4 | `736b190ccabc0cc96db791f6f173e36f7ee5401c7a4ffff2d28f4f8a03514097` | `73be43ae89200494c50cfe7e2388ceafe3b90a61449619ce8beb88376e5c21b9` | 0 | 2.708333 |
| shot-05 | job_6a0b92728ab145eda328b6dc553be8aa | renders/shot-05-minixm-8188-v2.mp4 | `fbd325c297e4feaa12666bf106394615a25c97f1e28d89606e7d5f3a90d2f570` | `4a00fc773c043eab71bebc664de8991aec3d24e04dba0ea813f7f1ab3b78aa36` | 0 | 5.125000 |
| shot-06 | job_d14a8c1e6dc34514a934913f224a4740 | renders/shot-06-minixm-8188-v2.mp4 | `82419760f91f4f7ff70c3e642387abdda9bd709621d4d219365f1348eb4ee763` | `166a5a342956b73a9ed8b62f48a2406db355d7260d01ab1c2ff7e3bd4ca9a545` | 0 | 1.416666 |
| shot-07 | job_8d8f9a19280340a2a83d419c745ee939 | renders/shot-07-minixm-8188-v2.mp4 | `d6f215854d75dfd2244ee0852509252bb043715a318a1dca099ca2f838e9be8f` | `fd1c26c22b76c01aaefaf96d0187f500b990d9ef04c76657b7f68797a4a1ac71` | 0 | 2.541666 |
| shot-08 | job_25b720ebdef7434ab6c15fe4d38a733d | renders/shot-08-minixm-8188-v2.mp4 | `d5032a930113f9d6dbd4ec4b43fa4e74638ccb81d397e7f4afba4298ec5d0352` | `f7300bc4082816617d130e2ecba9bfe7b579599cb6d5fbe908716eb61b650950` | 0 | 5.750000 |
| shot-09 | job_b8155163a57249dabe41587659831e53 | renders/shot-09-minixm-8188-v2.mp4 | `a9429b1af3ab61ec769705993b3b1cad1afba88b01e1a91365f642926aaaf3bd` | `39ab58c4d50bd5040a4485ca534dba7d15551feb8ee6d6477e8aeee1f8caed69` | 44 | 2.375000 |
| shot-10 | job_8864504f3be94124af6b38d74437ac88 | renders/shot-10-minixm-8188-v2.mp4 | `ba68233e042bc69660c1817812196afb24c7410368c6bfe5aeab4f4b222cc38b` | `1e55e332d0b2ced7afa0b6f2ff4b36cf0d5d7edc34167946b5e73ba5b119f281` | 44 | 4.166666 |

首镜v1拒用候选保留，不计入10个采用镜头。媒体探测、全文件解码与视觉记录分别见逐镜probe、edit/qa-v7.md和storyboards。
