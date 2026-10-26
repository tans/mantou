# 发布检查续审记录

2026-10-26，继续Issue #24/#19/#20。原报告保留，当前原三集报告为speaker-qa-v2，剧情候选为本目录v13；视频和封面不重渲染。

在临时隔离副本中复制social-story配置，其它素材引用原归档，只修改该副本cover.png的字节；运行实际`review_short_series.py`。修正前返回static_status=pass、退出0；修正后返回static_status=fail、cover_fingerprint错误、退出2。原课次文件未修改。

根因：检查入口只遍历音视频/字幕/源文件，漏掉独立封面。修正为校验封面实际SHA、配置设计、三项源引用完整性，并将cover_sha256纳入人工记录身份。候选另需cover_visual=pass，封面改变后旧人工记录失效。缺失输入也返回结构化fail/退出2。

另发现v12清单的focus_method被bindings中的旧source-gesture覆盖；现在复核清单保留assembly中的实际“timed speaker badge and below-frame directional marker”。这不代表真实口型同步或人工听检通过。

实际原三集和两个候选共五个当前报告全部static pass、human pending、publishable false。人工模板继续保持未填写；未新增测试代码或测试文件。
