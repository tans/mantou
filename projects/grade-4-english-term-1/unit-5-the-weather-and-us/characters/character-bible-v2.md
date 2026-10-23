# Unit 5 角色与声线 v2

沿用全局 `shinchan-community-tv-v1` 视觉和 voice-library.md 的固定profile。声音为英语合成声，不是原动画演员配音。教材角色更换为小新角色组，原文姓名仅在line-013明确删去；其余教学词句保留。

| ID | 人物/外观 | Voice profile / voice | 行 |
| --- | --- | --- | --- |
| narrator | 教学旁白 | teacher-en-mia-clarity-v1 / Mia | line-001, line-002 |
| shinchan | 小新 | shinchan-en-milo-v1 / Milo | line-005, line-006, line-011, line-012, line-014, line-016, line-018 |
| kazama | 风间 | kazama-en-dean-v1 / Dean | line-003, line-007, line-008, line-013, line-015, line-017 |
| nene | 妮妮 | nene-en-mia-v1 / Mia | line-004, line-009, line-010 |

小新红上衣黄短裤、粗眉短黑发；风间深蓝侧分发浅蓝上衣深蓝短裤；妮妮橘红双马尾粉裙。shot-06为独立雪景，分别使用红/浅蓝/粉色冬装、手套，延续发型脸型与色系；其它镜头保持日常服装。旁白不出镜。完整模型/style/逐镜关联见lesson-v1.json和storyboard-v1.md。

参考图从Unit 4归档副本复用，官方原图出处在assets/characters/shinchan-official/README.md；新课未改原图。唯一场景参考为Unit 3已生成动画帧，不当作教材证据或新课成片。

## 本课出场与连续性

| 角色 | 出场镜头 | 连续性 |
| --- | --- | --- |
| 小新 | shot-01至shot-10 | 红/黄色系、粗眉短黑发、幼儿比例；shot-06明确更换红色冬装，shot-07回到室内常服 |
| 风间 | shot-01至shot-10 | 浅蓝/深蓝衣着、侧分蓝黑发；shot-06明确浅蓝冬装；shot-07至shot-10沿用同一沙发/雨窗 |
| 妮妮 | shot-01至shot-06、shot-10 | 红色双马尾、粉色衣着；shot-06保暖粉外套；shot-07至shot-09不入画，shot-10重新同框 |
| 教学旁白 | line-001、line-002；不出镜 | Mia clarity，不映射为妮妮或教材人物身份 |

采用声线配置与完整style以lesson-v5.json及audio/manifest-selected-v2.md为准。v2补充出场矩阵，不改voice ID、台词或已采用配音。新课分镜图来自内置image_gen，原图和逐格派生关系见storyboards/scene-reference-manifest-v1.json。
