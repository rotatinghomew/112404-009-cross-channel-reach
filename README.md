# 展览数字内容的跨入口触达与受众估计

本项目保存视觉艺术机构日常业务分析使用的合成演练资料，样例不代表真实机构、作品、交易或研究结论。

## 资料

- `channels.csv`：展览讲解入口及启停时间。字段为 `channel_id, channel_type, exhibit_id, active_from, active_to, entry_context, campaign_ref`。
- `events.csv`：入口曝光、阅读、播放和反馈事件，参与者代号仅用于演练。字段为 `event_id, channel_id, visitor_token, language, age_band, event_at, event_type, content_id, consent_state, session_key`。
- `aggregation_requests.csv`：受众切片请求及发布状态。字段为 `request_id, period, dimension_set, minimum_group, requested_by, state, created_at`。
- `venue_counts.csv`：馆内场次客流和讲解活动签到汇总，用于与数字渠道口径对照。字段为 `record_id, exhibit_id, gallery_id, period, visitors, guided_visitors, measurement, source_ref`。

记录之间通过 `*_id`、`*_key` 或 `*_ref` 字段关联。日期采用 ISO 格式；空值表示来源未提供该事实，不代表数值为零。不同来源的统计范围和状态以 `docs/data-contract.md` 为准。样例中保留了待确认、取消、缺失和版本变化等原始情况，不包含预先计算的分析结论。

## 运行

需要 Python 3.11 或更高版本，无第三方依赖。运行 `python3 -m unittest discover -s tests -v` 可检查资料编码、字段和记录结构。
