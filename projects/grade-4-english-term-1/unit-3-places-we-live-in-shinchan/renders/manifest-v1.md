# 视频生成记录 v1

## 初样

`visual-baseline-xiaoguai-h3-v1.mp4`，xiaoguai MiniMax H3，768p，任务 `xg_P1G_kQb2bQ77Veul84JYj`，请求5秒，实际5.166667秒，1376×768，24fps，含AAC音轨（尽管请求静音）。风间过高且脸型成人化，已否决，不能入片。原片与sidecar保留。

## 正式v3镜头

20镜头每次传入三张官方角色图，按各镜头 task-v3.json 记录输入SHA、请求时长、task ID、状态；generation-v3.log保留状态变更。临时SSLEOF查询错误只使用同ID续查，不重复提交。

公开768p价为¥0.08/秒（2026-10-22访问供应商页面），v3冻结计划235秒，估算¥18.80；加5秒初样约¥0.40，加医院补片前总估算¥19.20，实际结算未知。图像生成失败费用未知，TTS实际费用未知，不把未知记为0。

正式镜头下载后另生成无音轨派生片；最终只混入已核实文本的TTS。20个计划镜头现已全部下载并检查首中尾帧；媒体流/SHA见`probe-selected-v8.json`，最终采用表见`../lesson-v8.json`。供应商返回音轨的原片保留，静音派生稿和最终TTS混音关系见`../edit/assembly-v8.md`。

## 教学物件复核

shot-06原片把公共厕所标志与医疗十字混在同一建筑，不直接作为整镜入片。剪辑将公交站/厕所画面裁至左侧1088px避开错误医疗标牌；“There is a hospital.”换用独立医院镜头；“There is also a playground.”换用已核对的shot-03游乐场画面。组合为静音衍生片，原片保留。该修订只用已生成素材，不再调用供应商。

shot-12-v3医院镜头大部分时间停留在商店，直到结尾才转到医院；为保证“see a doctor”与医院画面匹配，另生成医院主体始终入镜的prompt-v4 / hospital-shot-v4.json候选。新增请求11秒768p，公开价估算约¥0.88；旧片保留。

## 完整导出与预算归档

医院v4补片已下载并用于shot-12及shot-06修复。成功视频请求为20个计划镜头+5秒否决初样+11秒医院补片，共251请求秒；按访问时768p公开价估算¥20.08，实际账单未知。TTS与两次内置图片网络失败的结算未知。

当前观看版本：`unit-3-shinchan-vertical-bilingual-v9.mp4`和`unit-3-places-we-live-in-shinchan-bilingual-burned-v8.mp4`；无字幕母版v8。完整媒体探测、哈希、字幕对应和检查状态见`../edit/qa-v9.json`及`../edit/qa-v9.md`。旧v8竖屏仅作为标点换行修复前历史稿。人工全片听检及用户验收未完成。
